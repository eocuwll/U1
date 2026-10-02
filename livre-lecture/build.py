# -*- coding: utf-8 -*-
"""Génère le livre « Je lis, j'écris ! » (PDF A4, à imprimer)."""
import os, re
import uharfbuzz as hb
from fontTools.ttLib import TTFont as FTFont
from fontTools.pens.basePen import BasePen
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from contenu import (JOURS, TEST_SYLLABES, TEST_MOTS, TEST_OUTILS, TEST_TEXTE_TITRE,
                     TEST_TEXTE, TEST_QCM, TEST_DICTEE_MOTS, TEST_DICTEE_PHRASES, TEST_COPIE)

ICI = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ICI, "fonts")
SORTIE = os.path.join(ICI, "Je-lis-j-ecris-21-jours-CE1.pdf")

pdfmetrics.registerFont(TTFont("R", os.path.join(FONTS, "Andika-Regular.ttf")))
pdfmetrics.registerFont(TTFont("B", os.path.join(FONTS, "Andika-Bold.ttf")))

# ── Palette volontairement réduite : noir, gris, un seul bleu ardoise ──
INK = HexColor("#1d1d1d")
ACC = HexColor("#2f5d8a")
SYL = HexColor("#8a8a8a")      # 2e couleur des syllabes alternées
MUTE = HexColor("#6b6b6b")
LINE = HexColor("#c9c9c9")
TRACE = HexColor("#c4c4c4")    # lettres à repasser
SEY_F = HexColor("#d3dde8")    # lignes fines Seyès
SEY_B = HexColor("#8fa9c4")    # lignes de base Seyès
PALE = HexColor("#f3f5f8")     # fond très léger des encadrés

PW, PH = 210 * mm, 297 * mm
ML = 18 * mm
W = PW - 2 * ML
INTER = 3.3 * mm                 # interligne Seyès agrandi (CE1)

# ───────────────────────── écriture cursive liée (Playwrite France Moderne) ─────────────────────────
_CP = os.path.join(FONTS, "PlaywriteFRModerne.ttf")
_ft = FTFont(_CP); _gs = _ft.getGlyphSet(); _order = _ft.getGlyphOrder()
_hbfont = hb.Font(hb.Face(hb.Blob.from_file_path(_CP)))


class _Pen(BasePen):
    def __init__(self, gs, p):
        super().__init__(gs); self.p = p
    def _moveTo(self, a): self.p.moveTo(*a)
    def _lineTo(self, a): self.p.lineTo(*a)
    def _curveToOne(self, a, b, d): self.p.curveTo(*a, *b, *d)
    def _closePath(self): self.p.close()


def _shape(text):
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(_hbfont, buf, {})
    return buf.glyph_infos, buf.glyph_positions


def cursive_width(text, size):
    _, pos = _shape(text)
    return sum(p.x_advance for p in pos) * size / 1000


def cursive(c, text, x, y, size, color=INK):
    infos, pos = _shape(text)
    s = size / 1000; cx = 0
    c.saveState(); c.setFillColor(color)
    for i, p in zip(infos, pos):
        path = c.beginPath(); _gs[_order[i.codepoint]].draw(_Pen(_gs, path))
        c.saveState(); c.translate(x + (cx + p.x_offset) * s, y + p.y_offset * s); c.scale(s, s)
        c.drawPath(path, stroke=0, fill=1, fillMode=1); c.restoreState()
        cx += p.x_advance
    c.restoreState()
    return cx * s


CUR = INTER / mm * mm / 0.5    # taille de police : hauteur des minuscules = 1 interligne

# ───────────────────────── texte enrichi ─────────────────────────
NB = " "


def prep(t):
    t = t.replace("« ", "«" + NB).replace(" »", NB + "»")
    for p in "!?:;":
        t = t.replace(" " + p, NB + p)
    return t


def runs_of(s):
    """'b{ou}le' -> [('b',0),('ou',1),('le',0)]"""
    out, bold, buf = [], 0, ""
    for ch in s:
        if ch in "{}":
            if buf: out.append((buf, bold))
            buf = ""; bold = 1 if ch == "{" else 0
        else:
            buf += ch
    if buf: out.append((buf, bold))
    return out


def rw(runs, size):
    return sum(pdfmetrics.stringWidth(t.replace(NB, " "), "B" if b else "R", size) for t, b in runs)


def draw_runs(c, x, y, runs, size, color=INK, bcolor=ACC):
    for t, b in runs:
        t = t.replace(NB, " ")
        c.setFont("B" if b else "R", size); c.setFillColor(bcolor if b else color)
        c.drawString(x, y, t); x += pdfmetrics.stringWidth(t, "B" if b else "R", size)
    return x


def wrap(text, width, size):
    """Renvoie une liste de lignes ; chaque ligne = liste de mots (listes de runs). None = saut de paragraphe."""
    lines = []
    for para in prep(text).split("\n"):
        cur, cw = [], 0
        sp = pdfmetrics.stringWidth(" ", "R", size)
        for word in para.split(" "):
            if not word: continue
            r = runs_of(word); w = rw(r, size)
            if cur and cw + sp + w > width:
                lines.append(cur); cur, cw = [], 0
            cw = w if not cur else cw + sp + w
            cur.append(r)
        if cur: lines.append(cur)
        lines.append(None)
    while lines and lines[-1] is None: lines.pop()
    return lines


def count_words(line):
    return sum(1 for wd in line if re.search(r"[A-Za-zÀ-ÿœŒ0-9]", "".join(t for t, _ in wd)))


def draw_para(c, x, y, text, width, size, lead=1.6, color=INK, bcolor=ACC, counts=False):
    sp = pdfmetrics.stringWidth(" ", "R", size)
    total = 0
    for ln in wrap(text, width, size):
        if ln is None:
            y -= size * 0.45; continue
        xx = x
        for wd in ln:
            xx = draw_runs(c, xx, y, wd, size, color, bcolor) + sp
        if counts:
            total += count_words(ln)
            c.setFont("R", 8); c.setFillColor(SYL)
            c.drawRightString(x + width + 10 * mm, y + 1, str(total))
        y -= size * lead
    return y


def para_height(text, width, size, lead=1.6):
    h = 0
    for ln in wrap(text, width, size):
        h += size * 0.45 if ln is None else size * lead
    return h


def syl_word(c, x, y, word, size, measure=False):
    """Mot syllabé : syllabes en couleurs alternées, graphème étudié en gras."""
    xx = x
    for k, syl in enumerate(word.split("-")):
        col = INK if k % 2 == 0 else SYL
        for t, b in runs_of(syl):
            f = "B" if b else "R"
            if not measure:
                c.setFont(f, size); c.setFillColor(col); c.drawString(xx, y, t)
            xx += pdfmetrics.stringWidth(t, f, size)
    return xx - x


# ───────────────────────── éléments graphiques ─────────────────────────
def seyes(c, x, ytop, width, rows, inter=INTER, margin=True):
    """Lignage Seyès. Renvoie la liste des lignes d'écriture (y) et le y du bas."""
    n = 4 * rows + 1
    bases = []
    for k in range(n + 1):
        y = ytop - k * inter
        if k % 4 == 3:
            c.setStrokeColor(SEY_B); c.setLineWidth(0.7); bases.append(y)
        else:
            c.setStrokeColor(SEY_F); c.setLineWidth(0.35)
        c.line(x, y, x + width, y)
    if margin:
        c.setStrokeColor(SEY_B); c.setLineWidth(0.5)
        c.line(x + 10 * mm, ytop, x + 10 * mm, ytop - n * inter)
    return bases, ytop - n * inter


