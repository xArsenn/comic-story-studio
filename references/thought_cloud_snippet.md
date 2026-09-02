# `thought_cloud` snippet

Not bundled in `scripts/comic_lib.py` because it was written ad hoc per project — copy this
into your per-project render script (alongside the `comic_lib` import) when a panel needs a
"character is thinking about X" beat (e.g. the mascot realizing its own role in the story at
the end of a series).

```python
def thought_cloud(cx, cy, w, h, content, tail_to=None, ink="#1c1c1c", paper="#faf6ee"):
    """content: an SVG string (e.g. a small character drawn at local origin 0,0) that
    appears inside the cloud. tail_to: (x, y) point the trailing bubbles drift toward —
    typically the thinking character's head."""
    g = [f'<ellipse cx="{cx}" cy="{cy}" rx="{w/2}" ry="{h/2}" fill="{paper}" stroke="{ink}" stroke-width="3"/>']
    if tail_to:
        tx, ty = tail_to
        g.append(f'<circle cx="{cx-(cx-tx)*0.35}" cy="{cy+(h/2)+14}" r="10" fill="{paper}" stroke="{ink}" stroke-width="2.5"/>')
        g.append(f'<circle cx="{cx-(cx-tx)*0.55}" cy="{cy+(h/2)+30}" r="6" fill="{paper}" stroke="{ink}" stroke-width="2"/>')
    g.append(f'<g transform="translate({cx},{cy})">{content}</g>')
    return "\n".join(g)
```

Usage example (mascot thinking about the personified bond character):

```python
thought_cloud(CX+140, CY2-100, 220, 130,
              bond_guy(0, 10, 0.55, mood="happy", pose="cheer"),
              tail_to=(CX-60, CY2-30))
```
