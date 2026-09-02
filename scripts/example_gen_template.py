# -*- coding: utf-8 -*-
"""Template: copy this per-project, fill in your own panels, then run the
render pipeline described in SKILL.md (svg -> png via cairosvg)."""
import sys
sys.path.insert(0, ".")  # adjust to wherever comic_lib.py was copied
from comic_lib import (cat, person, bond_guy, wallet_guy, moneybag, document_icon,
                        tree, bench, bulletin_board, house_door, government_building,
                        vault, store_shelf, counter, world_blob, pool, red_thread,
                        cross_out, check_mark, scale_icon, speech_bubble, heart,
                        motion_lines, sound_burst, gold_coin_guy, oil_barrel_guy,
                        shady_guy, build_svg, INK, ACCENT, WARM, PAPER)

CX = 400          # illustration-area center x (fixed by the panel layout system)
CY1 = 373.6       # illustration-area center y, panel 1 of the image
CY2 = 929.6       # illustration-area center y, panel 2 of the image

IMAGES = []

# Each image = one PNG = two panels (top/bottom). Each panel is a dict:
#   title    -> 5-10 汉字, verb-led
#   caption  -> the ONE real-world fact this panel stands for (never skip this)
#   content  -> SVG snippet: scenery first, then characters, then text/marks

p1 = {
    "title": "示例标题占位",
    "caption": "现实：这里写这一格对应的真实事实",
    "content": f'''
    {tree(CX-250, CY1+150, 0.85)}
    {cat(CX, CY1+80, 1.2, mood="neutral", pose="stand")}
    '''
}
p2 = {
    "title": "第二格标题占位",
    "caption": "现实：第二格对应的真实事实",
    "content": f'''
    {bond_guy(CX, CY2+60, 1.2, mood="happy")}
    '''
}
IMAGES.append([p1, p2])

for i, panels in enumerate(IMAGES, start=1):
    svg = build_svg(panels)
    with open(f"comic_{i}.svg", "w", encoding="utf-8") as f:
        f.write(svg)
print("done", len(IMAGES))
