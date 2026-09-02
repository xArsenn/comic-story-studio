# -*- coding: utf-8 -*-
"""v2: richer, scene-based drawing helpers — characters have limbs & poses,
panels get real backgrounds so the story reads as scenes, not floating icons."""

INK = "#1c1c1c"
PAPER = "#faf6ee"
ACCENT = "#b8402e"
WARM = "#e8a355"
SKY = "#f0e6d2"
GROUND = "#e4d9c2"
FONT = "Noto Sans CJK SC"

W, H = 800, 1200
MARGIN = 64
GAP = 40
PANEL_H = (H - 2*MARGIN - GAP) // 2
PANEL_W = W - 2*MARGIN
PANEL1_Y = MARGIN
PANEL2_Y = MARGIN + PANEL_H + GAP
TITLE_H_RATIO = 0.23


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def title_block(text, px, py, pw, ph, caption=None):
    n = len(text)
    size = 54 if n <= 6 else (42 if n <= 10 else 34)
    if caption:
        size -= 8
    cx = px + pw/2
    if caption:
        cy = py + ph*0.42
        cap = f'<text x="{cx}" y="{py+ph*0.74}" font-family="{FONT}" font-weight="500" font-size="19" fill="{ACCENT}" text-anchor="middle" opacity="0.9">{esc(caption)}</text>'
    else:
        cy = py + ph/2 + size*0.35
        cap = ""
    return f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-weight="900" font-size="{size}" fill="{INK}" text-anchor="middle" letter-spacing="1">{esc(text)}</text>' + cap


def gold_coin_guy(cx, cy, s=1.0, mood="tired"):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<path d="M -14 40 L -16 62" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="M 14 40 L 16 62" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="M -26 6 L -46 22" stroke="{WARM}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 26 6 L 46 22" stroke="{WARM}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<circle cx="0" cy="0" r="42" fill="{WARM}" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<circle cx="0" cy="0" r="30" fill="none" stroke="{INK}" stroke-width="2.5" opacity="0.6"/>')
    g.append(f'<text x="0" y="10" font-family="{FONT}" font-weight="900" font-size="26" fill="{INK}" text-anchor="middle">金</text>')
    g.append(f'<circle cx="-13" cy="-8" r="3.5" fill="{INK}"/><circle cx="13" cy="-8" r="3.5" fill="{INK}"/>')
    g.append(f'<path d="M -10 -32 l -8 -8 M 10 -32 l 8 -8" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def oil_barrel_guy(cx, cy, s=1.0, mood="energetic"):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<path d="M -14 46 L -18 70" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 14 46 L 18 70" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M -30 4 L -52 -16" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 30 4 L 52 -16" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<rect x="-32" y="-48" width="64" height="92" rx="8" fill="{INK}"/>')
    g.append(f'<rect x="-32" y="-20" width="64" height="10" fill="{ACCENT}"/>')
    g.append(f'<text x="0" y="-2" font-family="{FONT}" font-weight="900" font-size="20" fill="{PAPER}" text-anchor="middle">OIL</text>')
    g.append(f'<circle cx="-11" cy="20" r="4" fill="{PAPER}"/><circle cx="11" cy="20" r="4" fill="{PAPER}"/>')
    g.append(f'<path d="M -8 34 Q 0 40 8 34" fill="none" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def shady_guy(cx, cy, s=1.0):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<path d="M -14 40 L -16 62" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="M 14 40 L 16 62" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')
    g.append(f'<path d="M -24 4 L -40 24" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 24 4 L 40 24" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M -26 40 Q -30 -4 0 -10 Q 30 -4 26 40 Z" fill="{INK}" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<circle cx="0" cy="-32" r="24" fill="#d8cdb8" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<rect x="-20" y="-38" width="40" height="10" rx="4" fill="{INK}"/>')
    g.append(f'<rect x="-18" y="-36" width="36" height="10" rx="4" fill="{INK}"/>')
    g.append('</g>')
    return "\n".join(g)


def panel_frame(px, py, pw, ph):
    return f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="none" stroke="{INK}" stroke-width="3" rx="10"/>'


