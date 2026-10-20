#!/usr/bin/env python3
"""Build a labeled board (grid) from image files.

Used for moodboards on the pages and for agents that judge a set of images at once
(the audience panel, the recognition test). With --blind the order is shuffled,
file names are hidden behind letters, and the key is written OUTSIDE the board folder.

Usage:
  py board.py --out raw/visuals/boards/<name> [--size 360] [--cols 3] [--blind] [--no-labels] [--seed 7]
              [--masks masks.json] LABEL_OR_ID=path ...

Writes <out>/board/board.jpg, one tile per image, and <out>/key.json.
Give an agent the file paths (agents can't list a folder), never key.json.
masks.json (optional): {"LABEL_OR_ID": [[x0, y0, x1, y1], ...]} as fractions of width and height,
painted gray before resizing (to hide logos in a blind test).
"""
import argparse
import json
import random
import shutil
import string
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is missing. Run the plugin's setup again, or: python3 -m pip install --user pillow")


def open_image(path):
    """Pillow first; macOS sips for HEIC and other formats Pillow can't read; None if neither works."""
    try:
        return upright(Image.open(path)).convert("RGB")
    except Exception:
        pass
    if shutil.which("sips"):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "t.jpg"
            if subprocess.run(["sips", "-s", "format", "jpeg", str(path), "--out", str(out)],
                              capture_output=True).returncode == 0:
                return upright(Image.open(out)).convert("RGB")
    return None


def upright(img):
    """Turn a phone photo the way it was shot (its EXIF orientation), so masks and crops land right."""
    try:
        from PIL import ImageOps
        return ImageOps.exif_transpose(img)
    except Exception:
        return img


def square(img, size):
    img = img.convert("RGB")
    img.thumbnail((size, size))
    canvas = Image.new("RGB", (size, size), (244, 243, 240))
    canvas.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
    return canvas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", type=int, default=360)
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--blind", action="store_true")
    ap.add_argument("--no-labels", action="store_true", help="no captions on the sheet")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--masks")
    ap.add_argument("items", nargs="+", help="LABEL_OR_ID=path")
    a = ap.parse_args()
    if a.size < 40:
        sys.exit("--size must be 40 or more")

    items = []
    for it in a.items:
        if "=" not in it:
            sys.exit(f"Expected LABEL_OR_ID=path, got: {it}")
        k, p = it.split("=", 1)
        if not Path(p).is_file():
            print(f"Skipped, not a file: {p}")
            continue
        items.append((k, p))
    masks = json.loads(Path(a.masks).read_text()) if a.masks else {}
    if a.blind:
        random.Random(a.seed).shuffle(items)

    out = Path(a.out)
    board_dir = out / "board"
    board_dir.mkdir(parents=True, exist_ok=True)
    def letter(n):  # A..Z, then AA, AB ...
        s = ""
        n += 1
        while n:
            n, r = divmod(n - 1, 26)
            s = string.ascii_uppercase[r] + s
        return s
    key, tiles, names = {}, [], []
    for i, (k, p) in enumerate(items):
        label = letter(len(tiles)) if a.blind else k
        img = open_image(p)
        if img is None:
            print(f"Skipped, can't open: {p}")
            continue
        for box in masks.get(k, []):
            x0, y0, x1, y1 = box
            ImageDraw.Draw(img).rectangle(
                [x0 * img.width, y0 * img.height, x1 * img.width, y1 * img.height], fill=(200, 200, 200))
        tile = square(img, a.size)
        name = label if a.blind else f"{len(tiles) + 1:02d}"
        tile.save(board_dir / f"{name}.jpg", quality=85)
        names.append(f"{name}.jpg")
        key[label] = {"id": k, "file": p, "masked": k in masks}
        tiles.append((label, tile))

    if not tiles:
        sys.exit("No image could be opened: no board was made.")
    cols = max(1, a.cols)
    rows = (len(tiles) + cols - 1) // cols
    pad, cap = 12, (0 if a.no_labels else 26)
    sheet = Image.new("RGB", (cols * (a.size + pad) + pad, rows * (a.size + pad + cap) + pad), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    for i, (label, tile) in enumerate(tiles):
        x = pad + (i % cols) * (a.size + pad)
        y = pad + (i // cols) * (a.size + pad + cap)
        sheet.paste(tile, (x, y))
        if not a.no_labels:
            d.text((x, y + a.size + 6), str(label)[:40], fill=(20, 20, 20))
    sheet.save(board_dir / "board.jpg", quality=85)
    (out / "key.json").write_text(json.dumps({"size": a.size, "blind": a.blind, "labels": key}, indent=2))
    print(f"Board: {len(tiles)} images, {board_dir / 'board.jpg'}")
    files = ", ".join(str(board_dir / f) for f in ["board.jpg"] + names)
    print(f"Give the agent these files by path: {files} (never {out / 'key.json'})")


if __name__ == "__main__":
    main()
