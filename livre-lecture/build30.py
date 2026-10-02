# -*- coding: utf-8 -*-
"""Génère « Mon grand livre de lecture et d'écriture — 30 jours » (PDF A4, 90 pages)."""
import io, math, os, random, re
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics

import build as B                      # polices, écriture cursive, Seyès, découpage du texte
from contenu30 import (J, BILANS, BLOCS, T_SYLLABES, T_MOTS, T_FLUENCE_TITRE, T_FLUENCE,
                       T_COMP_TITRE, T_COMP, T_COMP_Q, T_DICTEE_MOTS, T_DICTEE_PHRASES, T_PRODUCTION)

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "Mon-grand-livre-30-jours-CE1.pdf")

PW, PH = 210 * mm, 297 * mm
ML = 16 * mm
W = PW - 2 * ML
BOTTOM = 12 * mm
FS = 14                                   # taille de base demandée : 14 pt

INK = HexColor("#20232a")
MUTE = HexColor("#5f6670")
LINE = HexColor("#cfd4da")
STAR = HexColor("#f2b705")
THEMES = [  # (couleur principale, teinte claire) — une couleur par bloc de 5 jours
    (HexColor("#e4572e"), HexColor("#fde9e2")),
    (HexColor("#1f9e89"), HexColor("#dcf3ee")),
    (HexColor("#7b5cc4"), HexColor("#ece6f8")),
    (HexColor("#d9811a"), HexColor("#fcefd9")),
    (HexColor("#2f7dc1"), HexColor("#e0eef9")),
    (HexColor("#3c9a4b"), HexColor("#e2f2e4")),
]
NEUTRE = (HexColor("#2f7dc1"), HexColor("#eef3f8"))


def theme(n):
    return THEMES[(n - 1) // 5]


# ───────────────────────── primitives ─────────────────────────
def sw(t, f="R", s=FS):
    return pdfmetrics.stringWidth(t.replace(B.NB, " "), f, s)


def text(c, x, y, t, s=FS, f="R", col=INK):
    c.setFont(f, s); c.setFillColor(col); c.drawString(x, y, t.replace(B.NB, " "))


def ctext(c, x, y, t, s=FS, f="R", col=INK):
    c.setFont(f, s); c.setFillColor(col); c.drawCentredString(x, y, t)


def rbox(c, x, y, w, h, fill=None, stroke=LINE, r=3 * mm, lw=0.9):
    c.setLineWidth(lw)
    if stroke is None:
        c.setStrokeColor(white)
    else:
        c.setStrokeColor(stroke)
    if fill is not None:
        c.setFillColor(fill)
    c.roundRect(x, y, w, h, r, stroke=0 if stroke is None else 1, fill=1 if fill is not None else 0)


def star(c, cx, cy, r, fill=None, stroke=STAR, lw=1.0):
    p = c.beginPath()
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        (p.moveTo if i == 0 else p.lineTo)(cx + rr * math.cos(a), cy + rr * math.sin(a))
    p.close()
    c.setStrokeColor(stroke); c.setLineWidth(lw)
    if fill is not None:
        c.setFillColor(fill)
    c.drawPath(p, stroke=1, fill=1 if fill is not None else 0)


def checkbox(c, x, y, s=4 * mm, col=MUTE):
    c.setStrokeColor(col); c.setLineWidth(0.8); c.roundRect(x, y, s, s, 0.8 * mm, stroke=1, fill=0)


def auto_bold(t, keys):
    if not keys or "{" in t:
        return t
    pat = "|".join(sorted((re.escape(k) for k in keys), key=len, reverse=True))
    return re.sub(f"({pat})", r"{\1}", t)


def para(c, x, y, t, width, s=FS, lead=1.55, col=INK, bcol=None, counts=False):
    sp = sw(" ", "R", s); total = 0
    for ln in B.wrap(t, width, s):
        if ln is None:
            y -= s * 0.4; continue
        xx = x
        for wd in ln:
            for tt, b in wd:
                tt = tt.replace(B.NB, " ")
                c.setFont("B" if b else "R", s); c.setFillColor(bcol if (b and bcol) else col)
                c.drawString(xx, y, tt); xx += sw(tt, "B" if b else "R", s)
            xx += sp
        if counts:
            total += B.count_words(ln)
            c.setFont("R", 8.5); c.setFillColor(MUTE); c.drawRightString(x + width + 11 * mm, y + 1, str(total))
        y -= s * lead
    return y


def syl_word(c, x, y, word, s, col2):
    xx = x
    for k, syl in enumerate(word.split("-")):
        col = INK if k % 2 == 0 else col2
        for t, b in B.runs_of(syl):
            f = "B" if b else "R"
            c.setFont(f, s); c.setFillColor(col); c.drawString(xx, y, t); xx += sw(t, f, s)
    return xx - x


def seyes(c, ytop, rows, x=ML, width=W):
    return B.seyes(c, x, ytop, width, rows)


def section(c, y, t, col, note=None, s=15):
    c.setFillColor(col); c.circle(ML + 2 * mm, y + 1.8 * mm, 2 * mm, stroke=0, fill=1)
    text(c, ML + 6 * mm, y, t, s, "B", INK)
    if note:
        text(c, ML + 6 * mm + sw(t, "B", s) + 3 * mm, y + 0.3 * mm, note, 11.5, "R", MUTE)
    return y - 8 * mm


def word_boxes(c, x, y, words, s=FS, col=LINE, h=9 * mm):
    for wd in words:
        tw = sw(wd, "R", s) + 6 * mm
        rbox(c, x, y - 2.8 * mm, tw, h, stroke=col, r=2 * mm)
        text(c, x + 3 * mm, y, wd, s)
        x += tw + 3 * mm
    return x


# ───────────────────────── livre ─────────────────────────
class Livre:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PW, PH))
        self.c.setTitle("Mon grand livre de lecture et d'écriture — 30 jours (CE1)")
        self.page = 0

    def new(self):
        if self.page:
            self.c.showPage()
        self.page += 1

    def foot(self, col=MUTE):
        self.c.setFont("R", 9); self.c.setFillColor(col); self.c.drawCentredString(PW / 2, 7 * mm, str(self.page))


def band(c, col, light, pill, step, titre, right=None):
    c.setFillColor(light); c.rect(0, PH - 24 * mm, PW, 24 * mm, stroke=0, fill=1)
    c.setFillColor(col); c.rect(0, PH - 24 * mm, PW, 1.2 * mm, stroke=0, fill=1)
    pw = sw(pill, "B", 12) + 8 * mm
    rbox(c, ML, PH - 16 * mm, pw, 8 * mm, fill=col, stroke=None, r=4 * mm)
    text(c, ML + 4 * mm, PH - 13.4 * mm, pill, 12, "B", white)
    x = ML + pw + 4 * mm
    if step:
        text(c, x, PH - 13.6 * mm, step, 13, "B", col); x += sw(step, "B", 13) + 3 * mm
    s = 18
    while sw(titre, "B", s) > PW - ML - x - 34 * mm and s > 12:
        s -= 0.5
    text(c, x, PH - 14 * mm, titre, s, "B", INK)
    if right:
        c.setFont("R", 10); c.setFillColor(MUTE); c.drawRightString(PW - ML, PH - 13.4 * mm, right)
    return PH - 33 * mm


def progress(c, n, col):
    x0 = PW - ML - 29 * 2.6 * mm; y = PH - 20.5 * mm
    for i in range(30):
        c.setFillColor(col if i < n else white); c.setStrokeColor(col); c.setLineWidth(0.5)
        c.circle(x0 + i * 2.6 * mm, y, 0.9 * mm, stroke=1, fill=1)


