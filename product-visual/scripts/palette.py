#!/usr/bin/env python3
"""Sample the main colors of images, so a palette rests on real pixels, not on taste.

Usage:
  py palette.py --colors 6 path1.jpg path2.png ...

Prints, per image, its main colors as hex with their share of the image, then the colors
shared across all images. Transparent pixels (a cut-out, a logo) are left out. Colors too
close to tell apart are merged, so the list holds distinct colors only (up to --colors).
Near-white and near-black backgrounds are reported but marked, so they don't crowd out the
product and the setting.
"""
import argparse
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is missing. Run the plugin's setup again, or: python3 -m pip install --user pillow")

MERGE = 20  # RGB distance below which two colors read as one
PER_IMAGE = 20000  # pixels taken from each image for the set, so each image weighs the same


def opaque_pixels(path, size=240):
    img = Image.open(path).convert("RGBA")
    img.thumbnail((size, size))
    data = img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()
    px = [p[:3] for p in data if p[3] >= 128]
    return px, len(px) < img.size[0] * img.size[1]


def distinct_colors(pixels, n):
    if not pixels:
        return []
    strip = Image.new("RGB", (len(pixels), 1))
    strip.putdata(pixels)
    k = min(max(n * 3, 8), 256)
    q = strip.quantize(colors=k, method=Image.Quantize.MEDIANCUT)
    pal, hist = q.getpalette(), q.histogram()
    found = sorted(((hist[i], tuple(pal[i * 3: i * 3 + 3])) for i in range(min(k, len(hist))) if hist[i]), reverse=True)
    merged = []
    for count, rgb in found:
        for m in merged:
            if sum((a - b) ** 2 for a, b in zip(m[1], rgb)) ** 0.5 < MERGE:
                m[0] += count
                break
        else:
            merged.append([count, rgb])
    merged.sort(reverse=True)
    total = sum(m[0] for m in merged) or 1
    return [("#%02X%02X%02X" % rgb, count / total, rgb) for count, rgb in merged[:n] if count / total >= 0.005]


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
    if not 1 <= a.colors <= 32:
        sys.exit("--colors must be between 1 and 32")
    pooled = []
    for f in a.files:
        try:
            px, cut = opaque_pixels(f)
        except Exception as e:
            print(f"{f}\n  skipped: can't open ({e.__class__.__name__}); convert it to JPEG first")
            continue
        if not px:
            print(f"{f}\n  skipped: every pixel is transparent")
            continue
        print(f + ("  (transparent pixels left out)" if cut else ""))
        for hx, share, rgb in distinct_colors(px, a.colors):
            print(f"  {hx}  {share:5.1%}{note(rgb)}")
        step = max(1, len(px) // PER_IMAGE)
        pooled.extend(px[::step])
    if not pooled:
        return
    print("Palette for the set (distinct colors, use these, named by role):")
    for hx, share, rgb in distinct_colors(pooled, a.colors):
        print(f"  {hx}  {share:5.1%}{note(rgb)}")


if __name__ == "__main__":
    main()