def scene_bg(px, py, pw, ph, ground_ratio=0.28, sky=SKY, ground=GROUND):
    gy = py + ph*(1-ground_ratio)
    return f'''<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="{sky}" opacity="0.55"/>
    <rect x="{px}" y="{gy}" width="{pw}" height="{ph-(gy-py)}" fill="{ground}" opacity="0.6"/>
    <line x1="{px}" y1="{gy}" x2="{px+pw}" y2="{gy}" stroke="{INK}" stroke-width="2" opacity="0.35"/>'''


def speech_bubble(cx, cy, w, h, text, tail="left", fill="white", stroke=INK, text_color=None, size=26, bold=False):
    text_color = text_color or INK
    x, y = cx - w/2, cy - h/2
    if tail == "left":
        pts = f'{x+w*0.18},{y+h} {x+w*0.02},{y+h+22} {x+w*0.34},{y+h}'
    elif tail == "right":
        pts = f'{x+w*0.66},{y+h} {x+w*0.98},{y+h+22} {x+w*0.82},{y+h}'
    else:
        pts = f'{x+w*0.4},{y+h} {x+w*0.5},{y+h+22} {x+w*0.6},{y+h}'
    weight = "900" if bold else "500"
    lines = text.split(chr(10))
    tspans = "".join(f'<tspan x="{cx}" dy="{0 if i==0 else size*1.15}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    ty = y + h/2 - (len(lines)-1)*size*0.55
    return f'''<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.35}" fill="{fill}" stroke="{stroke}" stroke-width="3.5"/>
    <polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="3.5"/>
    <text x="{cx}" y="{ty}" font-family="{FONT}" font-weight="{weight}" font-size="{size}" fill="{text_color}" text-anchor="middle" dominant-baseline="middle">{tspans}</text></g>'''


def heart(cx, cy, s=1.0, color=ACCENT):
    return f'''<path transform="translate({cx},{cy}) scale({s})"
    d="M 0 18 C -22 0 -26 -20 -12 -26 C -4 -30 0 -20 0 -14 C 0 -20 4 -30 12 -26 C 26 -20 22 0 0 18 Z"
    fill="{color}"/>'''


def motion_lines(cx, cy, n=3, length=30, angle=0, gap=10):
    import math
    g = ['<g>']
    for i in range(n):
        off = (i - (n-1)/2) * gap
        rad = math.radians(angle)
        dx, dy = -math.sin(rad)*off, math.cos(rad)*off
        x1 = cx + dx
        y1 = cy + dy
        x2 = x1 - length*math.cos(rad)
        y2 = y1 - length*math.sin(rad)
        g.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" opacity="0.55"/>')
    g.append('</g>')
    return "".join(g)


def sound_burst(cx, cy, text, s=1.0, color=ACCENT):
    pts = []
    import math
    n = 10
    for i in range(n*2):
        ang = math.pi*2*i/(n*2)
        r = 34 if i % 2 == 0 else 18
        pts.append(f'{cx+r*math.cos(ang)*s},{cy+r*math.sin(ang)*s}')
    return f'''<polygon points="{" ".join(pts)}" fill="{PAPER}" stroke="{color}" stroke-width="3"/>
    <text x="{cx}" y="{cy+7}" font-family="{FONT}" font-weight="900" font-size="{20*s}" fill="{color}" text-anchor="middle">{esc(text)}</text>'''


# ---------------- characters ----------------

def cat(cx, cy, s=1.0, mood="neutral", pose="stand", flip=False, tilt=0):
    fx = -1 if flip else 1
    g = [f'<g transform="translate({cx},{cy}) scale({fx*s},{s}) rotate({tilt})">']
    # tail
    g.append(f'<path d="M 34 30 Q 66 10 60 -26 Q 56 -46 38 -40" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    # legs / feet (pose variants)
    if pose == "run":
        g.append(f'<path d="M -14 70 L -34 92" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
        g.append(f'<path d="M 14 70 L 30 60" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    else:
        g.append(f'<ellipse cx="-18" cy="76" rx="12" ry="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
        g.append(f'<ellipse cx="18" cy="76" rx="12" ry="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    # body
    g.append(f'<ellipse cx="0" cy="34" rx="40" ry="46" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    # arms (pose variants)
    if pose == "point":
        g.append(f'<path d="M 30 20 L 76 -6" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<circle cx="80" cy="-9" r="6" fill="{INK}"/>')
        g.append(f'<ellipse cx="-24" cy="50" rx="11" ry="8" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    elif pose == "wave":
        g.append(f'<path d="M -30 10 Q -60 -10 -50 -40" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>')
        g.append(f'<ellipse cx="24" cy="50" rx="11" ry="8" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    elif pose == "knock":
        g.append(f'<path d="M 26 12 L 60 -14" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<circle cx="64" cy="-18" r="7" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
        g.append(f'<ellipse cx="-24" cy="50" rx="11" ry="8" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    elif pose == "shrug":
        g.append(f'<path d="M -30 16 Q -50 4 -46 -14" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M 30 16 Q 50 4 46 -14" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>')
    else:
        g.append(f'<ellipse cx="-24" cy="50" rx="11" ry="8" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
        g.append(f'<ellipse cx="24" cy="50" rx="11" ry="8" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    # head
    g.append(f'<circle cx="0" cy="-24" r="46" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<path d="M -40 -52 L -50 -92 L -10 -66 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
    g.append(f'<path d="M 40 -52 L 50 -92 L 10 -66 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>')
    g.append(f'<path d="M -37 -58 L -43 -80 L -20 -65 Z" fill="{WARM}"/>')
    g.append(f'<path d="M 37 -58 L 43 -80 L 20 -65 Z" fill="{WARM}"/>')
    g.append(f'<circle cx="-32" cy="-12" r="7" fill="{WARM}"/>')
    g.append(f'<circle cx="32" cy="-12" r="7" fill="{WARM}"/>')
    for yy in (-22, -14):
        g.append(f'<line x1="-46" y1="{yy}" x2="-70" y2="{yy-4}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
        g.append(f'<line x1="46" y1="{yy}" x2="70" y2="{yy-4}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    if mood == "surprised":
        g.append(f'<circle cx="-16" cy="-28" r="6.5" fill="{INK}"/><circle cx="16" cy="-28" r="6.5" fill="{INK}"/>')
        g.append(f'<ellipse cx="0" cy="-8" rx="7" ry="9" fill="{INK}"/>')
    elif mood == "happy":
        g.append(f'<path d="M -22 -30 Q -16 -22 -10 -30" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M 10 -30 Q 16 -22 22 -30" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M -10 -8 Q 0 2 10 -8" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == "worried":
        g.append(f'<circle cx="-16" cy="-26" r="5" fill="{INK}"/><circle cx="16" cy="-26" r="5" fill="{INK}"/>')
        g.append(f'<path d="M -10 -4 Q 0 -12 10 -4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == "smug":
        g.append(f'<path d="M -22 -27 L -8 -27" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M 8 -27 L 22 -27" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M -8 -6 Q 4 0 14 -10" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    elif mood == "determined":
        g.append(f'<path d="M -22 -24 L -8 -20" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M 22 -24 L 8 -20" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<circle cx="-14" cy="-14" r="4.5" fill="{INK}"/><circle cx="14" cy="-14" r="4.5" fill="{INK}"/>')
        g.append(f'<path d="M -8 0 L 8 0" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    else:
        g.append(f'<circle cx="-16" cy="-26" r="5.5" fill="{INK}"/><circle cx="16" cy="-26" r="5.5" fill="{INK}"/>')
        g.append(f'<path d="M -8 -6 Q 0 0 8 -6" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def person(cx, cy, s=1.0, color=WARM, mood="neutral", pose="stand", flip=False):
    """Concrete little person with a real (simple) face + limbs — not a bare silhouette."""
    fx = -1 if flip else 1
    g = [f'<g transform="translate({cx},{cy}) scale({fx*s},{s})">']
    # legs
    g.append(f'<path d="M -14 40 L -18 78" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>')
    g.append(f'<path d="M 14 40 L 18 78" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>')
    # body
    g.append(f'<path d="M -28 40 Q -32 -6 0 -12 Q 32 -6 28 40 Z" fill="{color}" stroke="{INK}" stroke-width="4"/>')
    # arms
    if pose == "wave":
        g.append(f'<path d="M -26 4 Q -50 -14 -42 -40" stroke="{color}" stroke-width="12" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M -26 4 Q -50 -14 -42 -40" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>')
        g.append(f'<path d="M 26 4 L 34 30" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M 26 4 L 34 30" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    elif pose == "point":
        g.append(f'<path d="M 24 0 L 60 -18" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 60 -18" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M -24 0 L -30 26" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M -24 0 L -30 26" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    elif pose == "hold":
        g.append(f'<path d="M -24 0 L -6 22" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M -24 0 L -6 22" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 6 22" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 6 22" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M -24 0 L -30 30" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M -24 0 L -30 30" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 30 30" stroke="{color}" stroke-width="12" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 30 30" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    # head
    g.append(f'<circle cx="0" cy="-38" r="26" fill="#fbead9" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<path d="M -26 -46 Q 0 -70 26 -46 Q 26 -58 0 -60 Q -26 -58 -26 -46 Z" fill="{INK}"/>')
    if mood == "happy":
        g.append(f'<path d="M -12 -40 Q -8 -34 -4 -40" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M 4 -40 Q 8 -34 12 -40" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M -8 -26 Q 0 -20 8 -26" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    elif mood == "worried":
        g.append(f'<circle cx="-8" cy="-38" r="3" fill="{INK}"/><circle cx="8" cy="-38" r="3" fill="{INK}"/>')
        g.append(f'<path d="M -8 -22 Q 0 -28 8 -22" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    else:
        g.append(f'<circle cx="-8" cy="-38" r="3" fill="{INK}"/><circle cx="8" cy="-38" r="3" fill="{INK}"/>')
        g.append(f'<path d="M -6 -26 Q 0 -22 6 -26" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def bond_guy(cx, cy, s=1.0, mood="sad", pose="stand"):
    """Personified US-bond IOU character, now with arms & legs so it can act."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    # legs
    g.append(f'<path d="M -14 48 L -16 74" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 14 48 L 16 74" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    # arms
    if pose == "open":
        g.append(f'<path d="M -32 0 L -58 -18" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<path d="M 32 0 L 58 -18" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    elif pose == "cheer":
        g.append(f'<path d="M -30 -6 L -50 -46" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<path d="M 30 -6 L 50 -46" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M -30 6 L -44 30" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<path d="M 30 6 L 44 30" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    # body (the IOU slip)
    g.append(f'<rect x="-34" y="-40" width="68" height="88" rx="6" fill="{PAPER}" stroke="{ACCENT}" stroke-width="4"/>')
    for yy in (-20, -4, 12, 28):
        g.append(f'<line x1="-24" y1="{yy}" x2="24" y2="{yy}" stroke="{ACCENT}" stroke-width="2" opacity="0.5"/>')
    g.append(f'<text x="0" y="-50" font-family="{FONT}" font-weight="900" font-size="18" fill="{ACCENT}" text-anchor="middle">US BOND</text>')
    if mood == "sad":
        g.append(f'<circle cx="-12" cy="-6" r="4" fill="{INK}"/><circle cx="12" cy="-6" r="4" fill="{INK}"/>')
        g.append(f'<path d="M -10 14 Q 0 6 10 14" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M -18 -10 l -6 10 M 18 -10 l 6 10" stroke="{ACCENT}" stroke-width="2.5" stroke-linecap="round"/>')
    elif mood == "happy":
        g.append(f'<path d="M -16 -8 Q -12 -3 -8 -8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M 8 -8 Q 12 -3 16 -8" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M -10 10 Q 0 20 10 10" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M -14 -6 L -6 -6" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M 6 -6 L 14 -6" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
        g.append(f'<path d="M -10 12 Q 0 20 10 12" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def wallet_guy(cx, cy, s=1.0, mood="happy", pose="stand"):
    """Personified stablecoin wallet character, with arms & legs."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<path d="M -12 44 L -14 68" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    g.append(f'<path d="M 12 44 L 14 68" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>')
    if pose == "knock":
        g.append(f'<path d="M 26 0 L 56 -20" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<circle cx="60" cy="-24" r="7" fill="{PAPER}" stroke="{INK}" stroke-width="3.5"/>')
        g.append(f'<path d="M -26 0 L -38 22" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    elif pose == "give":
        g.append(f'<path d="M 24 0 L 56 6" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<path d="M -24 0 L -40 20" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    else:
        g.append(f'<path d="M -24 0 L -38 22" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
        g.append(f'<path d="M 24 0 L 38 22" stroke="{ACCENT}" stroke-width="9" stroke-linecap="round"/>')
    g.append(f'<rect x="-38" y="-30" width="76" height="60" rx="12" fill="{ACCENT}" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<text x="0" y="-38" font-family="{FONT}" font-weight="900" font-size="16" fill="{ACCENT}" text-anchor="middle">USDT/USDC</text>')
    g.append(f'<circle cx="24" cy="0" r="8" fill="{PAPER}" stroke="{INK}" stroke-width="2.5"/>')
    if mood == "happy":
        g.append(f'<circle cx="-12" cy="-6" r="4.5" fill="{PAPER}"/><circle cx="8" cy="-6" r="4.5" fill="{PAPER}"/>')
        g.append(f'<path d="M -14 10 Q -2 18 10 10" fill="none" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>')
    else:
        g.append(f'<circle cx="-12" cy="-6" r="4.5" fill="{PAPER}"/><circle cx="8" cy="-6" r="4.5" fill="{PAPER}"/>')
        g.append(f'<path d="M -12 12 L 6 12" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


def moneybag(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
      <path d="M -26 -10 Q -30 -34 0 -34 Q 30 -34 26 -10 Q 34 30 0 34 Q -34 30 -26 -10 Z" fill="{WARM}" stroke="{INK}" stroke-width="3.5"/>
      <path d="M -10 -34 Q 0 -46 10 -34" fill="none" stroke="{INK}" stroke-width="3.5"/>
      <text x="0" y="10" font-family="{FONT}" font-weight="900" font-size="24" fill="{INK}" text-anchor="middle">$</text>
    </g>'''


def document_icon(cx, cy, s=1.0, stamped=False, label=None):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<rect x="-28" y="-36" width="56" height="72" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="3.5"/>')
    for yy in (-18, -4, 10, 24):
        g.append(f'<line x1="-16" y1="{yy}" x2="16" y2="{yy}" stroke="{INK}" stroke-width="2.5" opacity="0.6"/>')
    if stamped:
        g.append(f'<circle cx="14" cy="16" r="16" fill="none" stroke="{ACCENT}" stroke-width="3.5" transform="rotate(-18 14 16)"/>')
        g.append(f'<text x="14" y="21" font-family="{FONT}" font-weight="900" font-size="13" fill="{ACCENT}" text-anchor="middle" transform="rotate(-18 14 16)">批</text>')
    if label:
        g.append(f'<text x="0" y="-46" font-family="{FONT}" font-weight="700" font-size="16" fill="{ACCENT}" text-anchor="middle">{esc(label)}</text>')
    g.append('</g>')
    return "\n".join(g)


# ---------------- scenery ----------------

def tree(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <rect x="-6" y="0" width="12" height="34" fill="#c9b48a" stroke="{INK}" stroke-width="2.5"/>
    <circle cx="0" cy="-30" r="34" fill="#cdd9a0" stroke="{INK}" stroke-width="3"/>
    </g>'''


def bench(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <rect x="-45" y="-6" width="90" height="10" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
    <rect x="-45" y="-24" width="90" height="10" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
    <line x1="-38" y1="4" x2="-38" y2="26" stroke="{INK}" stroke-width="4"/>
    <line x1="38" y1="4" x2="38" y2="26" stroke="{INK}" stroke-width="4"/>
    </g>'''


def bulletin_board(cx, cy, s=1.0, torn=0):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<rect x="-56" y="-70" width="112" height="140" fill="#efe6d4" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<text x="0" y="-84" font-family="{FONT}" font-weight="900" font-size="20" fill="{INK}" text-anchor="middle">相亲角</text>')
    slots = [(-26,-40),(20,-40),(-26,4),(20,4),(-26,44),(20,44)]
    for i,(dx,dy) in enumerate(slots):
        if i < torn:
            g.append(f'<rect x="{dx-18}" y="{dy-16}" width="36" height="32" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="3,3" opacity="0.4"/>')
        else:
            g.append(f'<rect x="{dx-18}" y="{dy-16}" width="36" height="32" fill="{PAPER}" stroke="{INK}" stroke-width="2.5"/>')
            g.append(f'<circle cx="{dx}" cy="{dy-4}" r="6" fill="none" stroke="{INK}" stroke-width="2"/>')
            g.append(f'<line x1="{dx-8}" y1="{dy+8}" x2="{dx+8}" y2="{dy+8}" stroke="{INK}" stroke-width="2"/>')
    g.append('</g>')
    return "\n".join(g)


def house_door(cx, cy, s=1.0, open_=False):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<rect x="-70" y="-100" width="140" height="140" fill="#efe6d4" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<path d="M -70 -100 L 0 -140 L 70 -100 Z" fill="{ACCENT}" stroke="{INK}" stroke-width="4"/>')
    if open_:
        g.append(f'<rect x="-32" y="-70" width="60" height="70" fill="{INK}" opacity="0.85"/>')
    else:
        g.append(f'<rect x="-32" y="-70" width="60" height="70" fill="#8a6a4a" stroke="{INK}" stroke-width="3.5"/>')
        g.append(f'<circle cx="18" cy="-35" r="4" fill="{INK}"/>')
    g.append('</g>')
    return "\n".join(g)


def government_building(cx, cy, s=1.0):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<rect x="-110" y="-10" width="220" height="70" fill="#efe6d4" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<polygon points="-120,-10 0,-70 120,-10" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>')
    for x in (-80,-40,0,40,80):
        g.append(f'<rect x="{x-8}" y="-4" width="16" height="58" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>')
    g.append(f'<rect x="-6" y="-96" width="4" height="30" fill="{INK}"/>')
    g.append(f'<path d="M -2 -96 L 30 -88 L -2 -80 Z" fill="{ACCENT}"/>')
    g.append(f'<text x="0" y="-24" font-family="{FONT}" font-weight="900" font-size="18" fill="{INK}" text-anchor="middle">登记处</text>')
    g.append('</g>')
    return "\n".join(g)


def vault(cx, cy, s=1.0, open_=True):
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<rect x="-70" y="-70" width="140" height="140" rx="10" fill="#efe6d4" stroke="{INK}" stroke-width="5"/>')
    if open_:
        g.append(f'<rect x="-50" y="-50" width="100" height="100" rx="6" fill="{INK}" opacity="0.08"/>')
        g.append(moneybag(-18, 10, 0.7))
        g.append(document_icon(24, 6, 0.55))
    g.append(f'<circle cx="{-40 if open_ else 0}" cy="0" r="16" fill="none" stroke="{INK}" stroke-width="4"/>')
    g.append('</g>')
    return "\n".join(g)


def store_shelf(px, py, pw, ph):
    g = [f'<g>']
    shelf_y = py + ph*0.28
    g.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph*0.42}" fill="#efe6d4" stroke="{INK}" stroke-width="2.5" opacity="0.7"/>')
    n = 5
    cell_w = (pw-40)/n
    for i in range(n):
        x = px + 20 + i*cell_w
        g.append(f'<rect x="{x}" y="{py+10}" width="{cell_w-8}" height="{ph*0.42-20}" fill="{PAPER}" stroke="{INK}" stroke-width="2" opacity="0.8"/>')
    g.append(f'<line x1="{px}" y1="{shelf_y}" x2="{px+pw}" y2="{shelf_y}" stroke="{INK}" stroke-width="2" opacity="0.4"/>')
    g.append('</g>')
    return "".join(g)


def counter(cx, cy, s=1.0):
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <rect x="-90" y="0" width="180" height="46" fill="#d8c9a8" stroke="{INK}" stroke-width="4"/>
    <rect x="-70" y="-30" width="50" height="32" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
    </g>'''


def world_blob(cx, cy, r=90):
    return f'''<g>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#dfe6cf" stroke="{INK}" stroke-width="3.5"/>
    <path d="M {cx-r*0.5} {cy-r*0.6} Q {cx-r*0.1} {cy-r*0.9} {cx+r*0.4} {cy-r*0.5} Q {cx+r*0.6} {cy-r*0.1} {cx+r*0.3} {cy+r*0.3} Q {cx-r*0.2} {cy+r*0.7} {cx-r*0.6} {cy+r*0.2} Z" fill="#b7c98f" opacity="0.8"/>
    <ellipse cx="{cx-r*0.5}" cy="{cy+r*0.2}" rx="{r*0.3}" ry="{r*0.5}" fill="#b7c98f" opacity="0.8"/>
    </g>'''


def pool(cx, cy, rx=140, ry=70):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#d9e6ec" stroke="{ACCENT}" stroke-width="4" stroke-dasharray="10,6"/>'


def red_thread(x1, y1, x2, y2, sag=30):
    mx, my = (x1+x2)/2, (y1+y2)/2 + sag
    return f'<path d="M {x1} {y1} Q {mx} {my} {x2} {y2}" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-dasharray="2,6" stroke-linecap="round"/>'


def stamp_mark(cx, cy, text="XT", s=1.0, color=ACCENT):
    """Small square 'artist signature' mark, bottom-right corner convention
    for the 单图语录体 mode — gives cross-post recognizability the way a
    real cartoonist's chop does."""
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <rect x="-22" y="-22" width="44" height="44" fill="{color}"/>
    <text x="0" y="9" font-family="{FONT}" font-weight="900" font-size="22" fill="{PAPER}" text-anchor="middle">{esc(text)}</text>
    </g>'''


def build_quote_svg(image_content, caption_lines, signature="XT", width=900, height=1200,
                     image_ratio=0.62, bg=PAPER):
    """Canvas builder for the 单图语录体 mode: ONE image area (plain background,
    single centered subject, no scene furniture) + a caption block below it.
    caption_lines: list of strings, 2-3 short lines, rendered large and centered —
    the caption IS the whole joke, there is no separate title/subtitle split here."""
    img_h = height * image_ratio
    body = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    body.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{bg}"/>')
    body.append(f'<g>{image_content}</g>')
    body.append(stamp_mark(width - 60, img_h - 40, signature, 1.0))
    n = len(caption_lines)
    size = 46 if n <= 2 else 40
    line_h = size * 1.5
    total_h = line_h * n
    start_y = img_h + (height - img_h) / 2 - total_h / 2 + size
    for i, line in enumerate(caption_lines):
        y = start_y + i * line_h
        body.append(f'<text x="{width/2}" y="{y}" font-family="{FONT}" font-weight="900" '
                     f'font-size="{size}" fill="{INK}" text-anchor="middle">{esc(line)}</text>')
    body.append('</svg>')
    return "\n".join(body)


def blanket_burrito(cx, cy, s=1.0):
    """Mode-B prop: a person wrapped up in a blanket like a burrito, only a
    sleepy squinting face peeking out. Reusable for any 'exhausted but still
    doing X' daily-life quote card."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<ellipse cx="0" cy="30" rx="150" ry="95" fill="#c9b8e0" stroke="{INK}" stroke-width="5"/>')
    for x in (-90, -40, 20, 80):
        g.append(f'<path d="M {x} -55 Q {x+20} 30 {x} 105" fill="none" stroke="{INK}" stroke-width="2" opacity="0.35"/>')
    g.append(f'<circle cx="-30" cy="-30" r="52" fill="#fbead9" stroke="{INK}" stroke-width="5"/>')
    g.append(f'<path d="M -30 -78 Q -80 -85 -80 -30 Q -80 -50 -30 -78 Z" fill="{INK}"/>')
    g.append(f'<path d="M -52 -32 Q -46 -26 -40 -32" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    g.append(f'<path d="M -22 -32 Q -16 -26 -10 -32" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    g.append(f'<circle cx="-14" cy="-8" r="10" fill="{ACCENT}" opacity="0.35"/>')
    g.append(f'<circle cx="-46" cy="-8" r="10" fill="{ACCENT}" opacity="0.35"/>')
    g.append(f'<text x="20" y="-70" font-family="{FONT}" font-weight="700" font-size="26" fill="{INK}" opacity="0.6">Z z z</text>')
    g.append('</g>')
    return "\n".join(g)


def phone_glow_hand(cx, cy, s=1.0, flip=False):
    """Mode-B prop: an arm emerging (from a blanket, desk, etc.) holding a
    glowing phone, with an exaggerated 'energetic' scrolling finger — the
    visual joke of one body part refusing to be as tired as the rest."""
    fx = -1 if flip else 1
    g = [f'<g transform="translate({cx},{cy}) scale({fx*s},{s})">']
    for r, op in ((95, 0.15), (75, 0.22), (55, 0.3)):
        g.append(f'<circle cx="0" cy="0" r="{r}" fill="{WARM}" opacity="{op}"/>')
    g.append(f'<path d="M -55 75 Q -30 15 -10 10" fill="none" stroke="#fbead9" stroke-width="34" stroke-linecap="round"/>')
    g.append(f'<path d="M -55 75 Q -30 15 -10 10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    g.append(f'<rect x="-38" y="-58" width="56" height="100" rx="10" fill="{INK}"/>')
    g.append(f'<rect x="-32" y="-50" width="44" height="84" fill="{WARM}"/>')
    g.append(f'<ellipse cx="14" cy="4" rx="9" ry="13" fill="#fbead9" stroke="{INK}" stroke-width="3.5"/>')
    g.append(f'<rect x="7" y="-6" width="14" height="7" rx="3" fill="{ACCENT}"/>')
    g.append(f'<path d="M 14 -20 l -6 -8 M 14 -20 l 6 -8 M 14 -20 l 0 -10" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    for i, dx in enumerate((30, 40, 50)):
        g.append(f'<line x1="{dx}" y1="{-10+i*3}" x2="{dx+16}" y2="{-16+i*3}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>')
    g.append('</g>')
    return "\n".join(g)


def cross_out(cx, cy, r=34):
    return f'<line x1="{cx-r}" y1="{cy-r}" x2="{cx+r}" y2="{cy+r}" stroke="{ACCENT}" stroke-width="7" stroke-linecap="round"/><line x1="{cx-r}" y1="{cy+r}" x2="{cx+r}" y2="{cy-r}" stroke="{ACCENT}" stroke-width="7" stroke-linecap="round"/>'


def check_mark(cx, cy, r=34):
    return f'<path d="M {cx-r} {cy} L {cx-r*0.2} {cy+r*0.8} L {cx+r} {cy-r*0.7}" fill="none" stroke="{ACCENT}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'


def scale_icon(cx, cy, left_label="", right_label=""):
    g = [f'<g transform="translate({cx},{cy})">']
    g.append(f'<line x1="0" y1="-40" x2="0" y2="30" stroke="{INK}" stroke-width="4"/>')
    g.append(f'<line x1="-50" y1="-30" x2="50" y2="-30" stroke="{INK}" stroke-width="4"/>')
    for side, lab in ((-1, left_label), (1, right_label)):
        lx = side*50
        g.append(f'<line x1="{lx}" y1="-30" x2="{lx}" y2="-10" stroke="{INK}" stroke-width="2.5"/>')
        g.append(f'<path d="M {lx-22} -10 Q {lx} 8 {lx+22} -10 Z" fill="none" stroke="{INK}" stroke-width="3"/>')
        if lab:
            g.append(f'<text x="{lx}" y="2" font-family="{FONT}" font-weight="700" font-size="20" fill="{ACCENT}" text-anchor="middle">{esc(lab)}</text>')
    g.append(f'<rect x="-22" y="30" width="44" height="8" fill="{INK}"/>')
    g.append('</g>')
    return "\n".join(g)


def build_svg(panels, bg=True):
    body = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    body.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>')
    for i, p in enumerate(panels):
        py = PANEL1_Y if i == 0 else PANEL2_Y
        title_h = PANEL_H * TITLE_H_RATIO
        illus_y = py + title_h
        illus_h = PANEL_H - title_h
        body.append(panel_frame(MARGIN, py, PANEL_W, PANEL_H))
        clip_id = f"clip{i}_{id(p)}"
        body.append(f'<clipPath id="{clip_id}"><rect x="{MARGIN}" y="{illus_y}" width="{PANEL_W}" height="{illus_h}"/></clipPath>')
        if bg and p.get("bg", True):
            body.append(f'<g clip-path="url(#{clip_id})">{scene_bg(MARGIN, illus_y, PANEL_W, illus_h)}</g>')
        body.append(f'<g clip-path="url(#{clip_id})">{p["content"]}</g>')
        body.append(title_block(p["title"], MARGIN, py, PANEL_W, title_h, caption=p.get("caption")))
        body.append(f'<line x1="{MARGIN+24}" y1="{illus_y}" x2="{MARGIN+PANEL_W-24}" y2="{illus_y}" stroke="{INK}" stroke-width="1.5" opacity="0.25"/>')
    body.append('</svg>')
    return "\n".join(body)
