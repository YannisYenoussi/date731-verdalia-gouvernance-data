"""Verifie que chaque ligne de la matrice RACI (docs/05-gouvernance-raci.md) a un et un seul A et au moins un R."""
import re, sys, pathlib

path = pathlib.Path(__file__).resolve().parent.parent / "docs" / "05-gouvernance-raci.md"
lines = path.read_text(encoding="utf-8").splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("| Activité"))
rows = []
for l in lines[start + 2:]:
    if not l.startswith("|"):
        break
    cells = [c.strip() for c in l.strip("|").split("|")]
    rows.append((cells[0], cells[1:]))

ok = True
for name, vals in rows:
    a, r = vals.count("A"), vals.count("R")
    bad = [v for v in vals if v not in {"A", "R", "C", "I"}]
    status = "OK" if a == 1 and r >= 1 and not bad else "ERREUR"
    if status == "ERREUR":
        ok = False
    print(f"{status:7} A={a} R={r}  {name}")
print(f"{len(rows)} lignes controlees")
sys.exit(0 if ok else 1)