# ───────────────────────── JOUR : page 1 « Je lis » ─────────────────────────
def page_lire(c, d, opt):
    col, light = theme(d["n"]); auto = d.get("auto")
    y = band(c, col, light, f"JOUR {d['n']}", "1 · Je lis", d["titre"], f"{d['n']} / 30")
    progress(c, d["n"], col)
    # carte du son
    lw = 52 * mm; rx = ML + lw + 5 * mm; rw = W - lw - 9 * mm
    rh = B.para_height(d["regle"], rw, 13, 1.4)
    h = max(30 * mm, 11 * mm + rh + 9 * mm)
    rbox(c, ML, y - h, W, h, fill=light, stroke=col, lw=1.2)
    s = 34
    while sw(d["son"], "B", s) > lw - 6 * mm and s > 13:
        s -= 1
    ctext(c, ML + lw / 2, y - h / 2 - s * 0.3, d["son"], s, "B", col)
    c.setStrokeColor(col); c.setLineWidth(0.6); c.line(ML + lw, y - h + 4 * mm, ML + lw, y - 4 * mm)
    rs = 14
    while sw(d["ref"], "B", rs) > rw and rs > 10:
        rs -= 0.5
    text(c, rx, y - 7.5 * mm, d["ref"], rs, "B")
    para(c, rx, y - 13.5 * mm, d["regle"], rw, 13, 1.4, col=MUTE)
    text(c, rx, y - h + 3.5 * mm, "Mots-outils du jour :  " + "  ·  ".join(d["outils"]), 13, "B", col)
    y -= h + 8 * mm

    grid = d.get("syllabes") or d.get("grille")
    if grid and not opt.get("no_grid"):
        lab = "Je lis les syllabes" if "syllabes" in d else "Je lis les mots-outils"
        y = section(c, y, lab, col, "de gauche à droite, à voix haute")
        n = len(grid); cols = min(10, math.ceil(n / 2)) if n > 8 else n
        rows = math.ceil(n / cols); gap = 2 * mm; bw = (W - (cols - 1) * gap) / cols; bh = 10 * mm
        for i, sy in enumerate(grid):
            r, k = divmod(i, cols)
            bx = ML + k * (bw + gap); by = y - (r + 1) * bh - r * gap + 4 * mm
            rbox(c, bx, by, bw, bh, fill=white, stroke=col, r=2 * mm, lw=0.7)
            fs = 18
            while sw(sy, "R", fs) > bw - 2 * mm:
                fs -= 1
            ctext(c, bx + bw / 2, by + 3 * mm, sy, fs)
        y -= rows * bh + (rows - 1) * gap + 5 * mm

    if d.get("ponctuation"):
        y = section(c, y, "Je lis la même phrase avec 3 voix", col)
        colw = W / 3
        for i, s_ in enumerate(d["ponctuation"]):
            r, k = divmod(i, 3)
            bx = ML + k * colw; by = y - (r + 1) * 12 * mm + 4 * mm
            rbox(c, bx + 1.5 * mm, by, colw - 3 * mm, 10 * mm, stroke=col, r=2 * mm, lw=0.7)
            body, p = s_[:-1], s_[-1]
            tw = sw(body, "R", 16) + sw(" " + p, "B", 18)
            x0 = bx + colw / 2 - tw / 2
            text(c, x0, by + 3.2 * mm, body, 16); text(c, x0 + sw(body, "R", 16), by + 3.2 * mm, " " + p, 18, "B", col)
        y -= math.ceil(len(d["ponctuation"]) / 3) * 12 * mm + 4 * mm

    if d.get("mots"):
        y = section(c, y, "Je lis les mots", col, "les syllabes changent de couleur pour m'aider")
        colw = W / 3
        for i, m in enumerate(d["mots"]):
            r, k = divmod(i, 3)
            x = ML + k * colw + 2 * mm; yy = y - r * 9 * mm - 3 * mm
            checkbox(c, x, yy, 3.6 * mm, col)
            syl_word(c, x + 6.5 * mm, yy, m, 17, col)
        y -= math.ceil(len(d["mots"]) / 3) * 9 * mm + 5 * mm

    if d.get("paires"):
        y = section(c, y, "Je lis et je compare", col, "la lettre en couleur est muette")
        colw = W / 2
        for a, b in d["paires"]:
            c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(ML, y - 2.5 * mm, PW - ML, y - 2.5 * mm)
            para(c, ML + 4 * mm, y, a, colw, 16, bcol=col)
            ctext(c, ML + colw - 4 * mm, y, "→", 16, "R", col)
            para(c, ML + colw + 4 * mm, y, b, colw, 16, bcol=col)
            y -= 9.5 * mm
        y -= 3 * mm

    if d.get("conjugaison"):
        y = section(c, y, "Je lis les verbes", col, "puis je les récite sans regarder")
        colw = W / 2; hh = len(d["conjugaison"]) * 9 * mm + 11 * mm
        for k, lab in enumerate(["ÊTRE", "AVOIR"]):
            rbox(c, ML + k * (colw + 2 * mm), y - hh + 4 * mm, colw - 2 * mm, hh, fill=light, stroke=col)
            ctext(c, ML + k * (colw + 2 * mm) + colw / 2, y - 2 * mm, lab, 15, "B", col)
        yy = y - 11 * mm
        for a, b in d["conjugaison"]:
            text(c, ML + 10 * mm, yy, a, 16); text(c, ML + colw + 12 * mm, yy, b, 16)
            yy -= 9 * mm
        y -= hh + 4 * mm

    if d.get("groupes"):
        y = section(c, y, "Je lis par groupes de mots", col, "petite pause à chaque  /")
        for s_ in d["groupes"]:
            parts = s_.split(" / "); x = ML + 4 * mm
            for k, part in enumerate(parts):
                text(c, x, y, part, FS); x += sw(part, "R", FS)
                if k < len(parts) - 1:
                    text(c, x, y, "  /  ", FS, "B", col); x += sw("  /  ", "B", FS)
            y -= 8 * mm
        y -= 2 * mm

    if d.get("phrases") and not opt.get("no_phrases"):
        y = section(c, y, "Je lis les phrases", col)
        for p in d["phrases"]:
            c.setFillColor(col); c.circle(ML + 4 * mm, y + 1.5 * mm, 0.9 * mm, stroke=0, fill=1)
            para(c, ML + 7 * mm, y, auto_bold(p, auto), W - 7 * mm, FS, bcol=col)
            y -= 7.5 * mm
        y -= 2 * mm

    # texte
    y = section(c, y, "Je lis l'histoire : " + d["texte_titre"], col)
    chrono = d.get("chrono")
    y = para(c, ML + 2 * mm, y, auto_bold(d["texte"], auto), W - (15 * mm if chrono else 4 * mm),
             FS, 1.55, bcol=col, counts=chrono)
    y -= 1 * mm
    x = ML + 2 * mm
    text(c, x, y - 1 * mm, "Je lis 3 fois :", 12, "B", MUTE); x += sw("Je lis 3 fois :", "B", 12) + 4 * mm
    for lab in ["lentement", "mieux", "avec le ton"]:
        checkbox(c, x, y - 1.6 * mm, 3.8 * mm, col); text(c, x + 5.5 * mm, y - 1 * mm, lab, 12, "R", MUTE)
        x += sw(lab, "R", 12) + 12 * mm
    if chrono:
        text(c, x, y - 1 * mm, "En 1 minute : ____ mots", 12, "R", MUTE)
    y -= 10 * mm
    # compréhension orale
    y = section(c, y, "Je comprends", col, "je réponds à voix haute par une phrase")
    for k, q in enumerate(d["questions"], 1):
        text(c, ML + 3 * mm, y, f"{k}.", FS, "B", col)
        text(c, ML + 10 * mm, y, q, FS)
        checkbox(c, PW - ML - 5 * mm, y - 0.6 * mm, 4 * mm, col)
        y -= 8 * mm
    return y


# ───────────────────────── exercices ─────────────────────────
def blank(c, x, y, s, size=17, col=INK, lc=None):
    parts = s.split("_")
    for k, p in enumerate(parts):
        text(c, x, y, p, size, "R", col); x += sw(p, "R", size)
        if k < len(parts) - 1:
            c.setStrokeColor(lc or MUTE); c.setLineWidth(1)
            c.line(x + 1 * mm, y - 1.2 * mm, x + 13 * mm, y - 1.2 * mm); x += 14 * mm
    return x


