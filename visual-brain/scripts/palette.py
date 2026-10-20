#!/usr/bin/env python3
"""Sample the main colors of images, so a palette rests on real pixels, not on taste.

Usage:
  py palette.py --colors 6 path1.jpg path2.png ...

Prints, per image, its main colors as hex with their share of the image, then the colors
shared across all images. Near-white and near-black backgrounds are reported but marked,
so they don't crowd out the product and the setting.
"""
import argparse
import sys
from collections import Counter

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is missing. Run the plugin's setup again, or: python3 -m pip install --user pillow")


def main_colors(path, n):
    img = Image.open(path).convert("RGB")
    img.thumbnail((240, 240))
    q = img.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: n * 3]
    hist = q.histogram()
    counts = Counter({i: hist[i] for i in range(min(n, len(hist))) if hist[i]})
    total = sum(counts.values())
    out = []
    for idx, c in counts.most_common(n):
        r, g, b = pal[idx * 3: idx * 3 + 3]
        out.append(("#%02x%02x%02x" % (r, g, b), c / total, (r, g, b)))
    return out


def note(rgb):
    r, g, b = rgb
    if min(r, g, b) > 235:
        return " (near white)"
    if max(r, g, b) < 25:
        return " (near black)"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--colors", type=int, default=6)
    ap.add_argument("files", nargs="+")
    a = ap.parse_args()
    opened = []
    for f in a.files:
        try:
            cols = main_colors(f, a.colors)
            tile = Image.open(f).convert("RGB").resize((200, 200))
        except Exception as e:
            print(f"{f}\n  skipped: can't open ({e.__class__.__name__}); convert it to JPEG first")
            continue
        opened.append(tile)
        print(f)
        for hx, share, rgb in cols:
            print(f"  {hx}  {share:5.1%}{note(rgb)}")
    if not opened:
        return
    # One palette for the whole set: all images side by side, then the same median cut.
    strip = Image.new("RGB", (200 * len(opened), 200))
    for i, tile in enumerate(opened):
        strip.paste(tile, (i * 200, 0))
    q = strip.quantize(colors=a.colors, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: a.colors * 3]
    hist = q.histogram()
    total = sum(hist[: a.colors]) or 1
    print("Palette for the set (use these, named by role):")
    for idx in sorted(range(a.colors), key=lambda i: -hist[i]):
        if not hist[idx]:
            continue
        r, g, b = pal[idx * 3: idx * 3 + 3]
        print(f"  #{r:02X}{g:02X}{b:02X}  {hist[idx] / total:5.1%}{note((r, g, b))}")


if __name__ == "__main__":
    main()