def checkbox(c, x, y, s=3.6 * mm):
    c.setStrokeColor(MUTE); c.setLineWidth(0.7); c.roundRect(x, y, s, s, 0.6 * mm, stroke=1, fill=0)


def star(c, cx, cy, r, fill=False):
    import math
    p = c.beginPath()
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        (p.moveTo if i == 0 else p.lineTo)(cx + rr * math.cos(a), cy + rr * math.sin(a))
    p.close()
    c.setStrokeColor(ACC); c.setLineWidth(0.9); c.setFillColor(ACC)
    c.drawPath(p, stroke=1, fill=1 if fill else 0)


def cat(c, cx, cy, s=1.0, color=INK, lw=1.4):
    """Petit chat assis en dessin au trait (Moka)."""
    c.saveState(); c.translate(cx, cy); c.scale(s, s)
    c.setStrokeColor(color); c.setLineWidth(lw / s); c.setLineCap(1); c.setLineJoin(1)
    p = c.beginPath()                                   # corps
    p.moveTo(-14, 0); p.curveTo(-20, 18, -16, 34, -8, 40)
    p.moveTo(14, 0); p.curveTo(20, 18, 16, 34, 8, 40)
    p.moveTo(-14, 0); p.curveTo(-6, -3, 6, -3, 14, 0)
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()                                   # pattes avant
    p.moveTo(-5, -1); p.lineTo(-5, 12); p.moveTo(5, -1); p.lineTo(5, 12)
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()                                   # queue
    p.moveTo(14, 2); p.curveTo(30, 2, 34, 14, 26, 24)
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()                                   # tête + oreilles
    p.moveTo(-13, 50); p.curveTo(-15, 40, -9, 34, 0, 34)
    p.curveTo(9, 34, 15, 40, 13, 50)
    p.lineTo(14, 62); p.lineTo(6, 55); p.curveTo(2, 56, -2, 56, -6, 55)
    p.lineTo(-14, 62); p.close()
    c.setFillColor(HexColor("#ffffff")); c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(color)
    c.circle(-5, 46, 1.4, stroke=0, fill=1); c.circle(5, 46, 1.4, stroke=0, fill=1)
    p = c.beginPath()                                   # nez, bouche, moustaches
    p.moveTo(-1.2, 42.5); p.lineTo(1.2, 42.5); p.lineTo(0, 41.2); p.close()
    c.drawPath(p, stroke=1, fill=1)
    p = c.beginPath()
    p.moveTo(0, 41.2); p.curveTo(0, 39.5, -2.5, 39, -3, 40)
    p.moveTo(0, 41.2); p.curveTo(0, 39.5, 2.5, 39, 3, 40)
    for sgn in (-1, 1):
        p.moveTo(sgn * 4, 42); p.lineTo(sgn * 15, 44)
        p.moveTo(sgn * 4, 41); p.lineTo(sgn * 15, 40)
    c.setLineWidth(0.7 / s); c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def book_icon(c, cx, cy, s=1.0):
    c.saveState(); c.translate(cx, cy); c.scale(s, s)
    c.setStrokeColor(ACC); c.setLineWidth(1.0 / s); c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(0, -8); p.curveTo(-6, -5, -12, -5, -16, -7); p.lineTo(-16, 9)
    p.curveTo(-12, 11, -6, 11, 0, 8); p.curveTo(6, 11, 12, 11, 16, 9); p.lineTo(16, -7)
    p.curveTo(12, -5, 6, -5, 0, -8); p.lineTo(0, 8)
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


# ───────────────────────── page : en-tête / pied ─────────────────────────
class Livre:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PW, PH))
        self.c.setTitle("Je lis, j'écris ! — 21 jours pour reprendre la lecture (CE1)")
        self.c.setAuthor("Livret d'entraînement familial")
        self.page = 0
        self.pages_jour = {}

    def new(self, footer=True):
        if self.page:
            self.c.showPage()
        self.page += 1
        self._footer = footer

    def footer(self):
        c = self.c
        c.setFont("R", 8.5); c.setFillColor(SYL)
        c.drawCentredString(PW / 2, 9 * mm, str(self.page))

    def end_page(self):
        if self._footer:
            self.footer()


def header(L, jour, etape, titre):
    c = L.c
    top = PH - 13 * mm
    sem = (jour - 1) // 7 + 1
    c.setFont("B", 10.5); c.setFillColor(ACC); c.drawString(ML, top, f"JOUR {jour}")
    w = pdfmetrics.stringWidth(f"JOUR {jour}", "B", 10.5)
    c.setFont("R", 10.5); c.setFillColor(MUTE); c.drawString(ML + w, top, f"  ·  Semaine {sem}")
    # frise de progression : 21 points
    x0 = PW - ML - 20 * 4 * mm
    for i in range(21):
        cx = x0 + i * 4 * mm
        c.setStrokeColor(ACC if i < jour else LINE); c.setLineWidth(0.7)
        c.setFillColor(ACC)
        c.circle(cx, top + 1.2 * mm, 1.25 * mm, stroke=1, fill=1 if i < jour else 0)
    # titre d'étape
    y = PH - 27 * mm
    c.setStrokeColor(ACC); c.setLineWidth(1.1); c.setFillColor(ACC)
    c.circle(ML + 4.2 * mm, y + 2.2 * mm, 4.2 * mm, stroke=0, fill=1)
    c.setFillColor(HexColor("#ffffff")); c.setFont("B", 14)
    c.drawCentredString(ML + 4.2 * mm, y + 0.6 * mm, str(etape))
    noms = {1: "Je découvre", 2: "Je lis", 3: "J'écris"}
    c.setFont("B", 19); c.setFillColor(INK); c.drawString(ML + 11 * mm, y, noms[etape])
    w = pdfmetrics.stringWidth(noms[etape], "B", 19)
    c.setFont("R", 13); c.setFillColor(MUTE); c.drawString(ML + 11 * mm + w, y + 0.3 * mm, "   —  " + titre)
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(ML, y - 4.5 * mm, PW - ML, y - 4.5 * mm)
    return y - 12 * mm


def section(c, y, text, note=None):
    c.setFillColor(ACC); c.rect(ML, y - 0.2 * mm, 1.6 * mm, 4.4 * mm, stroke=0, fill=1)
    c.setFont("B", 13); c.setFillColor(INK); c.drawString(ML + 4 * mm, y, text)
    if note:
        w = pdfmetrics.stringWidth(text, "B", 13)
        c.setFont("R", 10); c.setFillColor(MUTE); c.drawString(ML + 4 * mm + w + 3 * mm, y + 0.2 * mm, note)
    return y - 8 * mm


def rbox(c, x, y, w, h, fill=None, stroke=LINE, r=2.5 * mm, lw=0.8):
    c.setStrokeColor(stroke); c.setLineWidth(lw)
    if fill is not None:
        c.setFillColor(fill)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1 if fill is not None else 0)


