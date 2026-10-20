#!/usr/bin/env python3
"""Build a blind shelf: the main image among competing main images, logos masked, at thumbnail size.

Takes main images as FRAME_ID=path pairs, resizes each to the size the channel
shows in mobile search, masks logo areas, shuffles them and labels them A, B, C.
Writes:
  <out>/grid/A.jpg, B.jpg ...   one file per image, for the fresh-eyes agent
  <out>/grid/grid.jpg           all images on one sheet, like a results page
  <out>/key.json                which letter is which frame (never shown to the agent)
  <out>/masks.json              the masks used, so a later run can reuse them

Usage:
  python3 shelf.py --out raw/visuals/shelf/2026-10-17-hats --size 360 \
      [--masks masks.json] [--cols 2] [--seed 7] \
      OWN-amazon-hat-01=raw/visuals/own/hat-01.jpg CMP-acme-amazon-hat-01=raw/visuals/screens/acme-01.png

masks.json maps a frame ID to boxes in fractions of width and height:
  {"CMP-acme-amazon-hat-01": [[0.70, 0.02, 0.98, 0.12]]}

Needs Pillow: the plugin setup installs it.
"""
import argparse
import json
import random
import string
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.stderr.write("Pillow is not installed. Run the plugin's setup again (it installs Pillow), or: python3 -m pip install --user pillow\n")
    sys.exit(2)


def fit_square(img, size):
    img = img.convert("RGB")
    img.thumbnail((size, size))
    canvas = Image.new("RGB", (size, size), (255, 255, 255))
    canvas.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
    return canvas


def apply_masks(img, boxes):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for x0, y0, x1, y1 in boxes:
        draw.rectangle([x0 * w, y0 * h, x1 * w, y1 * h], fill=(200, 200, 200))
    return img


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", type=int, default=360, help="pixels, measured from a mobile search screenshot")
    ap.add_argument("--masks", help="JSON file of logo boxes per frame ID")
    ap.add_argument("--cols", type=int, default=2, help="columns on the sheet; 2 matches most mobile results")
    ap.add_argument("--seed", type=int, help="fix the shuffle to repeat a run")
    ap.add_argument("frames", nargs="+", help="FRAME_ID=path")
    a = ap.parse_args()

    pairs = []
    for item in a.frames:
        if "=" not in item:
            sys.exit(f"Expected FRAME_ID=path, got: {item}")
        fid, path = item.split("=", 1)
        if not Path(path).is_file():
            sys.exit(f"Missing file for {fid}: {path}")
        pairs.append((fid, path))
    if len(pairs) > 26:
        sys.exit("At most 26 images per shelf.")

    masks = {}
    if a.masks:
        masks = json.loads(Path(a.masks).read_text())
        Path(a.out).mkdir(parents=True, exist_ok=True)
        (Path(a.out) / "masks.json").write_text(json.dumps(masks, indent=2))  # kept with the run, so a later run can reuse it

    rng = random.Random(a.seed)
    rng.shuffle(pairs)

    out = Path(a.out)
    grid_dir = out / "grid"
    grid_dir.mkdir(parents=True, exist_ok=True)

    key, tiles = {}, []
    for letter, (fid, path) in zip(string.ascii_uppercase, pairs):
        img = Image.open(path).convert("RGB")
        if fid in masks:
            img = apply_masks(img, masks[fid])  # boxes are fractions of the original image
        img = fit_square(img, a.size)
        img.save(grid_dir / f"{letter}.jpg", quality=88)
        key[letter] = {"frame_id": fid, "file": path, "masked": fid in masks}
        tiles.append((letter, img))

    label_h, gap = 28, 12
    cols = max(1, a.cols)
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * a.size + (cols + 1) * gap, rows * (a.size + label_h) + (rows + 1) * gap), (245, 245, 245))
    draw = ImageDraw.Draw(sheet)
    font = None
    for name in ("DejaVuSans-Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf"):
        try:
            font = ImageFont.truetype(name, 18)
            break
        except OSError:
            continue
    if font is None:
        try:
            font = ImageFont.load_default(size=18)
        except TypeError:
            font = ImageFont.load_default()
    for i, (letter, img) in enumerate(tiles):
        r, c = divmod(i, cols)
        x = gap + c * (a.size + gap)
        y = gap + r * (a.size + label_h + gap)
        sheet.paste(img, (x, y))
        draw.text((x + 4, y + a.size + 4), letter, fill=(20, 20, 20), font=font)
    sheet.save(grid_dir / "grid.jpg", quality=88)

    (out / "key.json").write_text(json.dumps({"size": a.size, "cols": cols, "seed": a.seed, "letters": key}, indent=2))
    print(f"Shelf: {len(tiles)} images, {a.size}px, sheet {grid_dir / 'grid.jpg'}")
    names = ", ".join(str(grid_dir / f"{l}.jpg") for l, _ in tiles)
    print(f"Give the agent these files by path: {grid_dir / 'grid.jpg'}, {names} (never {out / 'key.json'})")


if __name__ == "__main__":
    main()
