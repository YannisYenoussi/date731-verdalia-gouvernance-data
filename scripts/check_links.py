"""Verifie les liens internes des fichiers Markdown (fichiers cibles et ancres). Usage : python3 scripts/check_links.py"""
import re, sys, pathlib
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)|!\[[^\]]*\]\(([^)\s]+)\)")


def slug(heading: str) -> str:
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def anchors(path: pathlib.Path) -> set:
    out, in_code = set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("#"):
            out.add(slug(line.lstrip("#")))
    return out


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


errors, checked = [], 0
for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = strip_code(md.read_text(encoding="utf-8"))
    text = re.sub(r"`[^`]*`", "", text)
    for m in LINK.finditer(text):
        target = m.group(1) or m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        checked += 1
        file_part, _, anchor = target.partition("#")
        dest = md if file_part == "" else (md.parent / unquote(file_part)).resolve()
        if not dest.exists():
            errors.append(f"{md.relative_to(ROOT)} : fichier introuvable -> {target}")
            continue
        if anchor and dest.suffix == ".md" and slug(unquote(anchor)) not in anchors(dest):
            errors.append(f"{md.relative_to(ROOT)} : ancre introuvable -> {target}")

print(f"{checked} liens internes controles")
for e in errors:
    print("ERREUR", e)
print("OK" if not errors else f"{len(errors)} erreur(s)")
sys.exit(1 if errors else 0)