# ───────────────────────── page 1 du jour : je découvre ─────────────────────────
def page_decouvrir(L, d):
    c = L.c
    y = header(L, d["n"], 1, d["titre"])
    # carte du son
    left_w = 66 * mm
    rx = ML + left_w + 6 * mm; rwid = W - left_w - 12 * mm
    regle_h = para_height(d["regle"], rwid, 11.5, 1.45)
    h = max(34 * mm, 15 * mm + regle_h + 4 * mm)
    rbox(c, ML, y - h, W, h, fill=PALE, stroke=SEY_B)
    son = d["son"]; size = 40
    while pdfmetrics.stringWidth(son, "B", size) > left_w - 8 * mm and size > 14:
        size -= 1
    c.setFont("B", size); c.setFillColor(ACC)
    c.drawCentredString(ML + left_w / 2, y - h / 2 - size * 0.33, son)
    c.setStrokeColor(SEY_B); c.setLineWidth(0.6); c.line(ML + left_w, y - h + 5 * mm, ML + left_w, y - 5 * mm)
    rs = 14
    while pdfmetrics.stringWidth(d["ref"], "B", rs) > rwid and rs > 10:
        rs -= 0.5
    c.setFont("B", rs); c.setFillColor(INK); c.drawString(rx, y - 9 * mm, d["ref"])
    draw_para(c, rx, y - 16 * mm, d["regle"], rwid, 11.5, 1.45, color=MUTE)
    y -= h + 9 * mm

    if "syllabes" in d:
        items = d["syllabes"]; n = len(items)
        cols = 6 if n % 6 == 0 else 5 if n % 5 == 0 else 8 if n % 8 == 0 else 6
        y = section(c, y, "Je lis les syllabes", "de gauche à droite, à voix haute")
        gap = 2.5 * mm; bw = (W - (cols - 1) * gap) / cols; bh = 12.5 * mm
        for i, s in enumerate(items):
            r, k = divmod(i, cols)
            bx = ML + k * (bw + gap); by = y - (r + 1) * bh - r * gap + 3 * mm
            rbox(c, bx, by, bw, bh, r=2 * mm)
            c.setFont("R", 21); c.setFillColor(INK); c.drawCentredString(bx + bw / 2, by + bh / 2 - 7, s)
        rows = (n + cols - 1) // cols
        y -= rows * bh + (rows - 1) * gap + 7 * mm

    if "mots" in d:
        y = section(c, y, "Je lis les mots", "je coche chaque mot bien lu")
        colw = W / 3
        for i, m in enumerate(d["mots"]):
            r, k = divmod(i, 3)
            x = ML + k * colw + 2 * mm; yy = y - r * 11.5 * mm - 4 * mm
            checkbox(c, x, yy + 0.5 * mm)
            syl_word(c, x + 7 * mm, yy, m, 20)
        y -= 4 * 11.5 * mm + 4 * mm
        c.setFont("R", 9.5); c.setFillColor(MUTE)
        c.drawString(ML, y + 2 * mm, "Les syllabes sont en noir et en gris pour m'aider à découper le mot.")
        y -= 6 * mm

    if "paires" in d:
        y = section(c, y, "Je lis : un seul … plusieurs", "le s est en bleu : on ne l'entend pas")
        colw = W / 2
        c.setFont("B", 11); c.setFillColor(MUTE)
        c.drawString(ML + 6 * mm, y, "UN SEUL (singulier)"); c.drawString(ML + colw + 6 * mm, y, "PLUSIEURS (pluriel)")
        y -= 9 * mm
        for a, b in d["paires"]:
            c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(ML, y - 3 * mm, PW - ML, y - 3 * mm)
            draw_runs(c, ML + 6 * mm, y, runs_of(a), 19)
            c.setFont("R", 16); c.setFillColor(SYL); c.drawCentredString(ML + colw - 4 * mm, y, "→")
            draw_runs(c, ML + colw + 6 * mm, y, runs_of(b), 19)
            y -= 11 * mm
        y -= 4 * mm

    if "conjugaison" in d:
        y = section(c, y, "Je lis les verbes", "je lis chaque ligne, puis je la récite sans regarder")
        colw = W / 2
        rbox(c, ML, y - 6 * 12 * mm - 12 * mm, colw - 3 * mm, 6 * 12 * mm + 14 * mm, stroke=SEY_B)
        rbox(c, ML + colw + 3 * mm, y - 6 * 12 * mm - 12 * mm, colw - 3 * mm, 6 * 12 * mm + 14 * mm, stroke=SEY_B)
        c.setFont("B", 16); c.setFillColor(ACC)
        c.drawCentredString(ML + colw / 2, y - 4 * mm, "ÊTRE"); c.drawCentredString(ML + colw * 1.5, y - 4 * mm, "AVOIR")
        yy = y - 15 * mm
        for a, b in d["conjugaison"]:
            c.setFont("R", 19); c.setFillColor(INK)
            c.drawString(ML + 10 * mm, yy, a); c.drawString(ML + colw + 13 * mm, yy, b)
            yy -= 12 * mm
        y = yy - 6 * mm

    if "ponctuation" in d:
        y = section(c, y, "Je lis la même phrase avec 3 voix", "calme · qui pose une question · surprise")
        colw = W / 3
        for i, s in enumerate(d["ponctuation"]):
            r, k = divmod(i, 3)
            bx = ML + k * colw; by = y - (r + 1) * 15 * mm + 4 * mm
            rbox(c, bx + 1.5 * mm, by, colw - 3 * mm, 12.5 * mm, r=2 * mm)
            body, p = s[:-1], s[-1]
            c.setFont("R", 20); c.setFillColor(INK)
            tw = pdfmetrics.stringWidth(body, "R", 20) + pdfmetrics.stringWidth(" " + p, "B", 22)
            x0 = bx + colw / 2 - tw / 2
            c.drawString(x0, by + 4 * mm, body)
            c.setFont("B", 22); c.setFillColor(ACC)
            c.drawString(x0 + pdfmetrics.stringWidth(body, "R", 20), by + 4 * mm, " " + p)
        y -= 3 * 15 * mm + 6 * mm

    if "groupes" in d:
        y = section(c, y, "Je lis par groupes de mots", "je fais une petite pause à chaque  /")
        for s in d["groupes"]:
            parts = s.split(" / "); x = ML + 3 * mm
            for k, part in enumerate(parts):
                c.setFont("R", 17); c.setFillColor(INK); c.drawString(x, y, part)
                x += pdfmetrics.stringWidth(part, "R", 17)
                if k < len(parts) - 1:
                    c.setFont("B", 17); c.setFillColor(SYL); c.drawString(x, y, "  /  ")
                    x += pdfmetrics.stringWidth("  /  ", "B", 17)
            y -= 12 * mm
        y -= 3 * mm

    if "syllabes" not in d and "mots" not in d and "paires" not in d:
        pass

    # mots-outils
    y = section(c, y, "Mes mots-outils du jour", "je les lis · je les épelle · je les cache · je les écris")
    bw = (W - 2 * 5 * mm) / 3
    for k, m in enumerate(d["outils"]):
        bx = ML + k * (bw + 5 * mm)
        rbox(c, bx, y - 13 * mm, bw, 15 * mm, stroke=ACC, lw=1.0)
        c.setFont("B", 22); c.setFillColor(INK); c.drawCentredString(bx + bw / 2, y - 7.5 * mm, m)
    y -= 19 * mm
    seyes(c, ML, y, W, 1)
    L.end_page()


# ───────────────────────── page 2 du jour : je lis ─────────────────────────
def taille_texte(n):
    return 20 if n <= 3 else 18 if n <= 7 else 16 if n <= 14 else 14.5


