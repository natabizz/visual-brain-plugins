#!/usr/bin/env python3
"""Put the images into a page, so it is one self-contained file.

Write the page with each image as  src="file:<path to the image>"  (a path relative to the
workspace, or absolute). This script swaps every such src for a small data URI and saves the page.
It never prints image data, so nothing large lands in the chat.

Usage:
  py fill.py --max 480 projects/product-visual/outputs/<product>-<channel>-audit.html
  py fill.py --max 480 --out page-filled.html page.html

Opens images with Pillow; falls back to macOS sips (HEIC, odd formats); an image that can't be
opened becomes a gray tile, and is listed at the end so you can fix it.
"""
import argparse
import base64
import io
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

GRAY = ("data:image/svg+xml;base64," + base64.b64encode(
    b'<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"><rect width="10" height="10" fill="#cfc9bb"/></svg>').decode())


def to_jpeg(path, max_px):
    try:
        from PIL import Image
        img = Image.open(path)
        img = img.convert("RGB")
        img.thumbnail((max_px, max_px))
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
        return buf.getvalue()
    except Exception:
        pass
    if shutil.which("sips"):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "t.jpg"
            r = subprocess.run(["sips", "-Z", str(max_px), "-s", "format", "jpeg", str(path), "--out", str(out)],
                               capture_output=True)
            if r.returncode == 0 and out.exists():
                return out.read_bytes()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=480, help="longest side in pixels")
    ap.add_argument("--out", help="write here instead of replacing the page in place")
    ap.add_argument("page")
    a = ap.parse_args()
    page = Path(a.page)
    html = page.read_text(encoding="utf-8")
    cache, missing = {}, []

    def swap(m):
        raw = m.group(1)
        p = Path(raw)
        if raw not in cache:
            data = to_jpeg(p, a.max) if p.is_file() else None
            if data is None:
                missing.append(raw)
                cache[raw] = GRAY
            else:
                cache[raw] = "data:image/jpeg;base64," + base64.b64encode(data).decode()
        return 'src="' + cache[raw] + '"'

    # Swap only outside HTML comments, so instructions in comments stay as they are.
    parts = re.split(r"(<!--.*?-->)", html, flags=re.S)
    html = "".join(part if part.startswith("<!--") else re.sub(r'src="file:([^"]+)"', swap, part) for part in parts)
    target = Path(a.out) if a.out else page
    target.write_text(html, encoding="utf-8")
    size = target.stat().st_size / 1e6
    print(f"Page: {target} ({len(cache)} images, {size:.1f} MB)")
    if size > 15:
        print("Warning: the page is over 15 MB. Use fewer images or a smaller --max.")
    if missing:
        print("Could not open (shown as gray tiles):")
        for m in missing:
            print("  " + m)


if __name__ == "__main__":
    main()
