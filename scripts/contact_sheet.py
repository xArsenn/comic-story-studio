#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contact-sheet QC tool for comic-story-studio.

Composite a batch of rendered PNGs into one labeled grid so you can eyeball
character/color/style consistency across a whole series in one glance,
instead of opening each panel separately. Also useful during revisions —
each thumbnail is numbered so the user can say "change #3" instead of
describing the image.

Usage:
    python3 contact_sheet.py out.png img1.png img2.png img3.png ...
    python3 contact_sheet.py out.png --glob "work_*.png"
    python3 contact_sheet.py out.png --cols 4 img1.png img2.png ...

Requires Pillow (already available in this environment).
"""
import sys
import glob
import argparse
from PIL import Image, ImageDraw, ImageFont


def build_contact_sheet(paths, out_path, cols=None, thumb_w=360, label=True,
                          bg=(250, 246, 238), gap=16, font_size=28):
    if not paths:
        raise ValueError("No input images given.")
    n = len(paths)
    cols = cols or min(4, n)
    rows = (n + cols - 1) // cols

    imgs = []
    for p in paths:
        im = Image.open(p).convert("RGB")
        ratio = thumb_w / im.width
        im = im.resize((thumb_w, int(im.height * ratio)))
        imgs.append(im)
    thumb_h = max(im.height for im in imgs)

    label_h = font_size + 14 if label else 0
    cell_w = thumb_w + gap
    cell_h = thumb_h + label_h + gap

    sheet_w = cols * cell_w + gap
    sheet_h = rows * cell_h + gap
    sheet = Image.new("RGB", (sheet_w, sheet_h), bg)
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", font_size)
    except Exception:
        font = ImageFont.load_default()

    for i, im in enumerate(imgs):
        r, c = divmod(i, cols)
        x = gap + c * cell_w
        y = gap + r * cell_h
        sheet.paste(im, (x, y))
        if label:
            draw.rectangle([x, y + thumb_h, x + thumb_w, y + thumb_h + label_h],
                            fill=(230, 224, 210))
            draw.text((x + 8, y + thumb_h + 5), f"#{i+1}", fill=(30, 30, 30), font=font)

    sheet.save(out_path)
    print(f"Wrote {out_path}: {n} images, {cols}x{rows} grid")
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", help="output PNG path")
    ap.add_argument("inputs", nargs="*", help="input PNG paths (in order)")
    ap.add_argument("--glob", help="glob pattern instead of listing files (sorted)")
    ap.add_argument("--cols", type=int, default=None)
    ap.add_argument("--no-label", action="store_true")
    args = ap.parse_args()

    paths = sorted(glob.glob(args.glob)) if args.glob else args.inputs
    if not paths:
        ap.error("No input images: pass paths or --glob 'pattern*.png'")
    build_contact_sheet(paths, args.out, cols=args.cols, label=not args.no_label)


if __name__ == "__main__":
    main()
