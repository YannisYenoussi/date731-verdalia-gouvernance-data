"""Genere livrables/soutenance/DATE731_Verdalia_Soutenance.pptx (13 diapositives + 1 annexe).
Les notes des orateurs sont extraites de presentation/SCRIPT_ORAL.md. Prerequis : python-pptx, Pillow.
Usage : python3 scripts/build_pptx.py"""
import re, pathlib
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIAG = ROOT / "docs" / "diagrammes"
OUT = ROOT / "livrables" / "soutenance" / "DATE731_Verdalia_Soutenance.pptx"
C_DARK, C_GREEN, C_LIGHT, C_GREY, C_TEXT, C_WHITE = (RGBColor.from_string(x) for x in
    ("1B5E20", "2E7D32", "E8F5E9", "F2F4F2", "1B3A1F", "FFFFFF"))
FONT = "Calibri"
SW, SH = 13.333, 7.5

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(SW), Inches(SH)
BLANK = prs.slide_layouts[6]


def notes_from_script():
    txt = (ROOT / "presentation" / "SCRIPT_ORAL.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"\[Diapo (\d+)\]\n(.*?)(?=\n\[Diapo|\n## |\Z)", txt, flags=re.S):
        out[int(m.group(1))] = m.group(2).strip()
    return out


NOTES = notes_from_script()


def rect(slide, x, y, w, h, fill, line=None, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line; s.line.width = Pt(1)
    s.shadow.inherit = False
    return s


def text(slide, x, y, w, h, content, size=18, bold=False, color=C_TEXT, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, bullets=False, spacing=4):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05); tf.margin_top = tf.margin_bottom = Inches(0.03)
    lines = content if isinstance(content, list) else [content]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align; p.space_after = Pt(spacing)
        r = p.add_run(); r.text = ("•  " + ln) if bullets else ln
        r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = FONT
    return tb


def picture(slide, path, x, y, w, h):
    """Place l'image dans la boite (x, y, w, h) en conservant le ratio, centree."""
    iw, ih = Image.open(path).size
    ratio = min(w / iw, h / ih)
    pw, ph = iw * ratio, ih * ratio
    slide.shapes.add_picture(str(path), Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))


def base(n, title, speaker, subtitle=None):
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, SW, 1.05, C_DARK)
    rect(s, 0, 1.05, SW, 0.06, C_GREEN)
    text(s, 0.5, 0.12, 10.8, 0.8, title, 30, True, C_WHITE, anchor=MSO_ANCHOR.MIDDLE)
    if speaker:
        tag = rect(s, 11.3, 0.3, 1.6, 0.45, C_GREEN, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        text(s, 11.3, 0.3, 1.6, 0.45, speaker, 13, True, C_WHITE, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
    rect(s, 0, 7.1, SW, 0.4, C_GREY)
    text(s, 0.5, 7.12, 9, 0.35, "DATE731 — Verdalia — Data Gouvernance et IA responsable — EPSI M1", 11, False, RGBColor.from_string("4C6B50"), anchor=MSO_ANCHOR.MIDDLE)
    text(s, 12.0, 7.12, 0.9, 0.35, str(n) if isinstance(n, int) else n, 11, True, C_DARK, PP_ALIGN.RIGHT, MSO_ANCHOR.MIDDLE)
    if subtitle:
        text(s, 0.5, 1.2, 12.3, 0.5, subtitle, 17, False, RGBColor.from_string("4C6B50"))
    if isinstance(n, int) and n in NOTES:
        s.notes_slide.notes_text_frame.text = NOTES[n]
    return s


def arrow(slide, x1, y1, x2, y2, dashed=False, color=None):
    from pptx.enum.shapes import MSO_CONNECTOR
    from pptx.oxml.ns import qn
    from lxml import etree
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color or RGBColor.from_string("3F6B45"); c.line.width = Pt(2)
    ln = c.line._get_or_add_ln()
    if dashed:
        d = etree.SubElement(ln, qn("a:prstDash")); d.set("val", "dash")
    t = etree.SubElement(ln, qn("a:tailEnd")); t.set("type", "triangle")
    return c


def box(slide, x, y, w, h, label, fill=C_LIGHT, color=C_TEXT, size=14, bold=False, line=RGBColor.from_string("1B5E20")):
    r = rect(slide, x, y, w, h, fill, line, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    r.adjustments[0] = 0.12
    text(slide, x, y, w, h, label, size, bold, color, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE, spacing=0)
    return r


def card(slide, x, y, w, h, head, body, head_size=18, body_size=15, fill=C_LIGHT, dy=0.62):
    rect(slide, x, y, w, h, fill, RGBColor.from_string("A9B8AB"))
    rect(slide, x, y, 0.09, h, C_GREEN)
    text(slide, x + 0.2, y + 0.08, w - 0.3, 0.5, head, head_size, True, C_DARK)
    text(slide, x + 0.2, y + dy, w - 0.3, h - dy - 0.05, body, body_size, False, C_TEXT)


def table(slide, x, y, w, rows, col_w, font=13, row_h=0.42, head_size=None, highlight_first=False):
    nr, nc = len(rows), len(rows[0])
    gt = slide.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(row_h * nr))
    t = gt.table
    tblPr = gt._element.graphic.graphicData.tbl.tblPr
    tblPr.set("bandRow", "0"); tblPr.set("firstRow", "0")
    for j, cw in enumerate(col_w):
        t.columns[j].width = Inches(cw)
    for i, row in enumerate(rows):
        t.rows[i].height = Inches(row_h)
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.margin_left = c.margin_right = Inches(0.08); c.margin_top = c.margin_bottom = Inches(0.03)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid()
            if i == 0:
                c.fill.fore_color.rgb = C_GREEN
            elif highlight_first and i == 1:
                c.fill.fore_color.rgb = RGBColor.from_string("C8E6C9")
            else:
                c.fill.fore_color.rgb = C_WHITE if i % 2 else C_GREY
            tf = c.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            r = p.add_run(); r.text = val
            r.font.size = Pt(head_size or font) if i == 0 else Pt(font)
            r.font.bold = (i == 0) or (highlight_first and i == 1)
            r.font.name = FONT
            r.font.color.rgb = C_WHITE if i == 0 else C_TEXT
            p.alignment = PP_ALIGN.LEFT
    return t


# ---------------- Diapositive 1
s = base(1, "Verdalia : une base commune pour les données", "Personne 1",
         "Entreprise fictive de jardinage et d'équipement extérieur. Mission : concevoir, sans développer.")
stats = [("14", "magasins"), ("520", "salariés"), ("190 M€", "chiffre d'affaires"), ("600 000", "clients fidélisés"),
         ("6 M", "tickets de caisse par an"), ("400 000", "commandes e-commerce par an")]
for i, (v, l) in enumerate(stats):
    x = 0.6 + (i % 3) * 4.1; y = 2.1 + (i // 3) * 1.75
    rect(s, x, y, 3.8, 1.5, C_LIGHT, RGBColor.from_string("A9B8AB"))
    text(s, x, y + 0.12, 3.8, 0.8, v, 38, True, C_DARK, PP_ALIGN.CENTER)
    text(s, x, y + 0.92, 3.8, 0.5, l, 16, False, C_TEXT, PP_ALIGN.CENTER)
rect(s, 0.6, 5.7, 12.1, 1.1, C_DARK)
text(s, 0.8, 5.72, 11.7, 1.06, "Question : comment donner à 14 magasins une base de données commune, fiable et conforme, "
     "qui supporte aussi un assistant IA, sans accumuler de technologies ingouvernables ?", 19, True, C_WHITE, anchor=MSO_ANCHOR.MIDDLE)

# ---------------- Diapositive 2
s = base(2, "Problèmes rencontrés", "Personne 1", "Cinq sources qui ne se parlent pas : ERP, caisses, e-commerce, CRM, Excel")
probs = [("Clients en double", "Orthographes et identifiants incohérents"),
         ("Chiffres contradictoires", "Le CA change selon le service"),
         ("Pas de définition des KPI", "Aucun glossaire commun validé"),
         ("Exports par e-mail", "Données clients hors de tout contrôle"),
         ("Responsables flous", "Durées de conservation inconnues"),
         ("Traçabilité absente", "Impossible d'expliquer un chiffre")]
for i, (h, b) in enumerate(probs):
    card(s, 0.6 + (i % 3) * 4.1, 2.0 + (i // 3) * 2.35, 3.85, 2.1, h, b, 20, 17)
text(s, 0.6, 6.7, 12, 0.4, "Risque double : décisions fragiles et non-conformité RGPD.", 16, True, C_DARK)

# ---------------- Diapositive 3
s = base(3, "Cartographie des données", "Personne 1", "Un propriétaire métier (Data Owner) proposé pour chaque domaine")
rows = [["Source", "Contenu", "Data Owner proposé"],
        ["ERP", "catalogue, stocks, achats", "Achats et approvisionnement"],
        ["Caisses", "tickets de vente", "Commercial et exploitation"],
        ["E-commerce", "commandes, comptes", "Responsable e-commerce"],
        ["CRM fidélité", "profils, points, consentements", "Marketing et relation client"],
        ["Excel", "exports, suivis", "Propriétaire déclaré"]]
table(s, 0.6, 1.9, 7.6, rows, [1.7, 3.0, 2.9], 14, 0.55)
text(s, 8.6, 1.85, 4.2, 0.5, "Quatre familles de données", 20, True, C_DARK)
fam = [("Opérationnelles", "tickets, commandes, mouvements"), ("De référence", "clients, produits, magasins"),
       ("Sensibles", "identité, contacts, marge"), ("Stratégiques", "KPI financiers certifiés")]
for i, (h, b) in enumerate(fam):
    card(s, 8.6, 2.4 + i * 1.05, 4.2, 0.95, h, b, 15, 13, dy=0.42)
    # le corps est place sous le titre ; reduit pour tenir
text(s, 0.6, 5.5, 7.6, 1.3, ["Opérationnel : état courant, lu en temps réel (stock).",
                              "Analytique : copie consolidée de la veille (Warehouse).",
                              "À mesurer d'abord : écart de 50 000 entre 650 000 profils et 600 000 clients."], 15, False, C_TEXT, bullets=True)

# ---------------- Diapositive 4
s = base(4, "Objectifs et dix exigences", "Personne 1", "Chaque exigence a une solution, un responsable et un critère de vérification")
axes = [("Fiabiliser", ["EX-01 Vue unique du client", "EX-07 Qualité minimale", "EX-05 Traçabilité des KPI"]),
        ("Partager", ["EX-02 Définitions communes des KPI", "EX-03 Un responsable par jeu de données"]),
        ("Protéger", ["EX-04 RGPD des données clients", "EX-06 Droits d'accès par profil",
                      "EX-08 Encadrement de l'IA", "EX-09 Fournisseur et réversibilité"]),
        ("Planifier", ["EX-10 Jalons à 6 et 12 mois"])]
for i, (h, items) in enumerate(axes):
    x = 0.6 + i * 3.1
    rect(s, x, 2.0, 2.9, 4.6, C_LIGHT, RGBColor.from_string("A9B8AB"))
    rect(s, x, 2.0, 2.9, 0.65, C_GREEN)
    text(s, x, 2.0, 2.9, 0.65, h, 22, True, C_WHITE, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
    text(s, x + 0.12, 2.8, 2.7, 3.7, items, 16, False, C_TEXT, spacing=10)

# ---------------- Diapositive 5
s = base(5, "Comparaison des architectures", "Personne 2", "Dix critères pondérés, notes qualitatives de 1 à 5, quatre jeux de poids testés")
rows = [["Option", "Poids du groupe", "Poids égaux", "Évolutivité", "Délai et coût"],
        ["Warehouse + MDM (retenu)", "4,20", "4,10", "3,90", "4,20"],
        ["Hybride", "3,80", "3,60", "3,75", "3,55"],
        ["Lakehouse", "3,30", "3,10", "3,65", "2,95"],
        ["Data Lake", "2,45", "2,50", "2,75", "2,50"],
        ["Data Mesh", "2,30", "2,10", "2,90", "1,95"]]
table(s, 0.6, 1.95, 12.1, rows, [4.1, 2.0, 2.0, 2.0, 2.0], 17, 0.58, highlight_first=True)
text(s, 0.6, 5.6, 12.1, 1.4, ["Les notes sont des appréciations du groupe, pas des mesures.",
                               "Premier dans les quatre scénarios ; écart réduit à 0,15 point si l'évolutivité domine : limite assumée.",
                               "Data Mesh et Data Lake : trop lourds ou trop peu structurés pour 14 magasins."], 16, False, C_TEXT, bullets=True)

# ---------------- Diapositive 6
s = base(6, "Architecture retenue", "Personne 2", None)
SRCS = ["ERP", "Caisses magasins", "Site e-commerce", "CRM fidélité", "Excel maîtrisés"]
for i, lab in enumerate(SRCS):
    y = 1.4 + i * 0.88
    box(s, 0.35, y, 1.75, 0.72, lab, C_GREY, C_TEXT, 14, line=RGBColor.from_string("8A9A8C"))
    arrow(s, 2.1, y + 0.36, 2.55, 3.75)
text(s, 0.35, 5.85, 1.75, 0.35, "Sources", 13, True, RGBColor.from_string("4C6B50"), PP_ALIGN.CENTER)
box(s, 2.55, 3.25, 1.45, 1.0, "1. Ingestion\nELT, journal", C_LIGHT, C_TEXT, 14)
box(s, 4.35, 3.25, 1.6, 1.0, "2. Préparation\nquarantaine", C_LIGHT, C_TEXT, 14)
box(s, 6.4, 2.0, 1.9, 0.95, "3. MDM client\nidentifiant unique", C_GREEN, C_WHITE, 14, True)
box(s, 6.4, 4.55, 1.9, 0.95, "4. Data Warehouse\nfaits, dimensions", C_GREEN, C_WHITE, 14, True)
box(s, 8.75, 3.25, 1.6, 1.0, "5. Couche métier\nKPI certifiés", C_LIGHT, C_TEXT, 14)
box(s, 10.85, 1.4, 2.1, 0.75, "Tableaux de bord", C_LIGHT, C_TEXT, 14)
box(s, 10.85, 2.35, 2.1, 0.75, "Marketing sous RGPD", C_LIGHT, C_TEXT, 14)
box(s, 10.85, 3.3, 2.1, 0.75, "API sécurisée", C_GREEN, C_WHITE, 14, True)
box(s, 10.85, 4.25, 2.1, 0.75, "Assistant IA (pilote)", C_LIGHT, C_TEXT, 14)
box(s, 8.75, 5.35, 1.6, 0.75, "ERP : stock\ntemps réel", C_GREY, C_TEXT, 13, line=RGBColor.from_string("8A9A8C"))
arrow(s, 4.0, 3.75, 4.35, 3.75)
arrow(s, 5.95, 3.55, 6.4, 2.5)
arrow(s, 5.95, 3.95, 6.4, 5.0)
arrow(s, 7.35, 2.95, 7.35, 4.55)
text(s, 7.4, 3.5, 1.3, 0.4, "identifiant", 12, False, RGBColor.from_string("4C6B50"))
arrow(s, 8.3, 5.0, 8.75, 4.1)
arrow(s, 10.35, 3.4, 10.85, 1.8)
arrow(s, 10.35, 3.6, 10.85, 2.7)
arrow(s, 10.35, 3.85, 10.85, 3.65)
arrow(s, 11.9, 4.05, 11.9, 4.25)
arrow(s, 10.35, 5.7, 11.2, 5.0, dashed=True)
text(s, 0.35, 6.4, 12.6, 0.6, "Trait plein : flux vers l'aval. Pointillé : lecture seule en temps réel. "
     "Aucune donnée ne remonte du Warehouse vers les sources. Le Warehouse porte l'identifiant client, pas l'identité directe.",
     14, False, C_TEXT)

# ---------------- Diapositive 7
s = base(7, "MDM, Warehouse et indicateurs", "Personne 2", None)
card(s, 0.5, 1.35, 4.0, 2.5, "MDM client", ["Identifiant unique", "Règles certaines puis score", "Revue humaine des cas douteux", "Fusion réversible, journalisée"], 19, 14)
card(s, 4.65, 1.35, 4.0, 2.5, "Data Warehouse", ["Modèle en étoile", "Clients, produits, magasins, dates", "Ventes et mouvements de stock", "Identifiant sans identité directe"], 19, 14)
card(s, 8.8, 1.35, 4.0, 2.5, "KPI certifiés", ["Un seul calcul du CA", "Définition validée par la DAF", "Version et date affichées", "Écart caisses / Warehouse suivi"], 19, 14)
text(s, 0.5, 4.1, 12.3, 0.4, "De quel ticket vient ce chiffre ? Le lineage répond, étape par étape :", 17, True, C_DARK)
steps = ["Ticket de caisse", "Extraction (lot n°)", "Validation", "Transformation", "Table de faits", "Calcul du CA (règle v1.0)", "Tableau de bord"]
bw, gap, x0 = 1.58, 0.3, 0.35
for i, lab in enumerate(steps):
    x = x0 + i * (bw + gap)
    key = i >= 5
    box(s, x, 4.75, bw, 1.0, lab, C_GREEN if key else C_LIGHT, C_WHITE if key else C_TEXT, 13, key)
    if i < len(steps) - 1:
        arrow(s, x + bw, 5.25, x + bw + gap, 5.25)
box(s, x0 + 2 * (bw + gap), 6.15, bw, 0.7, "Quarantaine", C_WHITE, C_TEXT, 13)
arrow(s, x0 + 2 * (bw + gap) + bw / 2, 5.75, x0 + 2 * (bw + gap) + bw / 2, 6.15)

# ---------------- Diapositive 8
s = base(8, "Trajectoire de déploiement sur 12 mois", "Personne 2", None)
X0, MW = 3.0, 0.8
for m in range(12):
    rect(s, X0 + m * MW, 1.35, MW - 0.04, 0.4, C_GREEN)
    text(s, X0 + m * MW, 1.35, MW - 0.04, 0.4, f"M{m + 1}", 13, True, C_WHITE, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
phases = [("Phase 1 · cadrage", 0, 2, "Cadrage, rôles", "J1"),
          ("Phase 2 · socle data", 2, 6, "Ingestion, MDM, Warehouse, KPI", "J2"),
          ("Phase 3 · sécurisation et IA", 6, 9, "Accès, RGPD, API", "J3"),
          ("Phase 4 · pilote et bilan", 9, 12, "Pilote, bilan", "J4")]
for i, (lab, a, b, what, j) in enumerate(phases):
    y = 1.95 + i * 0.85
    rect(s, 0.5, y - 0.05, 12.35, 0.7, C_GREY if i % 2 == 0 else C_WHITE)
    text(s, 0.5, y, 2.45, 0.6, lab, 14, True, C_DARK, anchor=MSO_ANCHOR.MIDDLE)
    r = rect(s, X0 + a * MW, y + 0.03, (b - a) * MW - 0.04, 0.54, C_LIGHT, C_DARK, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, X0 + a * MW, y + 0.03, (b - a) * MW - 0.04, 0.54, what, 12, False, C_TEXT, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
    d = rect(s, X0 + b * MW - 0.28, y + 0.14, 0.32, 0.32, C_DARK, shape=MSO_SHAPE.DIAMOND)
    text(s, X0 + b * MW - 0.32, y + 0.45, 0.4, 0.25, j, 10, True, C_DARK, PP_ALIGN.CENTER)
text(s, 0.5, 5.3, 12.3, 0.3, "Mois de démarrage fictif, à ajuster. Le pilote n'ouvre que si J3 est franchi.", 12, False, RGBColor.from_string("4C6B50"))
ms = [("M2 · J1", "cadrage validé"), ("M6 · J2", "premiers KPI certifiés"), ("M9 · J3", "pilote autorisé"), ("M12 · J4", "bilan et décision")]
for i, (h, b) in enumerate(ms):
    x = 0.6 + i * 3.1
    rect(s, x, 5.65, 2.9, 1.2, C_LIGHT, RGBColor.from_string("A9B8AB"))
    text(s, x, 5.7, 2.9, 0.5, h, 18, True, C_DARK, PP_ALIGN.CENTER)
    text(s, x, 6.2, 2.9, 0.6, b, 15, False, C_TEXT, PP_ALIGN.CENTER)

# ---------------- Diapositive 9
s = base(9, "Gouvernance et matrice RACI", "Personne 3", None)
picture(s, ROOT / "presentation" / "assets" / "slide-09-gouvernance.png", 0.3, 1.3, 6.7, 5.7)
rows = [["Activité", "A (décide)"],
        ["Définition des KPI", "Data Owner"],
        ["Fusion de fiches clients", "Data Steward"],
        ["Règles de conservation", "Comité"],
        ["Gestion des incidents", "DSI et RSSI"],
        ["Choix du prestataire", "Sponsor"],
        ["Validation du déploiement", "Sponsor"]]
table(s, 7.2, 1.45, 5.6, rows, [3.2, 2.4], 15, 0.5)
text(s, 7.2, 5.15, 5.6, 1.8, ["11 activités, un seul A par ligne.",
                               "Responsable de traitement : Verdalia. Owner : décide. Steward : applique. DPO : conseille."],
     15, False, C_TEXT, bullets=True)

# ---------------- Diapositive 10
s = base(10, "RGPD et sécurité", "Personne 3", "Une base légale par finalité : le consentement n'est pas requis pour tout")
rows = [["Finalité", "Base légale proposée"],
        ["Ventes et commandes", "contrat"],
        ["Comptabilité", "obligation légale"],
        ["Fidélité", "contrat d'adhésion"],
        ["Prospection prospects", "consentement"],
        ["Prospection clients", "régime spécifique, à valider (DPO)"]]
table(s, 0.6, 1.9, 6.4, rows, [3.0, 3.4], 14, 0.55)
text(s, 7.4, 1.85, 5.4, 0.45, "Durées de conservation : trois statuts", 19, True, C_DARK)
st = [("Obligation légale", "10 ans, pièces comptables"), ("Recommandation CNIL", "3 ans, clients et prospects"),
      ("Proposition interne", "zone brute 90 jours")]
for i, (h, b) in enumerate(st):
    card(s, 7.4, 2.4 + i * 1.12, 5.4, 1.02, h, b, 16, 14, dy=0.5)
text(s, 0.6, 5.45, 6.4, 1.5, ["Droits des personnes traités sur un identifiant unique.",
                               "Registre, AIPD recommandée, contrats article 28.",
                               "Accès par rôle, chiffrement, journalisation."], 15, False, C_TEXT, bullets=True)

# ---------------- Diapositive 11
s = base(11, "Assistant IA responsable", "Personne 3", None)
chain = [("Conseiller authentifié", "SSO et authentification forte", False),
         ("API sécurisée", "droits selon rôle et magasin, filtre anti-injection", True),
         ("Données lues", "fiches produits validées, stock de l'ERP en lecture seule", False),
         ("Modèle IA", "requête minimale, sans identité client", True),
         ("Réponse filtrée", "sources citées, mention « généré par IA »", False),
         ("Vérification humaine", "le conseiller décide ; journal proportionné", False)]
for i, (h, b, key) in enumerate(chain):
    y = 1.35 + i * 0.93
    rect(s, 0.5, y, 8.0, 0.72, C_GREEN if key else C_LIGHT, C_DARK, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, 0.65, y, 2.5, 0.72, h, 16, True, C_WHITE if key else C_DARK, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 3.1, y, 5.3, 0.72, b, 14, False, C_WHITE if key else C_TEXT, anchor=MSO_ANCHOR.MIDDLE)
    if i < len(chain) - 1:
        arrow(s, 4.5, y + 0.72, 4.5, y + 0.93)
text(s, 8.9, 1.4, 4.2, 5.6, ["Jamais d'accès direct aux données.",
                              "Authentification et droits par rôle.",
                              "Requête sans identité client.",
                              "Historique client affiché au conseiller, pas envoyé au modèle.",
                              "Le conseiller vérifie chaque suggestion.",
                              "Contrat : non-réutilisation, réversibilité.",
                              "AI Act : analyse préliminaire, sans conclusion."], 17, False, C_TEXT, bullets=True, spacing=10)

# ---------------- Diapositive 12
s = base(12, "Risques et mesures", "Personne 3", "17 risques suivis dans le dossier ; les quatre principaux :")
rows = [["Risque", "Mesure de réduction", "Responsable"],
        ["Faux rapprochements de clients", "revue humaine, fusion réversible, journal", "Data Steward Client"],
        ["Désaccord sur les KPI", "glossaire validé par la direction financière", "Data Owner Finance"],
        ["Métiers peu impliqués", "sponsor actif, rôles nommés dès la phase 1", "Sponsor"],
        ["Retard de calendrier", "conditions de passage de phase, périmètre progressif", "Comité"]]
table(s, 0.6, 2.0, 12.1, rows, [3.6, 5.6, 2.9], 16, 0.8)

# ---------------- Diapositive 13
s = base(13, "Conclusion et bénéfices attendus", "Personne 3", None)
ben = [("Chiffres cohérents", "un seul calcul du CA, validé par la direction financière"),
       ("Vision client unique", "identifiant commun, corrections traçables"),
       ("Conformité et IA encadrées", "finalités, durées qualifiées, API, vérification humaine")]
for i, (h, b) in enumerate(ben):
    card(s, 0.6 + i * 4.1, 1.55, 3.85, 2.4, h, b, 20, 16)
rect(s, 0.6, 4.35, 12.1, 2.3, C_GREY, RGBColor.from_string("A9B8AB"))
text(s, 0.85, 4.45, 11.6, 0.5, "Limites assumées", 19, True, C_DARK)
text(s, 0.85, 4.95, 11.6, 1.7, ["Dépend de l'implication des métiers.",
                                 "Seuils, charges et notes : hypothèses à calibrer sur les données réelles.",
                                 "Points juridiques à faire valider par le DPO."], 16, False, C_TEXT, bullets=True)

# ---------------- Annexe
s = base("Annexe", "Traçabilité des exigences EX-01 à EX-10", None)
rows = [["ID", "Solution retenue", "Responsable", "Critère de vérification"],
        ["EX-01", "MDM, identifiant unique", "Data Owner Client", "doublons résiduels < 1 % (hypothèse)"],
        ["EX-02", "glossaire, KPI certifiés", "Data Owner Finance", "KPI publiés uniquement certifiés"],
        ["EX-03", "Owners et Stewards", "Sponsor, comité", "100 % des jeux avec Owner"],
        ["EX-04", "registre, bases légales, AIPD", "DPO", "registre complet, droits dans le délai"],
        ["EX-05", "lineage de bout en bout", "Resp. plateforme data", "démonstration complète d'un KPI"],
        ["EX-06", "accès par rôle", "DSI et RSSI", "revue trimestrielle signée"],
        ["EX-07", "indicateurs, quarantaine", "Data Stewards", "indicateurs mensuels dans les seuils"],
        ["EX-08", "API intermédiaire", "DPO, plateforme data", "aucune identité envoyée au modèle"],
        ["EX-09", "grille et contrat", "Sponsor, DSI", "contrat signé, test de remplacement"],
        ["EX-10", "4 phases, 4 jalons", "Comité", "J2 (mois 6) et J4 (mois 12) franchis"]]
table(s, 0.5, 1.3, 12.3, rows, [0.9, 3.5, 3.1, 4.8], 13, 0.5)

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(OUT))
print("Ecrit :", OUT.relative_to(ROOT), f"({OUT.stat().st_size // 1024} Ko), {len(prs.slides)} diapositives")
