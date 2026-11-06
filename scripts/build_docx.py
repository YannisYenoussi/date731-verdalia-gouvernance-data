"""Genere livrables/dossier/DATE731_Verdalia_Dossier_Architecture.docx a partir du Markdown (source de reference).
Prerequis : pandoc, python-docx. Usage : python3 scripts/build_docx.py"""
import re, subprocess, pathlib, tempfile, copy
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "livrables" / "dossier" / "DATE731_Verdalia_Dossier_Architecture.docx"
DG, GREEN, LIGHT = "1B5E20", "2E7D32", "E8F5E9"

MAIN = ["00-synthese-executive", "01-contexte-besoins", "02-cartographie-donnees", "03-cycle-vie-donnees",
        "04-architecture-cible", "05-gouvernance-raci", "06-rgpd-ia-responsable", "07-risques-mesures",
        "08-trajectoire", "09-matrice-tracabilite", "10-conclusion"]
BACK = ["sources/BIBLIOGRAPHIE", "sources/IAGRAPHIE"]
ANNEX = ["tracabilite/exigences", "architecture/comparaison-architectures", "architecture/kpi-et-lineage",
         "architecture/data-warehouse-modele", "architecture/assistant-ia-api", "architecture/choix-fournisseur",
         "donnees/mdm-client", "donnees/qualite-donnees", "donnees/classification-donnees-critiques",
         "gouvernance/roles-et-definitions", "gouvernance/raci", "gouvernance/politique-classification",
         "gouvernance/politique-acces", "rgpd/registre-traitements", "rgpd/durees-conservation",
         "rgpd/aipd-analyse", "rgpd/ia-ai-act-risques", "adr/ADR-001-architecture-cible",
         "adr/ADR-002-assistant-ia-via-api", "adr/ADR-003-pseudonymisation-warehouse",
         "sources/HYPOTHESES_QUESTIONS"]

LINK = re.compile(r"(?<!\!)\[([^\]]+)\]\((?!http)[^)]*\)")
IMG = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
CODE_LINK = re.compile(r"`([^`]*scripts/[^`]*)`")


def clean(md_path: pathlib.Path, shift: int) -> str:
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"^Suite : .*$|^Précédent : .*$|^Précédent : .*Suite : .*$", "", text, flags=re.M)

    def img(m):
        alt, rel = m.group(1), m.group(2)
        p = (md_path.parent / rel).resolve()
        w = "11cm" if "architecture-globale" in rel else ("13cm" if "05-acces" in rel else "15.5cm")
        return f"![{alt}]({p}){{width={w}}}"
    text = IMG.sub(img, text)
    text = LINK.sub(r"\1", text)
    # remonter ou abaisser les titres
    out, in_code = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("#") and shift:
            line = "#" * shift + line
        out.append(line)
    return "\n".join(out) + "\n\n"


def build_markdown() -> str:
    parts = []
    for n in MAIN:
        parts.append(clean(ROOT / "docs" / f"{n}.md", 0))
    for n in BACK:
        parts.append(clean(ROOT / "docs" / f"{n}.md", 0))
    parts.append("# Annexes\n\nLes annexes détaillent les chapitres. Elles reprennent les documents du dépôt Git.\n\n")
    for n in ANNEX:
        parts.append(clean(ROOT / "docs" / f"{n}.md", 1))
    return "".join(parts)