def exercice(c, y, ex, col, light):
    t = ex["type"]
    y = section(c, y, ex["titre"], col, ex.get("note"))
    it = ex.get("items", [])
    if t == "complete":
        long_ = any(len(q) > 11 for q, _ in it)
        cols = 2 if long_ else 3; colw = W / cols
        for k, (q, _a) in enumerate(it):
            r, kk = divmod(k, cols)
            blank(c, ML + kk * colw + 4 * mm, y - r * 10 * mm - 1 * mm, q, 15 if long_ else 18, lc=col)
        y -= math.ceil(len(it) / cols) * 10 * mm
    elif t == "entoure":
        colw = W / 3
        for k, (a, b) in enumerate(it):
            r, kk = divmod(k, 3)
            x = ML + kk * colw + 6 * mm; yy = y - r * 11 * mm - 1 * mm
            for j, sy in enumerate((a, b)):
                rbox(c, x + j * 22 * mm, yy - 3 * mm, 18 * mm, 9.5 * mm, stroke=col, r=4.5 * mm, lw=0.7)
                ctext(c, x + j * 22 * mm + 9 * mm, yy, sy, 17)
        y -= math.ceil(len(it) / 3) * 11 * mm
    elif t == "relie":
        right = [it[i][1] for i in ex["ordre_droite"]]
        for k, (a, _) in enumerate(it):
            yy = y - k * 8 * mm - 1 * mm
            text(c, ML + 8 * mm, yy, a, 16)
            c.setFillColor(col); c.circle(ML + 60 * mm, yy + 1.6 * mm, 1.2 * mm, stroke=0, fill=1)
            c.circle(ML + 100 * mm, yy + 1.6 * mm, 1.2 * mm, stroke=0, fill=1)
            text(c, ML + 106 * mm, yy, right[k], 16)
        y -= len(it) * 8 * mm
    elif t == "intrus":
        for k, (mots, _) in enumerate(it):
            yy = y - k * 10.5 * mm - 1 * mm
            word_boxes(c, ML + 6 * mm, yy, mots, 16, col)
        y -= len(it) * 10.5 * mm
    elif t == "vraifaux":
        colw = W / 2
        for k, (s_, _) in enumerate(it):
            r, kk = divmod(k, 2)
            x = ML + kk * colw + 4 * mm; yy = y - r * 10 * mm - 1 * mm
            text(c, x, yy, s_, 15)
            for j, l in enumerate("VF"):
                cx = x + 55 * mm + j * 9 * mm
                c.setStrokeColor(col); c.setLineWidth(0.8); c.circle(cx, yy + 1.6 * mm, 3.4 * mm, stroke=1, fill=0)
                ctext(c, cx, yy, l, 13, "B", col)
        y -= math.ceil(len(it) / 2) * 10 * mm
    elif t == "devinettes":
        for k, (q, _) in enumerate(it):
            yy = y - k * 8 * mm - 1 * mm
            text(c, ML + 6 * mm, yy, q, 15)
            c.setStrokeColor(col); c.setLineWidth(0.8)
            c.line(ML + 10 * mm + sw(q, "R", 15), yy - 1 * mm, PW - ML, yy - 1 * mm)
        y -= len(it) * 8 * mm
    elif t == "colonnes":
        word_boxes(c, ML + 4 * mm, y - 1 * mm, ex["items"], 14, col)
        y -= 12 * mm
        colw = (W - 6 * mm) / 2
        for k, lab in enumerate(ex["cols"]):
            bx = ML + k * (colw + 6 * mm)
            rbox(c, bx, y - 15 * mm, colw, 19 * mm, fill=light, stroke=col)
            ctext(c, bx + colw / 2, y - 1.5 * mm, lab, 14, "B", col)
            for j in range(2):
                c.setStrokeColor(LINE); c.line(bx + 4 * mm, y - 7.5 * mm - j * 6 * mm, bx + colw - 4 * mm, y - 7.5 * mm - j * 6 * mm)
        y -= 19 * mm
    elif t == "choix":
        colw = W / 2
        for k, (q, ch, _) in enumerate(it):
            r, kk = divmod(k, 2)
            x = ML + kk * colw + 3 * mm; yy = y - r * 10.5 * mm - 1 * mm
            x = blank(c, x, yy, q, 15, lc=col)
            text(c, x + 2 * mm, yy, "(" + " / ".join(ch) + ")", 12, "R", col)
        y -= math.ceil(len(it) / 2) * 10.5 * mm
    elif t == "ponct":
        colw = W / 2
        for k, (q, _) in enumerate(it):
            r, kk = divmod(k, 2)
            x = ML + kk * colw + 4 * mm; yy = y - r * 10 * mm - 1 * mm
            x = blank(c, x, yy, q.replace(" _", "_"), 16, lc=col)
        y -= math.ceil(len(it) / 2) * 10 * mm
    elif t == "groupes":
        for k, (q, _) in enumerate(it):
            text(c, ML + 6 * mm, y - k * 9 * mm - 1 * mm, q, 16)
        y -= len(it) * 9 * mm
    elif t == "ordre_num":
        for k, (q, _) in enumerate(it):
            yy = y - k * 9 * mm - 1 * mm
            rbox(c, ML + 4 * mm, yy - 2.5 * mm, 8 * mm, 8 * mm, stroke=col, r=1.5 * mm)
            text(c, ML + 16 * mm, yy, q, 15)
        y -= len(it) * 9 * mm
    return y - 3 * mm


# ───────────────────────── JOUR : page 2 « J'écris + test du jour + note » ─────────────────────────
def note_du_jour(c, y, col, light, labels=("Je lis", "J'écris", "Ma dictée", "Mon test")):
    h = 21 * mm
    rbox(c, ML, y - h, W, h, fill=light, stroke=col, lw=1.2)
    text(c, ML + 4 * mm, y - 6.5 * mm, "Ma note du jour", 14, "B", col)
    text(c, ML + 4 * mm, y - 12 * mm, "l'adulte colorie", 10.5, "R", MUTE)
    text(c, ML + 4 * mm, y - 16.5 * mm, "les étoiles (0 à 5)", 10.5, "R", MUTE)
    x0 = ML + 44 * mm; cw = 27 * mm
    for k, lab in enumerate(labels):
        x = x0 + k * cw
        ctext(c, x + cw / 2 - 2 * mm, y - 7 * mm, lab, 11.5, "B", INK)
        for j in range(5):
            star(c, x + 2.5 * mm + j * 4.6 * mm, y - 14 * mm, 2.1 * mm, fill=white, stroke=STAR, lw=0.8)
    bx = PW - ML - 18 * mm
    rbox(c, bx, y - h + 3 * mm, 15 * mm, h - 6 * mm, fill=white, stroke=col, r=2 * mm)
    ctext(c, bx + 7.5 * mm, y - 10 * mm, "___", 13, "B", INK)
    ctext(c, bx + 7.5 * mm, y - 15.5 * mm, "/ 20", 12, "B", col)
    return y - h - 3 * mm