def page_lire(L, d):
    c = L.c
    y = header(L, d["n"], 2, d["titre"])
    book_icon(c, ML + 8 * mm, y - 2 * mm, 0.85)
    c.setFont("B", 18); c.setFillColor(ACC)
    c.drawString(ML + 17 * mm, y - 4 * mm, f"Épisode {d['n']} : {d['histoire_titre']}")
    y -= 15 * mm
    size = taille_texte(d["n"])
    chrono = d.get("chrono")
    width = W - (14 * mm if chrono else 4 * mm)
    lead = 1.7 if size >= 18 else 1.6
    y = draw_para(c, ML + 2 * mm, y, d["histoire"], width, size, lead, counts=chrono)
    y -= 2 * mm
    if chrono:
        c.setFont("R", 8.5); c.setFillColor(SYL)
        c.drawRightString(PW - ML, y + 1 * mm, "nombre de mots")
    y -= 5 * mm
    # relectures
    rbox(c, ML, y - 13 * mm, W, 15 * mm, fill=PALE, stroke=SEY_B)
    c.setFont("B", 12); c.setFillColor(INK); c.drawString(ML + 5 * mm, y - 7 * mm, "Je lis l'histoire 3 fois :")
    x = ML + 55 * mm
    for k, lab in enumerate(["1re fois", "2e fois", "3e fois"]):
        checkbox(c, x, y - 7.6 * mm, 4.2 * mm)
        c.setFont("R", 12); c.setFillColor(INK); c.drawString(x + 6 * mm, y - 7 * mm, lab)
        x += 26 * mm
    if chrono:
        c.setFont("R", 11); c.setFillColor(MUTE)
        c.drawString(x - 2 * mm, y - 7 * mm, "En 1 min : _____ mots")
    y -= 23 * mm
    # compréhension
    y = section(c, y, "Je comprends", "je réponds par une phrase, à l'oral ou à l'écrit")
    qgap = (9 * mm, 7 * mm) if len(d["questions"]) > 3 else (10 * mm, 8 * mm)
    for k, q in enumerate(d["questions"], 1):
        c.setFont("B", 13); c.setFillColor(ACC); c.drawString(ML + 2 * mm, y, f"{k}.")
        c.setFont("R", 13); c.setFillColor(INK); c.drawString(ML + 9 * mm, y, q.replace(NB, " "))
        y -= qgap[0]
        c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(ML + 9 * mm, y, PW - ML, y)
        y -= qgap[1]
    # dessin si place
    bas = 16 * mm
    if y - bas > 38 * mm:
        y = section(c, y + 2 * mm, "Je dessine ce que j'ai lu")
        rbox(c, ML, bas, W, y - bas + 3 * mm, stroke=LINE)
    L.end_page()


# ───────────────────────── page 3 du jour : j'écris ─────────────────────────
def blank_word(c, x, y, s, size=20):
    """Affiche un mot à compléter ; '_' = case vide."""
    parts = s.split("_")
    for k, p in enumerate(parts):
        c.setFont("R", size); c.setFillColor(INK); c.drawString(x, y, p)
        x += pdfmetrics.stringWidth(p, "R", size)
        if k < len(parts) - 1:
            c.setStrokeColor(ACC); c.setLineWidth(0.9)
            c.line(x + 1 * mm, y - 1.2 * mm, x + 13 * mm, y - 1.2 * mm); x += 14 * mm
    return x


