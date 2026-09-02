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


def stamp_mark(cx, cy, text="ESK", s=1.0, color=ACCENT):
    """Small square 'artist signature' mark, bottom-right corner convention
    for the 单图语录体 mode — gives cross-post recognizability the way a
    real cartoonist's chop does."""
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <rect x="-22" y="-22" width="44" height="44" fill="{color}"/>
    <text x="0" y="9" font-family="{FONT}" font-weight="900" font-size="22" fill="{PAPER}" text-anchor="middle">{esc(text)}</text>
    </g>'''


def build_quote_svg(image_content, caption_lines, signature="ESK", width=900, height=1200,
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
    """Mode-B prop: a person wrapped up in a blanket like a burrito, drawn
    with warm, conventional 'fast asleep' cartoon cues — simple downturned
    lash-lines, rosy cheeks, a tilted head, and a classic sleep-bubble from
    the nose — deliberately avoiding surreal/uncanny details (no dangling
    objects on the face). Reusable for any 'exhausted but still doing X'
    daily-life quote card."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    g.append(f'<ellipse cx="0" cy="30" rx="150" ry="95" fill="#c9b8e0" stroke="{INK}" stroke-width="5"/>')
    for x in (-90, -40, 20, 80):
        g.append(f'<path d="M {x} -55 Q {x+20} 30 {x} 105" fill="none" stroke="{INK}" stroke-width="2" opacity="0.35"/>')
    # head, gently tilted and resting into the collar
    g.append('<g transform="translate(-30,-24) rotate(8)">')
    g.append(f'<circle cx="0" cy="0" r="52" fill="#fbead9" stroke="{INK}" stroke-width="5"/>')
    g.append(f'<path d="M 0 -48 Q -50 -55 -50 0 Q -50 -20 0 -48 Z" fill="{INK}"/>')
    # cheeks (drawn before eyes so blush sits low, not overlapping)
    g.append(f'<circle cx="-26" cy="18" r="9" fill="{ACCENT}" opacity="0.28"/>')
    g.append(f'<circle cx="16" cy="18" r="9" fill="{ACCENT}" opacity="0.28"/>')
    # simple, warm downturned sleepy eyes — one soft curved lash-line each,
    # no extra objects hanging off them
    g.append(f'<path d="M -40 0 Q -28 8 -16 2" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>')
    g.append(f'<path d="M 12 2 Q 24 10 36 3" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>')
    g.append(f'<path d="M -40 0 l -4 5 M -16 2 l 4 4" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    g.append(f'<path d="M 12 2 l -4 5 M 36 3 l 4 4" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>')
    # small content smile — asleep, not distressed
    g.append(f'<path d="M -6 26 Q -1 30 4 26" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
    g.append('</g>')
    # classic cartoon 'sleep bubble' chain drifting up and clear of the blanket collar
    g.append(f'<circle cx="20" cy="-58" r="5" fill="#dce8f0" stroke="{INK}" stroke-width="2" opacity="0.85"/>')
    g.append(f'<circle cx="34" cy="-78" r="8" fill="#dce8f0" stroke="{INK}" stroke-width="2" opacity="0.85"/>')
    g.append(f'<circle cx="54" cy="-104" r="15" fill="#dce8f0" stroke="{INK}" stroke-width="2.5" opacity="0.85"/>')
    g.append(f'<ellipse cx="49" cy="-109" rx="4" ry="6" fill="white" opacity="0.7"/>')
    g.append(f'<text x="88" y="-118" font-family="{FONT}" font-weight="700" font-size="26" fill="{INK}" opacity="0.55">Z z z</text>')
    g.append('</g>')
    return "\n".join(g)


def lying_phone_scene(cx, cy, s=1.0):
    """Mode-B prop: a person lying on their back in bed, blanket draped over
    the body (not wrapped like a cocoon), BOTH arms bent at a visible elbow
    (not tall smooth loops — that reads as 'hanging', not 'lying down')
    holding a glowing phone close above the face. Eyes open and fixed on the
    screen but heavy-lidded and tired (dark circles, strained brows) — awake
    and scrolling, not asleep. Reusable for any 'exhausted but still on the
    phone' daily-life card."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    # pillow
    g.append(f'<ellipse cx="0" cy="40" rx="175" ry="78" fill="#dfe6ee" stroke="{INK}" stroke-width="4"/>')
    # body + blanket, viewed from above, tapering down and off the bottom of frame
    g.append('<path d="M -135 30 Q -165 190 -95 300 L 95 300 Q 165 190 135 30 '
              'Q 70 55 0 55 Q -70 55 -135 30 Z" '
              f'fill="#c9b8e0" stroke="{INK}" stroke-width="5"/>')
    for x, sway in ((-70, -10), (-20, 8), (30, -6), (80, 10)):
        g.append(f'<path d="M {x} 60 Q {x+sway} 170 {x} 280" fill="none" stroke="{INK}" stroke-width="2" opacity="0.3"/>')
    # arms — TWO straight segments each (upper arm + forearm) with a visible
    # elbow bend resting near the pillow, not a tall smooth loop
    for side in (-1, 1):
        sx, sy = side*85, 35        # shoulder, at the blanket edge
        ex, ey = side*128, -30      # elbow, resting out near the pillow
        hx, hy = side*42, -112      # hand, up near the phone
        g.append(f'<path d="M {sx} {sy} L {ex} {ey} L {hx} {hy}" fill="none" '
                  f'stroke="#c9b8e0" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<path d="M {sx} {sy} L {ex} {ey} L {hx} {hy}" fill="none" '
                  f'stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<ellipse cx="{hx}" cy="{hy}" rx="15" ry="12" fill="#fbead9" stroke="{INK}" stroke-width="4"/>')
    # head, resting on the pillow, face looking straight up at the phone
    g.append(f'<circle cx="0" cy="0" r="72" fill="#fbead9" stroke="{INK}" stroke-width="5"/>')
    g.append(f'<path d="M -68 -10 Q -60 -62 0 -62 Q 60 -62 68 -10 Q 30 -40 0 -40 Q -30 -40 -68 -10 Z" fill="{INK}"/>')
    g.append(f'<ellipse cx="-26" cy="6" rx="17" ry="10" fill="#9c8bb8" opacity="0.35"/>')
    g.append(f'<ellipse cx="26" cy="6" rx="17" ry="10" fill="#9c8bb8" opacity="0.35"/>')
    g.append(f'<path d="M -40 -14 Q -26 -20 -12 -13" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    g.append(f'<path d="M 12 -13 Q 26 -20 40 -14" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')
    for ex in (-26, 26):
        g.append(f'<ellipse cx="{ex}" cy="8" rx="15" ry="11" fill="white" stroke="{INK}" stroke-width="3.5"/>')
        g.append(f'<circle cx="{ex}" cy="10" r="6.5" fill="{INK}"/>')
        g.append(f'<circle cx="{ex+2}" cy="8" r="1.8" fill="white"/>')
        g.append(f'<path d="M {ex-15} 2 Q {ex} -4 {ex+15} 2" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>')
    g.append(f'<path d="M -4 20 Q 0 26 4 20" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" opacity="0.6"/>')
    g.append(f'<path d="M -10 42 L 10 42" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
    g.append(f'<circle cx="-38" cy="28" r="8" fill="{ACCENT}" opacity="0.25"/>')
    g.append(f'<circle cx="38" cy="28" r="8" fill="{ACCENT}" opacity="0.25"/>')
    g.append(f'<path d="M 58 -30 Q 64 -18 58 -10 Q 52 -18 58 -30 Z" fill="#bcd8ea" stroke="{INK}" stroke-width="2"/>')
    # phone, held close above the face (between the two hands drawn above)
    px, py = 0, -150
    for r, op in ((78, 0.14), (58, 0.2), (40, 0.28)):
        g.append(f'<circle cx="{px}" cy="{py+20}" r="{r}" fill="{WARM}" opacity="{op}"/>')
    g.append(f'<rect x="{px-32}" y="{py-52}" width="64" height="108" rx="11" fill="{INK}"/>')
    g.append(f'<rect x="{px-26}" y="{py-44}" width="52" height="92" fill="{WARM}"/>')
    g.append(f'<circle cx="{px}" cy="{py-38}" r="3" fill="{INK}" opacity="0.6"/>')
    for dy in (-10, 8, 26):
        g.append(f'<line x1="{px-40}" y1="{py+dy}" x2="{px-54}" y2="{py+dy-5}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" opacity="0.55"/>')
        g.append(f'<line x1="{px+40}" y1="{py+dy}" x2="{px+54}" y2="{py+dy-5}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" opacity="0.55"/>')
    g.append('</g>')
    return "\n".join(g)


def phone_overhead(cx, cy, s=1.0):
    """Mode-B prop: a glowing phone held overhead with both hands (pair with
    lying_phone_scene), screen facing down so its light spills onto the face
    below."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    for r, op in ((110, 0.12), (85, 0.18), (60, 0.26)):
        g.append(f'<circle cx="0" cy="30" r="{r}" fill="{WARM}" opacity="{op}"/>')
    g.append(f'<rect x="-44" y="-70" width="88" height="150" rx="14" fill="{INK}"/>')
    g.append(f'<rect x="-36" y="-60" width="72" height="128" fill="{WARM}"/>')
    g.append(f'<circle cx="0" cy="-52" r="4" fill="{INK}" opacity="0.6"/>')
    for i, dy in enumerate((-10, 10, 30)):
        g.append(f'<line x1="{-55}" y1="{dy}" x2="{-72}" y2="{dy-6}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" opacity="0.55"/>')
        g.append(f'<line x1="{55}" y1="{dy}" x2="{72}" y2="{dy-6}" stroke="{INK}" stroke-width="2.5" stroke-linecap="round" opacity="0.55"/>')
    g.append('</g>')
    return "\n".join(g)


def bedroom_phone_scene(px, py, pw, ph):
    """Mode-B 'grounded scene' variant: fills the WHOLE image area with a
    moody night bedroom (wall, picture frame, nightstand + glowing lamp,
    a real bed with headboard and blanket) and a simple round-headed
    character sitting up, ONE hand holding a phone at chest height, with
    genuinely tired half-lidded eyes and a single tear/sweat drop. Use this
    instead of a plain-background single subject when the feeling calls for
    a real, atmospheric setting rather than an isolated icon — pass the
    full image-area rectangle (px, py, pw, ph)."""
    g = [f'<g transform="translate({px},{py})">']
    # wall
    g.append(f'<rect x="0" y="0" width="{pw}" height="{ph}" fill="#4a3436"/>')
    g.append(f'<rect x="0" y="{ph*0.7}" width="{pw}" height="{ph*0.3}" fill="#3a2a2c"/>')
    # nightstand + glowing lamp
    nx, ny = pw*0.05, ph*0.56
    for r, op in ((120, 0.10), (85, 0.16), (55, 0.24)):
        g.append(f'<circle cx="{nx+55}" cy="{ny-70}" r="{r}" fill="#f2c76b" opacity="{op}"/>')
    g.append(f'<rect x="{nx}" y="{ny}" width="115" height="{ph-ny}" fill="#5a3d2e" stroke="#2e2022" stroke-width="3"/>')
    g.append(f'<rect x="{nx+8}" y="{ny+18}" width="99" height="6" fill="#2e2022" opacity="0.4"/>')
    g.append(f'<path d="M {nx+35} {ny-70} L {nx+75} {ny-70} L {nx+65} {ny-20} L {nx+45} {ny-20} Z" fill="#f2c76b" stroke="#8a6a2a" stroke-width="2"/>')
    g.append(f'<rect x="{nx+50}" y="{ny-20}" width="10" height="20" fill="#3a2a1a"/>')
    # bed headboard
    hx0, hx1 = pw*0.16, pw*0.98
    g.append(f'<path d="M {hx0} {ph*0.62} L {hx0} {ph*0.22} Q {(hx0+hx1)/2} {ph*0.06} {hx1} {ph*0.22} L {hx1} {ph*0.62} Z" '
              f'fill="#6b4a36" stroke="#2e2022" stroke-width="4"/>')
    g.append(f'<path d="M {hx0+18} {ph*0.60} L {hx0+18} {ph*0.26} Q {(hx0+hx1)/2} {ph*0.13} {hx1-18} {ph*0.26} L {hx1-18} {ph*0.60} Z" '
              f'fill="none" stroke="#8a6a4a" stroke-width="3"/>')
    g.append(f'<ellipse cx="{(hx0+hx1)/2}" cy="{ph*0.14}" rx="10" ry="16" fill="#2e2022"/>')
    # blanket, draped over the lower body
    g.append(f'<path d="M {pw*0.22} {ph*0.62} Q {pw*0.2} {ph*0.85} {pw*0.3} {ph} L {pw*0.92} {ph} '
              f'Q {pw*0.98} {ph*0.8} {pw*0.9} {ph*0.6} Q {pw*0.6} {ph*0.72} {pw*0.22} {ph*0.62} Z" '
              f'fill="#8b98ab" stroke="#2e2022" stroke-width="4"/>')
    for fx2, fy2 in ((pw*0.4, ph*0.75), (pw*0.55, ph*0.8), (pw*0.7, ph*0.76)):
        g.append(f'<path d="M {fx2} {fy2} Q {fx2+20} {fy2+40} {fx2-10} {fy2+80}" fill="none" stroke="{INK}" stroke-width="2" opacity="0.2"/>')
    # character — simple round cream head+body sitting up against the headboard
    ccx, ccy, r = pw*0.54, ph*0.53, 155
    g.append(f'<circle cx="{ccx}" cy="{ccy}" r="{r}" fill="#f7f1e6" stroke="{INK}" stroke-width="5"/>')
    # arm + hand holding the phone at chest height (ONE hand, natural, clear of the face)
    sx, sy = ccx+r*0.55, ccy+r*0.75
    ex2, ey2 = ccx+r*1.05, ccy+r*0.55
    phx, phy = ccx+r*0.62, ccy+r*0.32
    g.append(f'<path d="M {sx} {sy} L {ex2} {ey2} L {phx} {phy}" '
              f'fill="none" stroke="#f7f1e6" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append(f'<path d="M {sx} {sy} L {ex2} {ey2} L {phx} {phy}" '
              f'fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
    for rr, op in ((60, 0.18), (42, 0.28)):
        g.append(f'<circle cx="{phx}" cy="{phy}" r="{rr}" fill="{WARM}" opacity="{op}"/>')
    g.append(f'<rect x="{phx-24}" y="{phy-34}" width="48" height="76" rx="9" fill="{INK}"/>')
    g.append(f'<rect x="{phx-18}" y="{phy-27}" width="36" height="62" fill="{WARM}"/>')
    # second arm — resting relaxed on the blanket, so the character has both arms
    rsx, rsy = ccx-r*0.55, ccy+r*0.7
    rex, rey = ccx-r*0.95, ccy+r*1.0
    rhx, rhy = ccx-r*0.65, ccy+r*1.25
    g.append(f'<path d="M {rsx} {rsy} L {rex} {rey} L {rhx} {rhy}" '
              f'fill="none" stroke="#f7f1e6" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append(f'<path d="M {rsx} {rsy} L {rex} {rey} L {rhx} {rhy}" '
              f'fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append(f'<ellipse cx="{rhx}" cy="{rhy}" rx="17" ry="14" fill="#f7f1e6" stroke="{INK}" stroke-width="4.5"/>')
    # tired droopy eyes with lash-line, plus one tear/sweat drop
    ex1, ex2, ey = ccx-r*0.27, ccx+r*0.15, ccy-r*0.12
    g.append(f'<path d="M {ex1-16} {ey} Q {ex1} {ey+9} {ex1+16} {ey}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<path d="M {ex2-16} {ey+2} Q {ex2} {ey+11} {ex2+16} {ey+2}" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    g.append(f'<circle cx="{ex1}" cy="{ey+5}" r="3" fill="{INK}"/>')
    g.append(f'<circle cx="{ex2}" cy="{ey+7}" r="3" fill="{INK}"/>')
    g.append(f'<path d="M {ex1-6} {ey+14} Q {ex1-9} {ey+30} {ex1-4} {ey+40} Q {ex1+1} {ey+30} {ex1-6} {ey+14} Z" '
              f'fill="#bcd8ea" stroke="{INK}" stroke-width="2"/>')
    # cheeks + small tired open mouth
    g.append(f'<circle cx="{ccx-46}" cy="{ccy+22}" r="13" fill="{ACCENT}" opacity="0.25"/>')
    g.append(f'<circle cx="{ccx+34}" cy="{ccy+24}" r="13" fill="{ACCENT}" opacity="0.25"/>')
    g.append(f'<ellipse cx="{ccx-10}" cy="{ccy+46}" rx="9" ry="7" fill="{INK}" opacity="0.7"/>')
    g.append('</g>')
    return "\n".join(g)


def outlined_text(cx, cy, text, size=42, fill="white", stroke=None, weight="900"):
    stroke = stroke or INK
    return (f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-weight="{weight}" font-size="{size}" '
            f'fill="none" stroke="{stroke}" stroke-width="{size*0.18}" stroke-linejoin="round" '
            f'text-anchor="middle">{esc(text)}</text>'
            f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-weight="{weight}" font-size="{size}" '
            f'fill="{fill}" text-anchor="middle">{esc(text)}</text>')


def build_scene_card_svg(scene_content, top_lines=None, bottom_lines=None,
                          signature="ESK", width=720, height=1200):
    """Full-bleed 'grounded scene' card for mode B: the illustration fills
    the ENTIRE canvas (a real environment — bedroom, kitchen, office —
    rather than a plain background), with bold white outlined text overlaid
    directly on the image near the top and/or bottom, meme-poster style.
    Use this instead of build_quote_svg when the feeling calls for a real
    atmospheric setting instead of an isolated subject on plain background."""
    body = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    body.append(f'<g>{scene_content}</g>')
    if top_lines:
        for i, line in enumerate(top_lines):
            body.append(outlined_text(width/2, 90 + i*54, line, size=42))
    if bottom_lines:
        n = len(bottom_lines)
        for i, line in enumerate(bottom_lines):
            body.append(outlined_text(width/2, height - 60 - (n-1-i)*54, line, size=42))
    body.append(stamp_mark(width - 50, height - 50, signature, 0.85))
    body.append('</svg>')
    return "\n".join(body)


def soft_defs():
    """A few soft radial gradients, injected once per SVG, used to push
    cheek/skin shading a little toward hand-painted softness instead of flat
    fills — the practical ceiling for what plain SVG paths can approximate
    of real marker/colored-pencil shading."""
    return f'''<defs>
    <radialGradient id="blushGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{ACCENT}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="skinShade" cx="45%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fff6ea" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#f3d9b8" stop-opacity="0.4"/>
    </radialGradient>
    </defs>'''


def hatch_fill(x, y, w, h, n=8, color=None, opacity=0.5):
    """A handful of slightly uneven parallel lines — the cheap SVG
    approximation of the sketchy hand-drawn hatching seen in marker
    illustration (e.g. a stack of paper). Not a substitute for real
    hand-drawn texture, just closer than a flat rect."""
    color = color or INK
    import random
    rnd = random.Random(int(x*7+y*13))
    lines = []
    for i in range(n):
        yy = y + h*i/(n-1)
        jitter1 = rnd.uniform(-4, 4)
        jitter2 = rnd.uniform(-4, 4)
        lines.append(f'<line x1="{x}" y1="{yy+jitter1}" x2="{x+w}" y2="{yy+jitter2}" '
                      f'stroke="{color}" stroke-width="1.6" opacity="{opacity}"/>')
    return "".join(lines)


def worker_face(cx, cy, s=1.0, mood="neutral", glasses=True, tilt=0):
    """Just the face (used internally by worker_figure, and directly for
    close-up reaction shots like the fourth-wall-break card)."""
    g = [f'<g transform="translate({cx},{cy}) scale({s}) rotate({tilt})">']
    g.append(f'<circle cx="0" cy="0" r="70" fill="url(#skinShade)" stroke="{INK}" stroke-width="4.5"/>')
    g.append(f'<circle cx="0" cy="0" r="70" fill="none" stroke="{INK}" stroke-width="4.5"/>')
    g.append(f'<path d="M -60 -18 Q -58 -55 -10 -62 Q 30 -66 55 -40 Q 20 -48 -10 -44 Q -40 -40 -60 -18 Z" fill="{INK}"/>')
    g.append(f'<circle cx="-46" cy="30" r="15" fill="url(#blushGrad)"/>')
    g.append(f'<circle cx="42" cy="32" r="15" fill="url(#blushGrad)"/>')
    if glasses:
        g.append(f'<circle cx="-22" cy="2" r="17" fill="none" stroke="{INK}" stroke-width="3"/>')
        g.append(f'<circle cx="24" cy="2" r="17" fill="none" stroke="{INK}" stroke-width="3"/>')
        g.append(f'<line x1="-5" y1="0" x2="5" y2="0" stroke="{INK}" stroke-width="3"/>')
        g.append(f'<line x1="-39" y1="-2" x2="-52" y2="-8" stroke="{INK}" stroke-width="3"/>')
        g.append(f'<line x1="41" y1="-2" x2="54" y2="-8" stroke="{INK}" stroke-width="3"/>')
    if mood == "tired":
        g.append(f'<path d="M -30 -14 Q -22 -20 -14 -14" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
        g.append(f'<path d="M 12 -14 Q 20 -20 28 -14" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
        g.append(f'<circle cx="-22" cy="4" r="3.5" fill="{INK}"/>')
        g.append(f'<circle cx="24" cy="4" r="3.5" fill="{INK}"/>')
        g.append(f'<path d="M -12 38 Q 0 32 12 38" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    elif mood == "happy":
        g.append(f'<path d="M -30 -6 Q -22 -14 -14 -6" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
        g.append(f'<path d="M 12 -6 Q 20 -14 28 -6" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
        g.append(f'<path d="M -14 34 Q 0 46 14 34" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>')
    elif mood == "wide_eyed":
        g.append(f'<circle cx="-22" cy="2" r="5" fill="{INK}"/>')
        g.append(f'<circle cx="24" cy="2" r="5" fill="{INK}"/>')
        g.append(f'<path d="M -8 36 Q 0 30 8 36" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    else:
        g.append(f'<circle cx="-22" cy="4" r="3.5" fill="{INK}"/>')
        g.append(f'<circle cx="24" cy="4" r="3.5" fill="{INK}"/>')
        g.append(f'<path d="M -10 36 L 10 36" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    g.append('</g>')
    return "\n".join(g)


# kept for backward compatibility — same as worker_face
worker_head = worker_face


def worker_figure(cx, cy, s=1.0, mood="neutral", pose="stand", glasses=True, hold=None):
    """Full 打工人 figure — head + torso + arms + legs — with a pose
    vocabulary so the body actually changes with what the quote describes,
    instead of reusing a floating head for every card. pose: stand/run/
    push/lie/slump/reach/sip/carry/point/wave. hold: optional inline SVG
    snippet (already positioned in LOCAL coords near the right hand,
    roughly around (55,20)) for a held prop that should move with the arm,
    e.g. a cup or a card — simplest way to attach a prop is to draw it
    separately at the hand coordinates this function documents per pose."""
    g = [f'<g transform="translate({cx},{cy}) scale({s})">']
    shirt = "#8fa3b5"
    pants = "#4a4a52"
    if pose == "lie":
        # lying on the back, legs kicking, arms flailing — for "struggling in bed"
        g.append(f'<ellipse cx="30" cy="70" rx="95" ry="42" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M 90 55 L 150 20" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 100 90 L 165 100" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -40 45 L -95 10" stroke="{shirt}" stroke-width="14" stroke-linecap="round"/>')
        g.append(f'<path d="M -30 90 L -85 115" stroke="{shirt}" stroke-width="14" stroke-linecap="round"/>')
        g.append(worker_face(-55, 20, 0.85, mood, glasses))
    elif pose == "run":
        g.append(f'<path d="M -20 -10 L 30 55 L 10 130" fill="none" stroke="{shirt}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<path d="M 10 130 L -20 165" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 5 100 L 55 150" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 15 20 L -45 -10" stroke="{shirt}" stroke-width="14" stroke-linecap="round"/>')
        g.append(f'<path d="M 20 50 L 75 30" stroke="{shirt}" stroke-width="14" stroke-linecap="round"/>')
        g.append(worker_face(0, -55, 0.85, mood, glasses, tilt=-8))
    elif pose == "push":
        g.append(f'<path d="M -10 -20 L 10 60 L -10 150" fill="none" stroke="{pants}" stroke-width="36" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<path d="M -10 150 L -50 195" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -10 150 L 35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 5 10 L 60 -15" stroke="{shirt}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 5 40 L 60 20" stroke="{shirt}" stroke-width="16" stroke-linecap="round"/>')
        g.append(worker_face(-30, -55, 0.85, mood, glasses, tilt=18))
    elif pose == "slump":
        g.append(f'<ellipse cx="0" cy="70" rx="80" ry="55" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -50 40 L -90 90" stroke="{shirt}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 50 40 L 30 100" stroke="{shirt}" stroke-width="16" stroke-linecap="round"/>')
        g.append(worker_face(20, -35, 0.85, mood, glasses, tilt=20))
    elif pose == "reach":
        g.append(f'<rect x="-45" y="10" width="90" height="120" rx="20" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -30 110 L -40 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 30 110 L 40 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -35 30 L -70 65" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<path d="M 35 20 L 90 -30" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(worker_face(0, -50, 0.9, mood, glasses))
    elif pose == "sip":
        g.append(f'<rect x="-42" y="15" width="84" height="115" rx="18" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -25 115 L -35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 25 115 L 35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -35 35 L -65 75" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<path d="M 35 30 L 60 -10" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(worker_face(0, -45, 0.9, mood, glasses))
    elif pose == "wave":
        g.append(f'<rect x="-42" y="15" width="84" height="115" rx="18" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -25 115 L -35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 25 115 L 35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -35 35 L -70 -5" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<path d="M 35 35 L 70 -5" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(worker_face(0, -45, 0.9, mood, glasses))
    elif pose == "point":
        g.append(f'<rect x="-42" y="15" width="84" height="115" rx="18" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -25 115 L -35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 25 115 L 35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -35 35 L -55 85" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<path d="M 35 30 L 100 5" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(worker_face(0, -45, 0.9, mood, glasses))
    else:  # stand
        g.append(f'<rect x="-42" y="15" width="84" height="115" rx="18" fill="{shirt}" stroke="{INK}" stroke-width="4.5"/>')
        g.append(f'<path d="M -25 115 L -35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M 25 115 L 35 190" stroke="{pants}" stroke-width="16" stroke-linecap="round"/>')
        g.append(f'<path d="M -35 35 L -60 90" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(f'<path d="M 35 35 L 60 90" stroke="{shirt}" stroke-width="15" stroke-linecap="round"/>')
        g.append(worker_face(0, -45, 0.9, mood, glasses))
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