def page_ecrire(c, d, opt):
    col, light = theme(d["n"]); auto = d.get("auto")
    y = band(c, col, light, f"JOUR {d['n']}", "2 · J'écris", d["titre"], f"{d['n']} / 30")
    progress(c, d["n"], col)
    # écriture attachée
    y = section(c, y, "Je repasse et j'écris", col, "le modèle, je repasse le gris, puis j'écris seule")
    lvl = opt.get("lvl", 0)
    w1, w2 = d["ecrire"]
    rows = 4 if lvl == 0 else 3 if lvl < 3 else 2
    bases, ybot = seyes(c, y + 1 * mm, rows)
    def model_row(yb, words):
        x = ML + 12 * mm
        for wd in words:
            ww = B.cursive_width(wd, B.CUR)
            B.cursive(c, wd, x, yb, B.CUR, INK); x += ww + 7 * mm
            for _ in range(2 if len(words) == 1 else 1):
                if x + ww < PW - ML - 2 * mm:
                    B.cursive(c, wd, x, yb, B.CUR, B.TRACE); x += ww + 7 * mm
            x += 6 * mm
    if lvl == 0:
        model_row(bases[0], [w1]); model_row(bases[1], [w2]); B.cursive(c, d["copie"], ML + 12 * mm, bases[2], B.CUR, INK)
    else:
        model_row(bases[0], [w1, w2]); B.cursive(c, d["copie"], ML + 12 * mm, bases[1], B.CUR, INK)
        if lvl == 3:
            xa = ML + 14 * mm + B.cursive_width(d["copie"], B.CUR)
            c.setFillColor(theme(d["n"])[0]); c.setFont("B", 14); c.drawString(xa + 2 * mm, bases[1] + 0.5 * mm, "→")
    y = ybot - 6 * mm
    # exercice
    y = exercice(c, y, d["ex"], col, light)
    # dictée
    y = section(c, y, "Ma dictée", col, "l'adulte lit la dictée (page « coin des parents »)")
    _, y = seyes(c, y + 1 * mm, 2)
    y -= 6 * mm
    # production
    y = section(c, y, "J'écris toute seule", col)
    text(c, ML + 6 * mm, y + 0.5 * mm, d["production"], 13, "R", INK)
    y -= 3 * mm
    pr = d.get("prod_rows", 1) if lvl < 2 else 1
    _, y = seyes(c, y, pr)
    y -= 5 * mm
    # test du jour
    tw = W - 10 * mm
    th = B.para_height(auto_bold(d["test"], auto), tw, FS, 1.5) + 27 * mm
    rbox(c, ML, y - th, W, th, fill=white, stroke=col, lw=1.6, r=4 * mm)
    star(c, ML + 6 * mm, y - 5 * mm, 3 * mm, fill=STAR)
    text(c, ML + 11 * mm, y - 6.5 * mm, "Mon test du jour", 15, "B", col)
    text(c, ML + 11 * mm + sw("Mon test du jour", "B", 15) + 3 * mm, y - 6.3 * mm,
         "je lis ce texte nouveau à voix haute, sans aide", 11.5, "R", MUTE)
    yy = para(c, ML + 5 * mm, y - 14 * mm, auto_bold(d["test"], auto), tw, FS, 1.5, bcol=col)
    text(c, ML + 5 * mm, yy + 0.5 * mm, "Question : " + d["test_q"], FS, "B", INK)
    yy -= 6.5 * mm
    text(c, ML + 5 * mm, yy + 1 * mm, "Pour l'adulte :  temps ______ s    erreurs ______    réponse juste", 11, "R", MUTE)
    checkbox(c, ML + 5 * mm + sw("Pour l'adulte :  temps ______ s    erreurs ______    réponse juste", "R", 11) + 2 * mm, yy + 0.3 * mm, 3.5 * mm, col)
    y -= th + 4 * mm
    y = note_du_jour(c, y, col, light)
    return y


# ───────────────────────── mesure / ajustement automatique ─────────────────────────
_dummy = canvas.Canvas(io.BytesIO())


def fit(fn, d, opts):
    for o in opts:
        if fn(_dummy, d, o) >= BOTTOM:
            return o
    print(f"  ! jour {d['n']} {fn.__name__} : dépassement")
    return opts[-1]


# ───────────────────────── bilans et jeux ─────────────────────────
def mots_meles(c, y, mots, col, seed):
    N = 10; rnd = random.Random(seed)
    grid = [[None] * N for _ in range(N)]
    for wd in mots:
        for _ in range(500):
            horiz = rnd.random() < 0.5
            r = rnd.randrange(N if horiz else N - len(wd) + 1)
            k = rnd.randrange(N - len(wd) + 1 if horiz else N)
            cells = [(r, k + i) if horiz else (r + i, k) for i in range(len(wd))]
            if all(grid[a][b] in (None, wd[i]) for i, (a, b) in enumerate(cells)):
                for i, (a, b) in enumerate(cells):
                    grid[a][b] = wd[i]
                break
    letters = "ABCDEFGHIJLMNOPRSTUV"
    cs = 8.5 * mm; x0 = ML + 6 * mm
    for r in range(N):
        for k in range(N):
            ch = grid[r][k] or rnd.choice(letters)
            rbox(c, x0 + k * cs, y - (r + 1) * cs, cs, cs, fill=white, stroke=LINE, r=1 * mm, lw=0.5)
            ctext(c, x0 + k * cs + cs / 2, y - (r + 1) * cs + 2.6 * mm, ch, 15, "B", INK)
    xl = x0 + N * cs + 10 * mm
    text(c, xl, y - 6 * mm, "Je cherche :", 14, "B", col)
    for i, wd in enumerate(mots):
        checkbox(c, xl, y - 15 * mm - i * 9 * mm, 4 * mm, col)
        text(c, xl + 7 * mm, y - 14.5 * mm - i * 9 * mm, wd.lower().replace("velo", "vélo"), 15)
    return y - N * cs - 6 * mm


def jeu(c, y, j, col, light, seed):
    t = j["type"]
    if t == "motsmeles":
        y = section(c, y, j["titre"], col, j.get("note"))
        return mots_meles(c, y, j["mots"], col, seed)
    if t in ("relie", "devinettes"):
        return exercice(c, y, j, col, light)
    y = section(c, y, j["titre"], col, j.get("note"))
    if t == "entoure_son":
        for k, (m, ch, _) in enumerate(j["items"]):
            yy = y - k * 11 * mm - 1 * mm
            text(c, ML + 8 * mm, yy, m, 17, "B")
            for i, s_ in enumerate(ch):
                bx = ML + 60 * mm + i * 26 * mm
                rbox(c, bx, yy - 3 * mm, 20 * mm, 9.5 * mm, stroke=col, r=4.5 * mm, lw=0.8)
                ctext(c, bx + 10 * mm, yy, s_, 16)
        return y - len(j["items"]) * 11 * mm - 3 * mm
    if t == "motmystere":
        for k, (sy, _) in enumerate(j["items"]):
            yy = y - k * 11 * mm - 1 * mm
            rbox(c, ML + 6 * mm, yy - 3 * mm, 62 * mm, 9.5 * mm, fill=light, stroke=col, r=2 * mm)
            ctext(c, ML + 37 * mm, yy, sy, 16, "B", col)
            text(c, ML + 74 * mm, yy, "→", 16, "R", col)
            c.setStrokeColor(MUTE); c.line(ML + 84 * mm, yy - 1 * mm, PW - ML, yy - 1 * mm)
        return y - len(j["items"]) * 11 * mm - 3 * mm
    if t == "vraifaux_texte":
        rbox(c, ML, y - 46 * mm, W, 49 * mm, fill=light, stroke=None)
        para(c, ML + 4 * mm, y - 4 * mm, j["texte"], W - 8 * mm, FS, 1.5)
        y -= 54 * mm
        for k, (s_, _) in enumerate(j["items"]):
            yy = y - k * 11 * mm
            text(c, ML + 6 * mm, yy, s_, 15)
            for i, l in enumerate("VF"):
                cx = PW - ML - 22 * mm + i * 11 * mm
                c.setStrokeColor(col); c.circle(cx, yy + 1.6 * mm, 3.8 * mm, stroke=1, fill=0)
                ctext(c, cx, yy, l, 14, "B", col)
        return y - len(j["items"]) * 11 * mm
    return y