def page_ecrire(L, d):
    c = L.c
    y = header(L, d["n"], 3, d["titre"])
    # repasser + écrire
    y = section(c, y, "Je repasse et j'écris", "le modèle en noir, je repasse le gris, puis j'écris seule")
    mots_ecr = d["ecrire"][:2] if (d.get("lettre") or d.get("ordre")) else d["ecrire"]
    for mot in mots_ecr:
        bases, ybot = seyes(c, ML, y + 1 * mm, W, 2)
        x = ML + 12 * mm
        cursive(c, mot, x, bases[0], CUR, INK)
        wmot = cursive_width(mot, CUR); step = wmot + 9 * mm
        x += step
        for _ in range(3):
            if x + wmot > PW - ML - 2 * mm:
                break
            cursive(c, mot, x, bases[0], CUR, TRACE); x += step
        y = ybot - 3.5 * mm
    y -= 4 * mm
    # compléter / remettre en ordre / lettre
    if d.get("lettre"):
        y = section(c, y, "J'écris une petite lettre", "à quelqu'un que j'aime (2 ou 3 phrases)")
        c.setFont("R", 11); c.setFillColor(MUTE)
        c.drawString(ML + 2 * mm, y, "Aide : Cher… / Chère… — Je vais bien. — Aujourd'hui, j'ai… — Gros bisous.")
        y -= 4 * mm
        _, y = seyes(c, ML, y, W, 3)
        y -= 7 * mm
    elif d.get("ordre"):
        y = section(c, y, d["completer_titre"], "puis j'écris la phrase")
        for q, _a in d["completer"]:
            x = ML + 2 * mm
            for wd in q.split(" / "):
                tw = pdfmetrics.stringWidth(wd, "R", 17) + 6 * mm
                rbox(c, x, y - 3 * mm, tw, 10 * mm, r=1.8 * mm)
                c.setFont("R", 17); c.setFillColor(INK); c.drawString(x + 3 * mm, y, wd)
                x += tw + 3 * mm
            c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(x + 4 * mm, y - 2 * mm, PW - ML, y - 2 * mm)
            y -= 14 * mm
        y -= 2 * mm
    else:
        y = section(c, y, d["completer_titre"])
        items = d["completer"]
        long_items = any(len(q) > 12 for q, _ in items)
        if long_items:
            colw = W / 2
            for k, (q, _a) in enumerate(items):
                r, kk = divmod(k, 2)
                x = ML + kk * colw; yy = y - r * 11 * mm - 1 * mm
                c.setFont("B", 12); c.setFillColor(ACC); c.drawString(x + 2 * mm, yy, f"{k + 1}.")
                blank_word(c, x + 8 * mm, yy, q, 16)
            y -= ((len(items) + 1) // 2) * 11 * mm
        else:
            colw = W / 3
            for k, (q, _a) in enumerate(items):
                r, kk = divmod(k, 3)
                blank_word(c, ML + kk * colw + 4 * mm, y - r * 12 * mm - 1 * mm, q, 21)
            y -= ((len(items) + 2) // 3) * 12 * mm
        y -= 3 * mm
    # copie
    y = section(c, y, "Je copie la phrase", "en écriture attachée")
    bases, ybot = seyes(c, ML, y + 1 * mm, W, 2)
    cursive(c, d["copie"], ML + 12 * mm, bases[0], CUR, INK)
    y = ybot - 6 * mm
    # dictée
    y = section(c, y, "Ma dictée", "un adulte lit la dictée du jour (page « coin des parents »)")
    _, y = seyes(c, ML, y + 1 * mm, W, 2)
    # étoiles
    y -= 7 * mm
    labels = ["J'ai bien lu", "J'ai écrit avec soin", "Je connais mes mots-outils"]
    colw = W / 3
    for k, lab in enumerate(labels):
        cx = ML + k * colw + 6 * mm
        star(c, cx, y - 1 * mm, 3.6 * mm)
        c.setFont("R", 11); c.setFillColor(INK); c.drawString(cx + 6 * mm, y - 2.5 * mm, lab)
    if y < 18 * mm:
        print(f"  ! page écrire jour {d['n']} : dépassement (y={y / mm:.0f} mm)")
    L.end_page()


# ───────────────────────── pages d'ouverture ─────────────────────────
def couverture(L):
    L.new(footer=False); c = L.c
    c.setStrokeColor(ACC); c.setLineWidth(1.2)
    c.roundRect(12 * mm, 12 * mm, PW - 24 * mm, PH - 24 * mm, 6 * mm)
    c.setLineWidth(0.5); c.roundRect(15 * mm, 15 * mm, PW - 30 * mm, PH - 30 * mm, 4.5 * mm)
    c.setFont("R", 14); c.setFillColor(MUTE); c.drawCentredString(PW / 2, PH - 45 * mm, "CE1  ·  21 jours  ·  lecture et écriture")
    c.setFont("B", 46); c.setFillColor(INK); c.drawCentredString(PW / 2, PH - 72 * mm, "Je lis, j'écris !")
    c.setFont("R", 17); c.setFillColor(ACC)
    c.drawCentredString(PW / 2, PH - 86 * mm, "21 jours pour retrouver le plaisir de lire")
    cat(c, PW / 2, PH / 2 - 42 * mm, 2.2)
    c.setStrokeColor(LINE); c.setLineWidth(0.8)
    c.line(PW / 2 - 45 * mm, PH / 2 - 44 * mm, PW / 2 + 45 * mm, PH / 2 - 44 * mm)
    c.setFont("R", 15); c.setFillColor(INK)
    c.drawCentredString(PW / 2, PH / 2 - 56 * mm, "avec Lina et son chat Moka")
    c.setFont("R", 14); c.setFillColor(MUTE); c.drawString(35 * mm, 40 * mm, "Ce livre appartient à :")
    c.setStrokeColor(SEY_B); c.line(88 * mm, 39 * mm, PW - 35 * mm, 39 * mm)
    L.end_page()


def guide_parents(L):
    L.new(); c = L.c
    y = PH - 22 * mm
    c.setFont("B", 22); c.setFillColor(INK); c.drawString(ML, y, "Le mot pour les parents")
    y -= 12 * mm
    blocs = [
        ("Objectif",
         "Relancer en 21 jours une lecture fluide et l'écriture des mots de base, après une longue "
         "pause. Le livre reprend les sons du CP, puis avance vers les sons complexes et la lecture de textes "
         "de plus en plus longs (de 35 à 170 mots). Il se termine par un bilan."),
        ("Le rituel : 3 pages par jour, 30 minutes environ",
         "Page 1 « Je découvre » (10 min) : le son, les syllabes, les mots, les mots-outils. "
         "Page 2 « Je lis » (10 min) : un épisode de l'histoire de Lina, lu 3 fois, puis les questions. "
         "Page 3 « J'écris » (10 min) : écriture attachée, exercice, copie, dictée. "
         "Mieux vaut 30 minutes chaque jour qu'une longue séance le week-end."),
        ("Comment aider",
         "Laissez votre enfant chercher avant de donner la réponse. En cas d'erreur, montrez le mot du doigt "
         "et dites « regarde bien ce son » plutôt que « non ». Faites relire la phrase entière après un mot "
         "difficile. Félicitez l'effort, pas seulement le résultat. Arrêtez la séance si la fatigue s'installe."),
        ("Les aides visuelles du livre",
         "Syllabes alternées noir / gris dans les listes de mots. Le son du jour est en gras bleu dans les textes. "
         "Peu de couleurs, volontairement, pour garder l'attention sur les lettres."),
        ("La dictée",
         "Elle est dans « Le coin des parents » à la fin du livre. Dites chaque mot deux fois, lentement, sans "
         "insister exagérément sur les lettres muettes. Corrigez ensuite ensemble : l'enfant compare avec le modèle."),
        ("La lecture chronométrée (à partir du jour 15)",
         "Lancez un minuteur d'une minute et comptez les mots lus correctement (les nombres gris à droite du "
         "texte aident à compter). Repères Éduscol en fin d'année : CP ≈ 50 mots/min, CE1 ≈ 70 mots/min. "
         "Le bilan final propose les mêmes mesures sur un texte nouveau."),
        ("À noter",
         "Ce livret est un outil d'entraînement familial. Il ne remplace ni l'enseignant ni un bilan "
         "orthophonique : si les difficultés persistent après le bilan, parlez-en à l'enseignant de la classe."),
    ]
    for t, txt in blocs:
        c.setFillColor(ACC); c.rect(ML, y - 0.2 * mm, 1.6 * mm, 4.4 * mm, stroke=0, fill=1)
        c.setFont("B", 12.5); c.setFillColor(INK); c.drawString(ML + 4 * mm, y, t)
        y -= 6.5 * mm
        y = draw_para(c, ML + 4 * mm, y, txt, W - 4 * mm, 11, 1.5, color=INK) - 4 * mm
    L.end_page()


LABELS = {1: "a e i o u", 2: "ou", 3: "on", 4: "an  en", 5: "in", 6: "oi", 7: "Révision",
          8: "ch", 9: "eu", 10: "au  eau", 11: "è  ai", 12: "gn  ill", 13: "c  g", 14: "Révision",
          15: "s  ss", 16: "pluriel", 17: "être avoir", 18: "ph  er", 19: ". ? !", 20: "fluidité", 21: "Révision"}


def parcours(L):
    L.new(); c = L.c
    y = PH - 22 * mm
    c.setFont("B", 22); c.setFillColor(INK); c.drawString(ML, y, "Mon parcours en 21 jours")
    c.setFont("R", 11.5); c.setFillColor(MUTE)
    c.drawString(ML, y - 8 * mm, "Chaque soir, je colorie l'étoile du jour terminé.")
    y -= 18 * mm
    semaines = ["Semaine 1 — Je retrouve les sons", "Semaine 2 — Les sons plus difficiles",
                "Semaine 3 — Je lis vite et bien, j'écris juste"]
    bw = (W - 6 * 3 * mm) / 7; bh = 34 * mm
    for s in range(3):
        c.setFont("B", 13); c.setFillColor(ACC); c.drawString(ML, y, semaines[s])
        y -= 4 * mm
        for k in range(7):
            d = JOURS[s * 7 + k]
            bx = ML + k * (bw + 3 * mm); by = y - bh
            rbox(c, bx, by, bw, bh, fill=PALE if d.get("revision") else None, stroke=SEY_B, r=2 * mm)
            c.setFont("B", 11); c.setFillColor(MUTE); c.drawCentredString(bx + bw / 2, by + bh - 6 * mm, f"Jour {d['n']}")
            lab = LABELS[d["n"]]
            size = 15
            while pdfmetrics.stringWidth(lab, "B", size) > bw - 3 * mm and size > 8:
                size -= 0.5
            c.setFont("B", size); c.setFillColor(INK); c.drawCentredString(bx + bw / 2, by + bh - 16 * mm, lab)
            c.setFont("R", 8); c.setFillColor(SYL)
            star(c, bx + bw / 2, by + 8 * mm, 4.6 * mm)
        y -= bh + 10 * mm
    rbox(c, ML, y - 22 * mm, W, 24 * mm, stroke=ACC, lw=1.1)
    c.setFont("B", 16); c.setFillColor(INK); c.drawString(ML + 8 * mm, y - 9 * mm, "Jour 22 : mon grand bilan")
    c.setFont("R", 11.5); c.setFillColor(MUTE)
    c.drawString(ML + 8 * mm, y - 16 * mm, "Je lis, je comprends, j'écris… et je reçois mon diplôme !")
    star(c, PW - ML - 14 * mm, y - 10 * mm, 7 * mm)
    L.end_page()


def personnages(L):
    L.new(); c = L.c
    y = PH - 22 * mm
    c.setFont("B", 22); c.setFillColor(INK); c.drawString(ML, y, "Comment ça marche ?")
    y -= 14 * mm
    etapes = [("1", "Je découvre", "Je lis le son du jour, les syllabes, les mots et mes 3 mots-outils."),
              ("2", "Je lis", "Je lis l'histoire de Lina trois fois, puis je réponds aux questions."),
              ("3", "J'écris", "Je repasse, j'écris, je complète, je copie, et je fais ma dictée.")]
    for num, t, txt in etapes:
        rbox(c, ML, y - 22 * mm, W, 24 * mm, stroke=SEY_B)
        c.setFillColor(ACC); c.circle(ML + 12 * mm, y - 10 * mm, 6 * mm, stroke=0, fill=1)
        c.setFillColor(HexColor("#ffffff")); c.setFont("B", 18); c.drawCentredString(ML + 12 * mm, y - 12.4 * mm, num)
        c.setFont("B", 16); c.setFillColor(INK); c.drawString(ML + 24 * mm, y - 8 * mm, t)
        c.setFont("R", 12); c.setFillColor(MUTE); c.drawString(ML + 24 * mm, y - 15 * mm, txt)
        y -= 29 * mm
    y -= 4 * mm
    c.setFont("B", 18); c.setFillColor(INK); c.drawString(ML, y, "Les personnages de l'histoire")
    y -= 10 * mm
    pers = [("Lina", "Elle a 7 ans et elle est en CE1, comme toi."),
            ("Moka", "Le chat de Lina. Il est curieux et un peu peureux."),
            ("Tom", "Le grand frère de Lina. Il aime rigoler."),
            ("Papa et maman", "Les parents de Lina."),
            ("Mamie", "La grand-mère de Lina. Elle habite loin, à la campagne.")]
    cat(c, PW - ML - 14 * mm, y - 52 * mm, 0.9)
    for n, t in pers:
        c.setFont("B", 14); c.setFillColor(ACC); c.drawString(ML + 2 * mm, y, n)
        c.setFont("R", 12.5); c.setFillColor(INK); c.drawString(ML + 42 * mm, y, t)
        y -= 10 * mm
    y -= 6 * mm
    rbox(c, ML, y - 32 * mm, W, 34 * mm, fill=PALE, stroke=SEY_B)
    c.setFont("B", 13); c.setFillColor(INK); c.drawString(ML + 6 * mm, y - 7 * mm, "Mes 3 règles d'or")
    regles = ["Je lis avec mon doigt sous les mots.",
              "Si je bloque, je découpe le mot en syllabes, puis je relis la phrase.",
              "J'écris lentement, sur la ligne, en attachant les lettres."]
    yy = y - 14 * mm
    for r in regles:
        star(c, ML + 9 * mm, yy + 1.4 * mm, 2.4 * mm, fill=True)
        c.setFont("R", 12.5); c.setFillColor(INK); c.drawString(ML + 14 * mm, yy, r)
        yy -= 7 * mm
    L.end_page()


# ───────────────────────── bilan final ─────────────────────────
def header_bilan(L, titre, sous=None):
    c = L.c
    top = PH - 13 * mm
    c.setFont("B", 10.5); c.setFillColor(ACC); c.drawString(ML, top, "MON GRAND BILAN")
    y = PH - 27 * mm
    c.setFont("B", 19); c.setFillColor(INK); c.drawString(ML, y, titre)
    if sous:
        w = pdfmetrics.stringWidth(titre, "B", 19)
        c.setFont("R", 12); c.setFillColor(MUTE); c.drawString(ML + w + 4 * mm, y + 0.5 * mm, sous)
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(ML, y - 4.5 * mm, PW - ML, y - 4.5 * mm)
    return y - 13 * mm


def score_box(c, y, label, total):
    rbox(c, PW - ML - 64 * mm, y - 2.5 * mm, 64 * mm, 10 * mm, stroke=ACC)
    c.setFont("R", 11); c.setFillColor(INK)
    c.drawString(PW - ML - 61 * mm, y + 0.6 * mm, f"{label} : ______ / {total}")


def bilan(L):
    c = L.c
    # intro
    L.new()
    y = header_bilan(L, "Le jour du bilan", "à faire le jour 22, au calme")
    cat(c, PW / 2, y - 62 * mm, 1.6)
    y -= 75 * mm
    txt = ("Bravo, tu as terminé les 21 jours ! Aujourd'hui, tu vas montrer tout ce que tu sais faire. "
           "Ce n'est pas une interrogation : c'est pour voir tes progrès. Prends ton temps et fais de ton mieux.")
    y = draw_para(c, ML + 10 * mm, y, txt, W - 20 * mm, 15, 1.6)
    y -= 6 * mm
    epreuves = [("1", "Je lis des syllabes et des mots", "lecture à voix haute, 1 minute par liste"),
                ("2", "Je lis les mots-outils", "lecture à voix haute"),
                ("3", "Je lis un texte nouveau", "lecture continue, chronométrée"),
                ("4", "Je comprends", "je coche la bonne réponse"),
                ("5", "J'écris", "dictée, copie et phrase libre")]
    for num, t, s in epreuves:
        c.setFillColor(ACC); c.circle(ML + 14 * mm, y + 1.6 * mm, 3.8 * mm, stroke=0, fill=1)
        c.setFillColor(HexColor("#ffffff")); c.setFont("B", 12); c.drawCentredString(ML + 14 * mm, y + 0.2 * mm, num)
        c.setFont("B", 13.5); c.setFillColor(INK); c.drawString(ML + 22 * mm, y, t)
        c.setFont("R", 11); c.setFillColor(MUTE); c.drawString(ML + 22 * mm, y - 5.5 * mm, s)
        y -= 15 * mm
    y -= 2 * mm
    rbox(c, ML, y - 34 * mm, W, 36 * mm, fill=PALE, stroke=SEY_B)
    c.setFont("B", 12); c.setFillColor(INK); c.drawString(ML + 5 * mm, y - 6 * mm, "Pour l'adulte")
    consigne = ("Munissez-vous d'un minuteur et d'un crayon. Pendant la lecture, barrez discrètement chaque mot "
                "mal lu, sans interrompre l'enfant. Notez les scores dans les cadres, puis reportez-les dans la "
                "grille d'évaluation. La dictée est page « coin des parents ».")
    draw_para(c, ML + 5 * mm, y - 13 * mm, consigne, W - 10 * mm, 11, 1.5)
    L.end_page()

    # épreuve 1
    L.new()
    y = header_bilan(L, "1. Je lis des syllabes et des mots", "1 minute par liste")
    score_box(c, y + 1 * mm, "syllabes lues", 30); y = section(c, y, "Les syllabes")
    cols = 6; bw = (W - 5 * 2.5 * mm) / cols; bh = 12 * mm
    for i, s in enumerate(TEST_SYLLABES):
        r, k = divmod(i, cols)
        bx = ML + k * (bw + 2.5 * mm); by = y - (r + 1) * bh - r * 2.5 * mm + 3 * mm
        rbox(c, bx, by, bw, bh, r=2 * mm)
        c.setFont("R", 20); c.setFillColor(INK); c.drawCentredString(bx + bw / 2, by + bh / 2 - 6.5, s)
    y -= 5 * bh + 4 * 2.5 * mm + 10 * mm
    score_box(c, y + 1 * mm, "mots lus", 30); y = section(c, y, "Les mots")
    colw = W / 3
    for i, m in enumerate(TEST_MOTS):
        r, k = divmod(i, 3)
        x = ML + k * colw + 3 * mm; yy = y - r * 11.2 * mm - 4 * mm
        c.setFont("R", 20); c.setFillColor(INK); c.drawString(x, yy, m)
    L.end_page()

    # épreuve 2 et 3
    L.new()
    y = header_bilan(L, "2. Je lis les mots-outils")
    score_box(c, y + 1 * mm, "mots-outils lus", 20)
    y -= 10 * mm
    cols = 5; bw = (W - 4 * 3 * mm) / cols
    for i, m in enumerate(TEST_OUTILS):
        r, k = divmod(i, cols)
        bx = ML + k * (bw + 3 * mm); by = y - (r + 1) * 12 * mm - r * 2.5 * mm + 4 * mm
        rbox(c, bx, by, bw, 12 * mm, r=2 * mm)
        c.setFont("R", 18); c.setFillColor(INK); c.drawCentredString(bx + bw / 2, by + 4 * mm, m)
    y -= 4 * 14.5 * mm + 10 * mm
    c.setFont("B", 19); c.setFillColor(INK); c.drawString(ML, y, "3. Je lis un texte nouveau")
    c.setFont("R", 12); c.setFillColor(MUTE)
    c.drawString(ML + pdfmetrics.stringWidth("3. Je lis un texte nouveau", "B", 19) + 4 * mm, y + 0.5 * mm,
                 "1 minute, à voix haute")
    y -= 11 * mm
    c.setFont("B", 16); c.setFillColor(ACC); c.drawString(ML + 2 * mm, y, TEST_TEXTE_TITRE)
    y -= 10 * mm
    y = draw_para(c, ML + 2 * mm, y, TEST_TEXTE, W - 14 * mm, 14, 1.55, counts=True)
    c.setFont("R", 8.5); c.setFillColor(SYL); c.drawRightString(PW - ML, y + 2 * mm, "nombre de mots")
    y -= 6 * mm
    rbox(c, ML, y - 11 * mm, W, 13 * mm, stroke=ACC)
    c.setFont("R", 11.5); c.setFillColor(INK)
    c.drawString(ML + 5 * mm, y - 6 * mm,
                 "Mots lus en 1 minute : ______   −  erreurs : ______   =  mots bien lus en 1 min : ______")
    L.end_page()

    # épreuve 4 + copie
    L.new()
    y = header_bilan(L, "4. Je comprends", "je relis le texte si j'ai besoin")
    score_box(c, y + 1 * mm, "bonnes réponses", 5)
    y -= 12 * mm
    for k, (q, choix, _) in enumerate(TEST_QCM, 1):
        c.setFont("B", 13.5); c.setFillColor(ACC); c.drawString(ML + 2 * mm, y, f"{k}.")
        c.setFont("R", 13.5); c.setFillColor(INK); c.drawString(ML + 9 * mm, y, q)
        y -= 9 * mm
        x = ML + 12 * mm
        for ch in choix:
            checkbox(c, x, y - 0.5 * mm, 4.2 * mm)
            c.setFont("R", 13); c.setFillColor(INK); c.drawString(x + 6.5 * mm, y, ch)
            x += max(48 * mm, pdfmetrics.stringWidth(ch, "R", 13) + 16 * mm)
        y -= 13 * mm
    y -= 4 * mm
    c.setFont("B", 19); c.setFillColor(INK); c.drawString(ML, y, "5. J'écris")
    y -= 11 * mm
    y = section(c, y, "a) Je copie la phrase", "en écriture attachée, sans oublier le point")
    bases, ybot = seyes(c, ML, y + 1 * mm, W, 2)
    cursive(c, TEST_COPIE, ML + 12 * mm, bases[0], CUR, INK)
    y = ybot - 8 * mm
    y = section(c, y, "b) J'écris une phrase toute seule", "sur le bonhomme de neige")
    seyes(c, ML, y + 1 * mm, W, 2)
    L.end_page()

    # dictée
    L.new()
    y = header_bilan(L, "5. J'écris (suite) : ma dictée")
    score_box(c, y + 1 * mm, "mots justes", 10)
    y = section(c, y, "c) Les 10 mots")
    for k in range(5):
        bases, _ = seyes(c, ML, y + 1 * mm, W / 2 - 3 * mm, 1)
        seyes(c, ML + W / 2 + 3 * mm, y + 1 * mm, W / 2 - 3 * mm, 1)
        c.setFont("R", 9); c.setFillColor(SYL)
        c.drawString(ML + 3 * mm, bases[0] + 1 * mm, str(k * 2 + 1))
        c.drawString(ML + W / 2 + 6 * mm, bases[0] + 1 * mm, str(k * 2 + 2))
        y -= 5 * INTER + 3 * mm
    y -= 5 * mm
    score_box(c, y + 1 * mm, "mots justes", 15)
    y = section(c, y, "d) Les 2 phrases")
    _, y = seyes(c, ML, y + 1 * mm, W, 4)
    L.end_page()

    # grille
    L.new()
    y = header_bilan(L, "Grille d'évaluation", "pour l'adulte")
    cols = [("Épreuve", 62), ("Score", 24), ("Acquis", 28), ("En cours", 28), ("À retravailler", 32)]
    lignes = [("1. Syllabes", "/ 30", "27 à 30", "21 à 26", "0 à 20"),
              ("1. Mots", "/ 30", "27 à 30", "21 à 26", "0 à 20"),
              ("2. Mots-outils", "/ 20", "18 à 20", "14 à 17", "0 à 13"),
              ("3. Mots bien lus en 1 min", "", "50 et +", "35 à 49", "moins de 35"),
              ("4. Compréhension", "/ 5", "5", "4", "0 à 3"),
              ("5c. Dictée de mots", "/ 10", "9 à 10", "7 à 8", "0 à 6"),
              ("5d. Dictée de phrases", "/ 15", "13 à 15", "10 à 12", "0 à 9"),
              ("5a-b. Copie et phrase", "", "sans erreur", "1 à 2 erreurs", "3 erreurs et +")]
    x0 = ML; rh = 12 * mm
    c.setFillColor(PALE); c.rect(x0, y - rh + 4 * mm, W, rh, stroke=0, fill=1)
    x = x0
    for t, w in cols:
        c.setFont("B", 11); c.setFillColor(INK); c.drawString(x + 2.5 * mm, y - 1.5 * mm, t); x += w * mm
    y -= rh
    for row in lignes:
        x = x0
        for k, (cell, (_, w)) in enumerate(zip(row, cols)):
            c.setFont("B" if k == 0 else "R", 10.5 if k != 4 or len(cell) < 14 else 9.5)
            c.setFillColor(INK if k < 2 else MUTE)
            c.drawString(x + 2.5 * mm, y - 1.5 * mm, cell); x += w * mm
        c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(x0, y - rh + 4 * mm, x0 + W, y - rh + 4 * mm)
        y -= rh
    y -= 6 * mm
    notes = [
        "Seuils « Acquis / En cours / À retravailler » : repères proposés pour ce livret (environ 90 % et 70 % "
        "de réussite). Ce ne sont pas des normes officielles.",
        "Lecture en 1 minute : repères Éduscol de fin d'année : CP ≈ 50 mots/min, CE1 ≈ 70 mots/min. "
        "En début de CE1, 50 mots/min montre que le niveau de fin de CP est retrouvé ; l'objectif de fin d'année reste 70.",
        "Dictée de phrases : compter 1 point par mot bien écrit (7 + 8 = 15 mots).",
        "Si plusieurs épreuves sont « À retravailler » : refaire les jours correspondants (sons difficiles, "
        "mots-outils), puis refaire le bilan 2 semaines plus tard. Si les difficultés persistent, en parler à "
        "l'enseignant.",
    ]
    for n in notes:
        c.setFillColor(ACC); c.circle(ML + 1.5 * mm, y + 1.3 * mm, 0.9 * mm, stroke=0, fill=1)
        y = draw_para(c, ML + 5 * mm, y, n, W - 5 * mm, 10.5, 1.45, color=INK) - 2.5 * mm
    y -= 4 * mm
    c.setFont("B", 12.5); c.setFillColor(INK); c.drawString(ML, y, "Mes progrès")
    y -= 7 * mm
    c.setFont("R", 11); c.setFillColor(MUTE)
    c.drawString(ML, y, "Mots bien lus en 1 minute :     jour 15 : ______     jour 20 : ______     bilan : ______")
    y -= 9 * mm
    c.drawString(ML, y, "Ce que je réussis le mieux :")
    c.setStrokeColor(LINE); c.line(ML + 55 * mm, y - 1 * mm, PW - ML, y - 1 * mm)
    y -= 9 * mm
    c.drawString(ML, y, "Ce que je vais encore travailler :")
    c.line(ML + 64 * mm, y - 1 * mm, PW - ML, y - 1 * mm)
    L.end_page()


def diplome(L):
    L.new(footer=False); c = L.c
    c.setStrokeColor(ACC); c.setLineWidth(1.4)
    c.roundRect(14 * mm, 14 * mm, PW - 28 * mm, PH - 28 * mm, 6 * mm)
    c.setLineWidth(0.5); c.roundRect(17 * mm, 17 * mm, PW - 34 * mm, PH - 34 * mm, 4.5 * mm)
    for k in range(5):
        star(c, PW / 2 + (k - 2) * 14 * mm, PH - 42 * mm, 4.5 * mm, fill=(k == 2))
    c.setFont("B", 44); c.setFillColor(INK); c.drawCentredString(PW / 2, PH - 72 * mm, "Diplôme")
    c.setFont("R", 17); c.setFillColor(ACC); c.drawCentredString(PW / 2, PH - 84 * mm, "de la grande lectrice")
    c.setFont("R", 14); c.setFillColor(MUTE); c.drawCentredString(PW / 2, PH - 108 * mm, "Ce diplôme est remis à")
    c.setStrokeColor(SEY_B); c.setLineWidth(0.8); c.line(50 * mm, PH - 124 * mm, PW - 50 * mm, PH - 124 * mm)
    lignes = ["qui a terminé les 21 jours de « Je lis, j'écris ! »",
              "et qui sait maintenant lire une histoire",
              "et écrire les mots de tous les jours."]
    y = PH - 140 * mm
    for l in lignes:
        c.setFont("R", 14); c.setFillColor(INK); c.drawCentredString(PW / 2, y, l); y -= 8 * mm
    cat(c, PW / 2, 62 * mm, 1.5)
    c.setFont("R", 12); c.setFillColor(MUTE)
    c.drawString(32 * mm, 38 * mm, "Le : ____________"); c.drawRightString(PW - 32 * mm, 38 * mm, "Signature : ____________")
    L.end_page()


def coin_parents(L):
    c = L.c
    def entete(titre):
        y = PH - 22 * mm
        c.setFont("B", 20); c.setFillColor(INK); c.drawString(ML, y, titre)
        c.setFont("R", 11); c.setFillColor(MUTE)
        c.drawString(ML, y - 7 * mm, "Dictées à lire à l'enfant et corrigés des exercices « Complète ». "
                     "À cacher pendant l'exercice !")
        return y - 16 * mm
    L.new(); y = entete("Le coin des parents")
    for d in JOURS:
        blocs = []
        mots = "  –  ".join(d["dictee_mots"])
        if d.get("lettre"):
            cor = "lettre libre : vérifier majuscule, point, mots-outils."
        else:
            cor = "  ·  ".join(f"{q.replace('_', a.upper() if False else a) if not d.get('ordre') else a}"
                               for q, a in d["completer"]) if "completer" in d else ""
            if d.get("ordre"):
                cor = "  ·  ".join(a for _, a in d["completer"])
        h = 6 * mm + para_height("Corrigé : " + cor, W - 24 * mm, 9.5, 1.35) + 8.5 * mm
        if y - h < 18 * mm:
            L.end_page(); L.new(); y = entete("Le coin des parents (suite)")
        c.setFont("B", 11); c.setFillColor(ACC); c.drawString(ML, y, f"Jour {d['n']}")
        c.setFont("R", 11); c.setFillColor(INK); c.drawString(ML + 20 * mm, y, mots)
        y -= 5.5 * mm
        c.setFont("R", 11); c.setFillColor(INK); c.drawString(ML + 20 * mm, y, "Phrase : « " + d["dictee_phrase"] + " »")
        y -= 5.5 * mm
        y = draw_para(c, ML + 20 * mm, y, "Corrigé : " + cor, W - 24 * mm, 9.5, 1.35, color=MUTE)
        c.setStrokeColor(LINE); c.setLineWidth(0.4); c.line(ML, y + 1.5 * mm, PW - ML, y + 1.5 * mm)
        y -= 3.5 * mm
    if y < 55 * mm:
        L.end_page(); L.new(); y = entete("Le coin des parents (suite)")
    y -= 4 * mm
    c.setFont("B", 13); c.setFillColor(INK); c.drawString(ML, y, "Bilan : la dictée")
    y -= 7 * mm
    c.setFont("R", 11); c.drawString(ML, y, "10 mots : " + "  –  ".join(TEST_DICTEE_MOTS[:5]))
    y -= 5.5 * mm; c.drawString(ML + 17 * mm, y, "  –  ".join(TEST_DICTEE_MOTS[5:]))
    y -= 7 * mm
    for k, p in enumerate(TEST_DICTEE_PHRASES, 1):
        c.drawString(ML, y, f"Phrase {k} : « {p} »"); y -= 6 * mm
    y -= 4 * mm
    c.setFont("B", 13); c.drawString(ML, y, "Bilan : réponses de compréhension")
    y -= 7 * mm
    c.setFont("R", 11)
    c.drawString(ML, y, "   ".join(f"{k}. {ch[r]}" for k, (_, ch, r) in enumerate(TEST_QCM, 1)))
    L.end_page()


def main():
    L = Livre(SORTIE)
    couverture(L)
    guide_parents(L)
    parcours(L)
    personnages(L)
    for d in JOURS:
        for f in (page_decouvrir, page_lire, page_ecrire):
            L.new(); f(L, d)
    bilan(L)
    diplome(L)
    coin_parents(L)
    L.c.save()
    print(f"{L.page} pages -> {SORTIE}")


if __name__ == "__main__":
    main()