def set_cell_bg(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def set_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:space"), "0"); el.set(qn("w:color"), "A9B8AB")
        borders.append(el)
    tblPr.append(borders)


def add_field(run, instr):
    for t, txt in (("begin", None), (None, instr), ("end", None)):
        if t:
            c = OxmlElement("w:fldChar"); c.set(qn("w:fldCharType"), t); run._r.append(c)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; run._r.append(it)


def style_reference(path):
    subprocess.run(["pandoc", "-o", str(path), "--print-default-data-file", "reference.docx"], check=True)
    d = Document(str(path))
    by = {st.name.lower(): st for st in d.styles}
    by["normal"].font.name = "Calibri"; by["normal"].font.size = Pt(11)
    for sn, size in (("heading 1", 20), ("heading 2", 15), ("heading 3", 12.5), ("heading 4", 11.5)):
        s = by[sn]; s.font.name = "Calibri"; s.font.size = Pt(size); s.font.bold = True
        s.font.color.rgb = RGBColor.from_string(DG if sn != "heading 3" else GREEN)
    for sn in ("body text", "first paragraph", "compact"):
        if sn in by:
            by[sn].font.name = "Calibri"; by[sn].font.size = Pt(10.5)
    d.save(str(path))


def post_process(docx_path):
    d = Document(str(docx_path))
    # tableaux : bordures, en-tete vert, police reduite, largeur
    for t in d.tables:
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_borders(t)
        t.autofit = True
        ncol = len(t.columns)
        size = 9 if ncol <= 5 else (8 if ncol <= 8 else 7)
        for ri, row in enumerate(t.rows):
            for cell in row.cells:
                if ri == 0:
                    set_cell_bg(cell, GREEN)
                elif ri % 2 == 0:
                    set_cell_bg(cell, "F2F4F2")
                for p in cell.paragraphs:
                    p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
                    for r in p.runs:
                        r.font.size = Pt(size)
                        if ri == 0:
                            r.font.bold = True; r.font.color.rgb = RGBColor(255, 255, 255)
        # repeter l'en-tete et eviter de couper une ligne
        for ri, row in enumerate(t.rows):
            trPr = row._tr.get_or_add_trPr()
            cs = OxmlElement("w:cantSplit"); trPr.append(cs)
            if ri == 0:
                th = OxmlElement("w:tblHeader"); trPr.append(th)
    # images centrees
    for p in d.paragraphs:
        if p._p.xpath(".//w:drawing"):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = False
    # marges
    for s in d.sections:
        s.left_margin = s.right_margin = Cm(2.0); s.top_margin = Cm(2.2); s.bottom_margin = Cm(2.0)

    # pied de page : numerotation
    for s in d.sections:
        s.footer.is_linked_to_previous = False
        fp = s.footer.paragraphs[0] if s.footer.paragraphs else s.footer.add_paragraph()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run("DATE731 — Verdalia — page "); r.font.size = Pt(9)
        r2 = fp.add_run(); r2.font.size = Pt(9); add_field(r2, "PAGE")
    d.save(str(docx_path))


def add_cover_and_toc(docx_path):
    d = Document(str(docx_path))
    body = d.element.body
    first = body[0]
    new = []

    def para(text="", size=11, bold=False, color=None, align=WD_ALIGN_PARAGRAPH.CENTER, before=0, after=6):
        p = d.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
        r = p.add_run(text); r.font.size = Pt(size); r.font.bold = bold
        if color:
            r.font.color.rgb = RGBColor.from_string(color)
        new.append(p._p); return p

    para("", before=40)
    para("EPSI — Master 1", 13, False, GREEN)
    para("DATE731 — Data Gouvernance et IA responsable", 16, True, DG, before=6)
    para("", before=30)
    para("VERDALIA", 40, True, DG)
    para("Donner une base commune aux données d'un réseau de magasins", 18, False, GREEN, after=12)
    para("Dossier d'architecture Data", 22, True, DG, before=20)
    para("Gouvernance, RGPD, IA responsable et trajectoire de déploiement", 13, False, "4C6B50", after=40)
    para("Groupe de trois étudiants (Sujet 1)", 12, True, DG, before=20)
    for role in ("Membre 1 — Analyse et données : [nom et prénom à compléter]",
                 "Membre 2 — Architecture et déploiement : [nom et prénom à compléter]",
                 "Membre 3 — Gouvernance et conformité : [nom et prénom à compléter]"):
        para(role, 11, False, None, after=3)
    para("Enseignant : [à compléter]        Date de remise : [à compléter]", 11, False, None, before=30)
    para("Version 0.1 — 6 novembre 2026 — premier jet à relire (voir IAgraphie)", 10, False, "6B7B6E", before=30)
    br = d.add_paragraph(); br.add_run().add_break(WD_BREAK.PAGE); new.append(br._p)

    # Table des matieres (champ Word a mettre a jour a l'ouverture)
    para("Table des matières", 20, True, DG, align=WD_ALIGN_PARAGRAPH.LEFT, after=10)
    tp = d.add_paragraph(); new.append(tp._p)
    r = tp.add_run()
    for t, txt in (("begin", None), (None, 'TOC \\o "1-2" \\h \\z \\u'), ("separate", None), ("end", None)):
        if t:
            c = OxmlElement("w:fldChar"); c.set(qn("w:fldCharType"), t); r._r.append(c)
            if t == "separate":
                tt = OxmlElement("w:t"); tt.text = "Clic droit puis « Mettre à jour les champs » pour afficher la table des matières."; r._r.append(tt)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)
    br2 = d.add_paragraph(); br2.add_run().add_break(WD_BREAK.PAGE); new.append(br2._p)

    for el in new:
        body.remove(el)
    idx = list(body).index(first)
    for k, el in enumerate(new):
        body.insert(idx + k, el)

    # forcer la mise a jour des champs a l'ouverture
    settings = d.settings.element
    upd = OxmlElement("w:updateFields"); upd.set(qn("w:val"), "true"); settings.append(upd)
    # saut de page avant chaque titre 1
    for p in d.paragraphs:
        if p.style.name.lower() == "heading 1":
            p.paragraph_format.page_break_before = True
    d.core_properties.title = "DATE731 — Verdalia — Dossier d'architecture Data"
    d.core_properties.author = "Groupe DATE731"
    d.save(str(docx_path))


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        md = tmp / "dossier.md"
        md.write_text(build_markdown(), encoding="utf-8")
        ref = tmp / "reference.docx"
        style_reference(ref)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["pandoc", str(md), "-f", "markdown+pipe_tables+implicit_figures-smart", "-o", str(OUT),
                        f"--reference-doc={ref}", "--resource-path", str(ROOT)], check=True)
    post_process(OUT)
    add_cover_and_toc(OUT)
    print("Ecrit :", OUT.relative_to(ROOT), f"({OUT.stat().st_size // 1024} Ko)")


if __name__ == "__main__":
    main()