def bilan_pages(L, b):
    col, light = THEMES[b["n"] - 1]
    c = L.c
    if b.get("final"):
        L.new()
        y = band(c, col, light, "BILAN 6", "", "Je lis une dernière histoire")
        y = section(c, y, "Je lis l'histoire : " + b["texte_titre"], col, "puis je chronomètre 1 minute")
        y = para(c, ML + 2 * mm, y, b["texte"], W - 15 * mm, FS, 1.6, counts=True) - 6 * mm
        y = section(c, y, "Je comprends", col, "j'écris ma réponse sur la ligne")
        for k, q in enumerate(b["questions"], 1):
            text(c, ML + 3 * mm, y, f"{k}.", FS, "B", col); text(c, ML + 10 * mm, y, q)
            y -= 9 * mm
            c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(ML + 10 * mm, y, PW - ML, y)
            y -= 8 * mm
        note_du_jour(c, y - 2 * mm, col, light, ("Lecture", "Vitesse", "Réponses", "Soin"))
        L.foot(); L.new()
        y = band(c, col, light, "BILAN 6", "", "Prête pour le grand test !")
        y = section(c, y, "Ma liste de championne", col, "je coche ce que je sais faire")
        for s_ in b["checklist"]:
            checkbox(c, ML + 6 * mm, y - 0.8 * mm, 5 * mm, col); text(c, ML + 15 * mm, y, s_, 15)
            y -= 11 * mm
        y -= 4 * mm
        y = section(c, y, "Je lis fièrement", col)
        for s_ in b["phrases"]:
            star(c, ML + 8 * mm, y + 1.8 * mm, 2.6 * mm, fill=STAR); text(c, ML + 14 * mm, y, s_, 17, "B")
            y -= 11 * mm
        y -= 4 * mm
        y = section(c, y, "Je recopie la phrase", col)
        bases, y = seyes(c, y + 1 * mm, 2)
        B.cursive(c, "Je suis prête pour le grand test.", ML + 12 * mm, bases[0], B.CUR, INK)
        B.cat(c, PW / 2, y - 48 * mm, 1.3, col)
        L.foot()
        return
    L.new()
    y = band(c, col, light, f"BILAN {b['n']}", "", f"Je mélange les jours {b['apres'] - 4} à {b['apres']}")
    y = section(c, y, "Lecture rapide", col, "je lis chaque mot deux fois, de plus en plus vite")
    bw = (W - 3 * 3 * mm) / 4
    for i, m in enumerate(b["lecture"]):
        r, k = divmod(i, 4)
        bx = ML + k * (bw + 3 * mm); by = y - (r + 1) * 12 * mm + 4 * mm
        rbox(c, bx, by, bw, 10 * mm, fill=light, stroke=col, r=2.5 * mm, lw=0.7)
        ctext(c, bx + bw / 2, by + 3 * mm, m, 17)
    y -= 2 * 12 * mm + 6 * mm
    y = section(c, y, "Je complète avec le bon mot", col)
    for q, ch, _ in b["choix"]:
        x = blank(c, ML + 6 * mm, y, q, 15, lc=col)
        text(c, x + 3 * mm, y, "(" + " / ".join(ch) + ")", 13, "R", col)
        y -= 10 * mm
    y -= 2 * mm
    y = section(c, y, "Je remets les mots dans l'ordre", col, "puis j'écris la phrase")
    for q, _ in b["ordre"]:
        word_boxes(c, ML + 6 * mm, y, q.split(" / "), 15, col)
        y -= 10 * mm
        c.setStrokeColor(LINE); c.line(ML + 6 * mm, y, PW - ML, y)
        y -= 9 * mm
    y -= 2 * mm
    y = section(c, y, "Petit défi d'écriture", col)
    text(c, ML + 6 * mm, y + 0.5 * mm, b["defi"], 13)
    _, y = seyes(c, y - 3 * mm, 3)
    note_du_jour(c, y - 6 * mm, col, light, ("Lecture", "Mots", "Phrases", "Défi"))
    L.foot(); L.new()
    y = band(c, col, light, f"BILAN {b['n']}", "", "Je joue avec les mots")
    for i, jj in enumerate(b["jeux"]):
        y = jeu(c, y, jj, col, light, seed=b["n"] * 10 + i) - 6 * mm
    B.cat(c, PW - ML - 20 * mm, BOTTOM + 6 * mm, 1.1, col)
    L.foot()


# ───────────────────────── pages d'ouverture ─────────────────────────
def couverture(L):
    L.new(); c = L.c
    for i, (col, light) in enumerate(THEMES):
        c.setFillColor(light); c.rect(0, PH - (i + 1) * 9 * mm, PW, 9 * mm, stroke=0, fill=1)
    c.setFillColor(white); c.roundRect(14 * mm, 20 * mm, PW - 28 * mm, PH - 80 * mm, 8 * mm, stroke=0, fill=1)
    ctext(c, PW / 2, PH - 82 * mm, "CE1  ·  30 jours  ·  lecture et écriture", 15, "R", MUTE)
    ctext(c, PW / 2, PH - 102 * mm, "Mon grand livre", 40, "B", THEMES[0][0])
    ctext(c, PW / 2, PH - 118 * mm, "de lecture et d'écriture", 26, "B", INK)
    ctext(c, PW / 2, PH - 131 * mm, "30 jours pour lire de façon fluide et écrire sans peur", 15, "R", THEMES[4][0])
    B.cat(c, PW / 2, PH / 2 - 62 * mm, 2.1, INK)
    for k in range(5):
        star(c, PW / 2 + (k - 2) * 13 * mm, PH / 2 - 72 * mm, 4 * mm, fill=STAR if k == 2 else white)
    ctext(c, PW / 2, PH / 2 - 86 * mm, "avec Lina et son chat Moka", 15, "R", INK)
    text(c, 34 * mm, 34 * mm, "Ce livre appartient à :", 15, "R", MUTE)
    c.setStrokeColor(THEMES[1][0]); c.setLineWidth(1); c.line(92 * mm, 33 * mm, PW - 34 * mm, 33 * mm)


def mot_parents(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "PARENTS", "", "Le mode d'emploi")
    blocs = [
        ("Ce livre regroupe 4 cahiers",
         "Les exercices de « Je lis, j'écris ! », « Mon livre de lecture et d'écriture » et des deux "
         "cahiers « CE1 15 jours » sont réunis et rangés du plus facile au plus difficile : syllabes "
         "simples, sons complexes, phrases, puis textes longs."),
        ("Chaque jour : 2 pages, 30 à 45 minutes",
         "Page 1 « Je lis » : le son, les syllabes, les mots, les phrases, l'histoire lue 3 fois, puis les "
         "questions à l'oral. Page 2 « J'écris » : écriture attachée, un exercice ou un jeu, la dictée, une "
         "phrase écrite seule, le test du jour et la note. Tous les 5 jours : un bilan et une page de jeux."),
        ("Le test du jour",
         "Un petit texte nouveau, lu à voix haute sans aide. Notez le temps et les erreurs. "
         "Les textes s'allongent : environ 20 mots au jour 1, plus de 60 au jour 30."),
        ("La note du jour (sur 20)",
         "4 étoiles × 5. Je lis : 5 = tout lu seule, 3 = quelques aides, 1 = beaucoup d'aide. "
         "J'écris : soin, lettres bien formées, exercice juste. Ma dictée : 5 = 0 erreur, 4 = 1, 3 = 2, "
         "2 = 3 ou 4, 1 = 5 et plus. Mon test : 5 = lu sans erreur et réponse juste, 3 = quelques erreurs, "
         "1 = lecture difficile. Reportez la note dans « Mes notes » et dans la courbe de progrès."),
        ("Comment aider",
         "Laissez chercher quelques secondes avant d'aider. Montrez la syllabe à reprendre, puis faites "
         "relire le mot entier. Ne corrigez que 2 ou 3 points à la fois. Félicitez l'effort."),
        ("À savoir",
         "Repères Éduscol de fin d'année : CP ≈ 50 mots lus correctement par minute, CE1 ≈ 70. "
         "Les barèmes de ce livre sont des propositions, pas des normes officielles. Si la lecture reste "
         "très difficile après les 30 jours, parlez-en à l'enseignant."),
    ]
    for t, txt in blocs:
        c.setFillColor(THEMES[blocs.index((t, txt)) % 6][0]); c.circle(ML + 2 * mm, y + 1.8 * mm, 2 * mm, stroke=0, fill=1)
        text(c, ML + 6 * mm, y, t, 15, "B")
        y = para(c, ML + 6 * mm, y - 7 * mm, txt, W - 6 * mm, 13, 1.45) - 4 * mm
    L.foot()


def programme(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "PROGRAMME", "", "Mes 30 jours, du plus facile au plus difficile")
    for bi, (nom, sous, a, b) in enumerate(BLOCS):
        col, light = THEMES[bi]
        h = 5 * 6.2 * mm + 10 * mm
        rbox(c, ML, y - h, W, h, fill=light, stroke=None)
        text(c, ML + 4 * mm, y - 6 * mm, f"Jours {a} à {b} — {nom}", 14, "B", col)
        text(c, ML + 4 * mm + sw(f"Jours {a} à {b} — {nom}", "B", 14) + 3 * mm, y - 6 * mm, sous, 11, "R", MUTE)
        yy = y - 13 * mm
        for n in range(a, b + 1):
            d = J[n - 1]
            text(c, ML + 6 * mm, yy, f"Jour {n}", 12.5, "B", col)
            text(c, ML + 26 * mm, yy, d["titre"], 12.5)
            text(c, ML + 100 * mm, yy, d["texte_titre"], 11.5, "R", MUTE)
            star(c, PW - ML - 6 * mm, yy + 1.5 * mm, 2.4 * mm, fill=white)
            yy -= 6.2 * mm
        y -= h + 2 * mm
    L.foot()


def comment(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "BIENVENUE", "", "Comment ça marche ?")
    etapes = [("1", "Je lis", "le son, les syllabes, les mots, les phrases et l'histoire (3 fois)."),
              ("2", "J'écris", "je repasse, je fais l'exercice, la dictée et une phrase toute seule."),
              ("★", "Mon test du jour", "je lis un texte nouveau sans aide."),
              ("20", "Ma note", "l'adulte colorie mes étoiles : je vois mes progrès !")]
    for i, (num, t, txt) in enumerate(etapes):
        col, light = THEMES[i]
        rbox(c, ML, y - 20 * mm, W, 22 * mm, fill=light, stroke=None)
        c.setFillColor(col); c.circle(ML + 11 * mm, y - 9 * mm, 6.5 * mm, stroke=0, fill=1)
        if num == "★":
            star(c, ML + 11 * mm, y - 9 * mm, 3.6 * mm, fill=white, stroke=white)
        else:
            ctext(c, ML + 11 * mm, y - 11.5 * mm, num, 16 if len(num) < 2 else 13, "B", white)
        text(c, ML + 23 * mm, y - 6 * mm, t, 16, "B", col)
        text(c, ML + 23 * mm, y - 13 * mm, txt, 13.5)
        y -= 26 * mm
    y -= 4 * mm
    text(c, ML, y, "Les personnages", 18, "B"); y -= 10 * mm
    pers = [("Lina", "7 ans, en CE1, comme toi."), ("Moka", "son chat, curieux et un peu peureux."),
            ("Tom", "son grand frère, très rigolo."), ("Papa, maman et mamie", "la famille de Lina."),
            ("Nina, Léo, Julie, Karim…", "les amis de l'école.")]
    for i, (n, t) in enumerate(pers):
        text(c, ML + 3 * mm, y, n, 14, "B", THEMES[i][0]); text(c, ML + 62 * mm, y, t, 14)
        y -= 9 * mm
    B.cat(c, PW - ML - 18 * mm, y + 6 * mm, 1.0, INK)
    y -= 4 * mm
    rbox(c, ML, y - 30 * mm, W, 32 * mm, fill=HexColor("#fff7d6"), stroke=STAR)
    text(c, ML + 6 * mm, y - 7 * mm, "Mes règles d'or", 15, "B")
    for k, r in enumerate(["Je lis avec mon doigt sous les mots.",
                           "Si je bloque, je découpe le mot en syllabes, puis je relis la phrase.",
                           "J'écris lentement, sur la ligne, en attachant les lettres."]):
        star(c, ML + 9 * mm, y - 13.5 * mm - k * 7 * mm, 2.4 * mm, fill=STAR)
        text(c, ML + 14 * mm, y - 15 * mm - k * 7 * mm, r, 13.5)
    L.foot()


def mes_notes(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "MES NOTES", "", "Le tableau de mes notes")
    cols = [("Jour", 18), ("Je lis", 22), ("J'écris", 22), ("Dictée", 22), ("Test", 22), ("Total /20", 26), ("Test : temps", 30)]
    x = ML
    c.setFillColor(HexColor("#eef3f8")); c.rect(ML, y - 3 * mm, W, 9 * mm, stroke=0, fill=1)
    for t, w in cols:
        text(c, x + 2 * mm, y, t, 11.5, "B"); x += w * mm
    y -= 3 * mm
    rh = 7.45 * mm
    for n in range(1, 31):
        col, light = theme(n)
        if n % 2 == 0:
            c.setFillColor(light); c.rect(ML, y - rh, W, rh, stroke=0, fill=1)
        text(c, ML + 2 * mm, y - rh + 2.3 * mm, f"Jour {n}", 11.5, "B", col)
        y -= rh
    c.setStrokeColor(LINE); c.setLineWidth(0.4)
    x = ML
    for t, w in cols[:-1]:
        x += w * mm; c.line(x, PH - 36 * mm, x, y)
    L.foot()


# ───────────────────────── grand test final ─────────────────────────
def score(c, y, lab, tot, col):
    t = f"{lab} : ______ / {tot}"
    w = sw(t, "B", 12) + 8 * mm
    rbox(c, PW - ML - w, y - 2.5 * mm, w, 9.5 * mm, fill=white, stroke=col, r=2 * mm)
    text(c, PW - ML - w + 4 * mm, y + 0.3 * mm, t, 12, "B", col)


def grand_test(L):
    c = L.c; col, light = HexColor("#c2185b"), HexColor("#fce4ee")
    # intro
    L.new()
    y = band(c, col, light, "GRAND TEST", "", "Le jour du grand test")
    B.cat(c, PW / 2, y - 55 * mm, 1.5, col)
    y -= 66 * mm
    y = para(c, ML + 8 * mm, y, "Bravo, tu as fini les 30 jours ! Aujourd'hui, tu montres tout ce que tu "
             "sais faire. Ce n'est pas une interrogation : c'est pour voir tes progrès. Prends ton temps.",
             W - 16 * mm, 15, 1.55) - 6 * mm
    eps = [("1", "Je lis des syllabes et des mots", "40 points"), ("2", "Je lis un texte (fluidité)", "10 points"),
           ("3", "Je comprends un texte", "10 points"), ("4", "Ma dictée", "20 points"),
           ("5", "J'écris un petit texte", "20 points")]
    for num, t, p in eps:
        c.setFillColor(col); c.circle(ML + 12 * mm, y + 1.8 * mm, 4 * mm, stroke=0, fill=1)
        ctext(c, ML + 12 * mm, y + 0.2 * mm, num, 13, "B", white)
        text(c, ML + 20 * mm, y, t, 15, "B"); text(c, PW - ML - 25 * mm, y, p, 13, "R", col)
        y -= 12 * mm
    rbox(c, ML, y - 28 * mm, W, 30 * mm, fill=light, stroke=None)
    text(c, ML + 5 * mm, y - 6 * mm, "Pour l'adulte", 13, "B", col)
    para(c, ML + 5 * mm, y - 13 * mm, "Prévoyez un minuteur. Ne soufflez pas les réponses. Barrez discrètement "
         "les mots mal lus. Une hésitation corrigée seule n'est pas une erreur. Reportez les points dans la "
         "grille (page suivante du test). La dictée est dans « Le coin des parents ».", W - 10 * mm, 11.5, 1.4)
    L.foot()
    # épreuve 1
    L.new()
    y = band(c, col, light, "ÉPREUVE 1", "", "Je lis des syllabes et des mots")
    score(c, y + 1 * mm, "syllabes", 20, col)
    y = section(c, y, "Les syllabes", col, "1 point par syllabe bien lue")
    cols = 5; bw = (W - 4 * 3 * mm) / cols
    for i, s_ in enumerate(T_SYLLABES):
        r, k = divmod(i, cols)
        bx = ML + k * (bw + 3 * mm); by = y - (r + 1) * 12 * mm + 4 * mm
        rbox(c, bx, by, bw, 10.5 * mm, fill=light, stroke=col, r=2 * mm, lw=0.7)
        ctext(c, bx + bw / 2, by + 3.3 * mm, s_, 19)
    y -= 4 * 12 * mm + 10 * mm
    score(c, y + 1 * mm, "mots", 20, col)
    y = section(c, y, "Les mots", col, "1 point par mot bien lu")
    for i, m in enumerate(T_MOTS):
        r, k = divmod(i, 4)
        text(c, ML + 6 * mm + k * W / 4, y - r * 11 * mm - 2 * mm, m, 18)
    L.foot()
    # épreuve 2
    L.new()
    y = band(c, col, light, "ÉPREUVE 2", "", "Je lis un texte à voix haute")
    score(c, PH - 14.5 * mm, "fluidité", 10, col)
    y = section(c, y, T_FLUENCE_TITRE, col, "1 minute chronométrée")
    y = para(c, ML + 2 * mm, y, T_FLUENCE, W - 15 * mm, FS, 1.6, counts=True) - 4 * mm
    rbox(c, ML, y - 38 * mm, W, 40 * mm, fill=light, stroke=None)
    text(c, ML + 5 * mm, y - 6 * mm, "Pour l'adulte", 13, "B", col)
    text(c, ML + 5 * mm, y - 13 * mm, "Mots lus en 1 min : ______  −  erreurs : ______  =  mots bien lus : ______", 12)
    lignes = ["2 pts : mots lus correctement", "2 pts : peu d'arrêts inutiles", "2 pts : respect des points",
              "2 pts : groupes de mots naturels", "2 pts : voix claire"]
    for k, l in enumerate(lignes):
        r, kk = divmod(k, 2)
        checkbox(c, ML + 6 * mm + kk * 85 * mm, y - 21.5 * mm - r * 6.5 * mm, 3.6 * mm, col)
        text(c, ML + 12 * mm + kk * 85 * mm, y - 21 * mm - r * 6.5 * mm, l, 11.5)
    L.foot()
    # épreuve 3
    L.new()
    y = band(c, col, light, "ÉPREUVE 3", "", "Je comprends un texte")
    score(c, PH - 14.5 * mm, "compréhension", 10, col)
    y = section(c, y, T_COMP_TITRE, col, "je lis en silence, puis je réponds")
    rbox(c, ML, y - B.para_height(T_COMP, W - 8 * mm, FS, 1.55) - 3 * mm, W,
         B.para_height(T_COMP, W - 8 * mm, FS, 1.55) + 6 * mm, fill=light, stroke=None)
    y = para(c, ML + 4 * mm, y - 1 * mm, T_COMP, W - 8 * mm, FS, 1.55) - 8 * mm
    for k, (q, _) in enumerate(T_COMP_Q, 1):
        text(c, ML + 3 * mm, y, f"{k}.", FS, "B", col); text(c, ML + 10 * mm, y, q)
        y -= 9.5 * mm
        c.setStrokeColor(LINE); c.setLineWidth(0.7); c.line(ML + 10 * mm, y, PW - ML, y)
        y -= 8.5 * mm
    L.foot()
    # épreuve 4
    L.new()
    y = band(c, col, light, "ÉPREUVE 4", "", "Ma dictée")
    score(c, y + 1 * mm, "mots", 10, col)
    y = section(c, y, "10 mots", col, "1 point par mot juste")
    for k in range(5):
        bases, _ = B.seyes(c, ML, y + 1 * mm, W / 2 - 3 * mm, 1)
        B.seyes(c, ML + W / 2 + 3 * mm, y + 1 * mm, W / 2 - 3 * mm, 1)
        text(c, ML + 3 * mm, bases[0] + 1 * mm, str(2 * k + 1), 10, "B", col)
        text(c, ML + W / 2 + 6 * mm, bases[0] + 1 * mm, str(2 * k + 2), 10, "B", col)
        y -= 5 * B.INTER + 3 * mm
    y -= 6 * mm
    score(c, y + 1 * mm, "phrases", 10, col)
    y = section(c, y, "2 phrases", col, "5 points par phrase")
    seyes(c, y + 1 * mm, 4)
    L.foot()
    # épreuve 5
    L.new()
    y = band(c, col, light, "ÉPREUVE 5", "", "J'écris un petit texte")
    score(c, y + 1 * mm, "production", 20, col)
    y = section(c, y, "Mon texte", col)
    y = para(c, ML + 6 * mm, y, T_PRODUCTION, W - 6 * mm, FS, 1.5) - 2 * mm
    _, y = seyes(c, y, 8)
    y -= 6 * mm
    crit = ["Chaque phrase commence par une majuscule (4)", "Je laisse un espace entre les mots (4)",
            "Je termine les phrases par un point (4)", "Mon texte a du sens (4)", "J'utilise 3 mots pour raconter (4)"]
    for k, cr in enumerate(crit):
        checkbox(c, ML + 2 * mm, y - k * 7.5 * mm - 0.6 * mm, 3.8 * mm, col)
        text(c, ML + 8 * mm, y - k * 7.5 * mm, cr, 13)
    L.foot()
    # grille
    L.new()
    y = band(c, col, light, "RÉSULTATS", "", "Ma grille sur 100 points")
    lignes = [("1. Lecture de syllabes", "/ 20"), ("1. Lecture de mots", "/ 20"), ("2. Fluidité", "/ 10"),
              ("3. Compréhension", "/ 10"), ("4. Dictée de mots", "/ 10"), ("4. Dictée de phrases", "/ 10"),
              ("5. Production écrite", "/ 20")]
    for k, (l, t) in enumerate(lignes):
        if k % 2 == 0:
            c.setFillColor(light); c.rect(ML, y - 3.5 * mm, W, 10 * mm, stroke=0, fill=1)
        text(c, ML + 4 * mm, y, l, 14); text(c, PW - ML - 40 * mm, y, "______  " + t, 14, "B", col)
        y -= 10 * mm
    rbox(c, ML, y - 6 * mm, W, 12 * mm, fill=col, stroke=None, r=2 * mm)
    text(c, ML + 4 * mm, y - 1.5 * mm, "TOTAL", 15, "B", white); text(c, PW - ML - 40 * mm, y - 1.5 * mm, "______  / 100", 15, "B", white)
    y -= 18 * mm
    text(c, ML, y, "Mots bien lus en 1 minute (épreuve 2) : ______", 14, "B"); y -= 7 * mm
    text(c, ML, y, "Repères Éduscol de fin d'année : CP ≈ 50 mots/min, CE1 ≈ 70 mots/min.", 12, "R", MUTE); y -= 11 * mm
    bandes = [("90 à 100", "Les bases sont très bien installées : continuer la lecture chaque jour."),
              ("75 à 89", "Progrès solides : reprendre les erreurs repérées dans le test."),
              ("55 à 74", "Bases présentes mais fragiles : refaire les jours des sons difficiles."),
              ("moins de 55", "Reprendre plus lentement, avec des textes courts, et demander l'avis de l'enseignant.")]
    text(c, ML, y, "Lecture du résultat (barème proposé, non officiel)", 14, "B"); y -= 9 * mm
    for k, (a, t) in enumerate(bandes):
        cc = THEMES[[5, 1, 3, 0][k]][0]
        rbox(c, ML, y - 3 * mm, 26 * mm, 9 * mm, fill=cc, stroke=None, r=2 * mm)
        ctext(c, ML + 13 * mm, y, a, 11.5, "B", white)
        para(c, ML + 30 * mm, y, t, W - 30 * mm, 12, 1.35)
        y -= 12 * mm
    y -= 4 * mm
    text(c, ML, y, "Après le livre", 14, "B"); y -= 7 * mm
    para(c, ML, y, "Continuer 15 à 20 minutes de lecture à voix haute par jour et quelques lignes d'écriture. "
         "La fluidité se construit en relisant souvent des textes faciles, pas seulement des textes nouveaux.",
         W, 12.5, 1.45)
    L.foot()


def courbe(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "MES PROGRÈS", "", "Ma courbe de progrès")
    text(c, ML, y, "Chaque soir, je colorie la colonne jusqu'à ma note du jour (sur 20).", 13.5, "R", MUTE)
    y -= 8 * mm
    x0 = ML + 10 * mm; gw = W - 12 * mm; gh = 150 * mm; ybot = y - gh
    cw = gw / 30
    for v in range(0, 21, 2):
        yy = ybot + v / 20 * gh
        c.setStrokeColor(LINE if v % 10 else MUTE); c.setLineWidth(0.4 if v % 10 else 0.7); c.line(x0, yy, x0 + gw, yy)
        c.setFont("R", 9); c.setFillColor(MUTE); c.drawRightString(x0 - 2 * mm, yy - 1, str(v))
    for n in range(30):
        col, light = theme(n + 1)
        c.setFillColor(light); c.rect(x0 + n * cw + 0.6 * mm, ybot, cw - 1.2 * mm, gh, stroke=0, fill=1)
        ctext(c, x0 + n * cw + cw / 2, ybot - 5 * mm, str(n + 1), 8.5, "B", col)
    y = ybot - 16 * mm
    text(c, ML, y, "Mes mots bien lus en 1 minute", 15, "B"); y -= 9 * mm
    for k, lab in enumerate(["Jour 28", "Bilan 6", "Grand test"]):
        rbox(c, ML + k * 60 * mm, y - 12 * mm, 55 * mm, 15 * mm, fill=THEMES[k + 3][1], stroke=None)
        text(c, ML + k * 60 * mm + 4 * mm, y - 6 * mm, lab, 13, "B", THEMES[k + 3][0])
        text(c, ML + k * 60 * mm + 4 * mm, y - 10.5 * mm, "______ mots", 12)
    L.foot()


def diplome(L):
    L.new(); c = L.c
    for i, (col, light) in enumerate(THEMES):
        c.setStrokeColor(col); c.setLineWidth(1.4)
        c.roundRect(10 * mm + i * 1.6 * mm, 10 * mm + i * 1.6 * mm, PW - 20 * mm - i * 3.2 * mm, PH - 20 * mm - i * 3.2 * mm, 7 * mm)
    for k in range(5):
        star(c, PW / 2 + (k - 2) * 15 * mm, PH - 45 * mm, 5 * mm, fill=STAR)
    ctext(c, PW / 2, PH - 78 * mm, "Diplôme", 48, "B", THEMES[0][0])
    ctext(c, PW / 2, PH - 92 * mm, "de la championne de lecture", 20, "R", THEMES[4][0])
    ctext(c, PW / 2, PH - 118 * mm, "Ce diplôme est remis à", 15, "R", MUTE)
    c.setStrokeColor(THEMES[1][0]); c.setLineWidth(1); c.line(48 * mm, PH - 134 * mm, PW - 48 * mm, PH - 134 * mm)
    for k, l in enumerate(["qui a terminé les 30 jours de son grand livre,", "qui lit une histoire de façon continue",
                           "et qui écrit les mots de tous les jours."]):
        ctext(c, PW / 2, PH - 150 * mm - k * 9 * mm, l, 15)
    ctext(c, PW / 2, PH - 185 * mm, "Score au grand test : ______ / 100", 15, "B", THEMES[5][0])
    B.cat(c, PW / 2, 55 * mm, 1.5, INK)
    text(c, 30 * mm, 34 * mm, "Le : ____________", 13, "R", MUTE)
    c.setFont("R", 13); c.drawRightString(PW - 30 * mm, 34 * mm, "Signature : ____________")


def recap(L):
    L.new(); c = L.c
    y = band(c, *NEUTRE, "MÉMO", "", "Tous mes sons et mes mots-outils")
    y = section(c, y, "Mes sons", THEMES[0][0], "je relis cette page quand j'hésite")
    sons = [("ou", "loup"), ("on", "ballon"), ("an / en", "maman, dent"), ("in / ain / ein", "lapin, pain"),
            ("oi", "roi"), ("ch", "chat"), ("ge / gi / j", "girafe, jupe"), ("au / eau", "auto, bateau"),
            ("eu / œu", "feu, cœur"), ("è / ê / ai / ei", "mère, lait"), ("gn", "montagne"), ("ill / eil", "fille, soleil"),
            ("ç / gu", "garçon, guitare"), ("br / tr / pl", "bras, train"), ("s / ss", "rose, poisson"), ("ph", "photo")]
    colw = W / 2
    for i, (s_, m) in enumerate(sons):
        r, k = divmod(i, 2)
        col, light = THEMES[min(5, (r * 2 + k) // 3)]
        bx = ML + k * colw; by = y - r * 10.5 * mm
        rbox(c, bx, by - 3 * mm, colw - 3 * mm, 9 * mm, fill=light, stroke=None, r=2 * mm)
        text(c, bx + 4 * mm, by, s_, 14, "B", col); text(c, bx + 42 * mm, by, m, 14)
    y -= 8 * 10.5 * mm + 6 * mm
    y = section(c, y, "Mes mots-outils", THEMES[4][0], "je dois les lire d'un coup d'œil")
    tous = []
    for d in J:
        for o in d["outils"]:
            if o not in tous:
                tous.append(o)
    x = ML + 2 * mm
    for o in tous:
        w = sw(o, "R", 14) + 5 * mm
        if x + w > PW - ML:
            x = ML + 2 * mm; y -= 9 * mm
        rbox(c, x, y - 2.6 * mm, w, 8 * mm, fill=white, stroke=LINE, r=2 * mm, lw=0.6)
        text(c, x + 2.5 * mm, y, o, 14); x += w + 2 * mm
    L.foot()


def coin_parents(L):
    c = L.c

    def entete(sous=""):
        y = band(c, *NEUTRE, "PARENTS", "", "Le coin des parents" + sous)
        text(c, ML, y + 2 * mm, "Dictées à lire et corrigés. À cacher pendant les exercices !", 11.5, "R", MUTE)
        return y - 6 * mm

    def cor(ex):
        t = ex["type"]
        if t in ("complete", "devinettes"):
            return "  ·  ".join(q.replace("_", a) if "_" in q else a for q, a in ex["items"])
        if t == "entoure":
            return "l'adulte dit : " + ", ".join(a for a, _ in ex["items"])
        if t == "relie":
            return "  ·  ".join(f"{a} → {b}" for a, b in ex["items"])
        if t == "intrus":
            return "intrus : " + ", ".join(a for _, a in ex["items"])
        if t == "vraifaux":
            return "  ·  ".join(a for _, a in ex["items"])
        if t == "colonnes":
            return " | ".join(f"{h} : " + ", ".join(m) for h, m in zip(ex["cols"], ex["answers"]))
        if t == "choix":
            return "  ·  ".join(a for _, _, a in ex["items"])
        if t == "ponct":
            return "  ·  ".join(q.replace(" _", a) for q, a in ex["items"])
        if t == "groupes":
            return "  ·  ".join(a for _, a in ex["items"])
        if t == "ordre_num":
            return "ordre : " + ", ".join(str(a) for _, a in ex["items"])
        return ""

    L.new(); y = entete()
    for d in J:
        col = theme(d["n"])[0]
        cr = "Corrigé : " + cor(d["ex"])
        h = 11 * mm + B.para_height(cr, W - 22 * mm, 10, 1.3) + 1.5 * mm
        if y - h < BOTTOM + 2 * mm:
            L.foot(); L.new(); y = entete(" (suite)")
        text(c, ML, y, f"Jour {d['n']}", 11.5, "B", col)
        text(c, ML + 20 * mm, y, "Mots : " + "  –  ".join(d["dictee_mots"]), 11.5)
        y -= 5 * mm
        text(c, ML + 20 * mm, y, "Phrase : « " + d["dictee_phrase"] + " »", 11.5)
        y -= 5 * mm
        y = para(c, ML + 20 * mm, y, cr, W - 22 * mm, 10, 1.3, col=MUTE)
        c.setStrokeColor(LINE); c.setLineWidth(0.4); c.line(ML, y + 2 * mm, PW - ML, y + 2 * mm)
        y -= 2 * mm
    # bilans + test
    blocs = []
    for b in BILANS[:-1]:
        t = (f"Bilan {b['n']} : " + "  ·  ".join(a for _, _, a in b["choix"]) + "  ·  "
             + "  ·  ".join(a for _, a in b["ordre"]))
        for jj in b["jeux"]:
            if jj["type"] in ("motmystere", "devinettes", "entoure_son", "vraifaux_texte"):
                t += "  ·  jeu : " + ", ".join(str(it[-1]) for it in jj["items"])
        blocs.append(t)
    blocs.append("Grand test — dictée de mots : " + ", ".join(T_DICTEE_MOTS) + ".")
    blocs.append("Grand test — dictée de phrases : « " + T_DICTEE_PHRASES[0] + " »  puis  « " + T_DICTEE_PHRASES[1] + " »")
    blocs.append("Grand test — réponses de compréhension : " + "  ·  ".join(f"{k}. {a}" for k, (_, a) in enumerate(T_COMP_Q, 1)))
    for t in blocs:
        h = B.para_height(t, W, 11, 1.35) + 3 * mm
        if y - h < BOTTOM + 2 * mm:
            L.foot(); L.new(); y = entete(" (suite)")
        y = para(c, ML, y, t, W, 11, 1.35) - 2.5 * mm
    L.foot()


def main():
    L = Livre(SORTIE)
    couverture(L); mot_parents(L); programme(L); comment(L); mes_notes(L)
    for d in J:
        o1 = fit(page_lire, d, [{}, {"no_phrases": True}, {"no_phrases": True, "no_grid": True}])
        L.new(); page_lire(L.c, d, o1); L.foot()
        o2 = fit(page_ecrire, d, [{"lvl": 0}, {"lvl": 1}, {"lvl": 2}, {"lvl": 3}])
        L.new(); page_ecrire(L.c, d, o2); L.foot()
        if d["n"] % 5 == 0:
            bilan_pages(L, BILANS[d["n"] // 5 - 1])
    grand_test(L); courbe(L); diplome(L); recap(L); coin_parents(L)
    L.c.save()
    print(f"{L.page} pages -> {SORTIE}")


if __name__ == "__main__":
    main()
