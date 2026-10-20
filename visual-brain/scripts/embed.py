#!/usr/bin/env python3
"""Put the images into the direction page, each image once, so the page is one light file.

Write the page with each image as  src="file:<path>"  (relative to the workspace, or absolute).
The same image may appear many times (collage, social media grid, site mockup): it is stored once.
Photos become JPEG at --max pixels; PNG files with transparency (logos, icons) stay PNG.
Image data is never printed, so nothing large lands in the chat.

Usage:
  py embed.py --max 760 --out projects/visual-brain/outputs/visual-direction.html projects/visual-brain/outputs/visual-direction.src.html

Keep the .src.html (with file: paths) next to the page: rebuild from it after any edit.
"""
import argparse
import base64
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PIXEL = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
GRAY = ("data:image/svg+xml;base64," + base64.b64encode(
    b'<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"><rect width="10" height="10" fill="#cfc9bb"/></svg>').decode())


def encode(path, max_px):
    try:
        from PIL import Image
        img = Image.open(path)
        try:
            from PIL import ImageOps
            img = ImageOps.exif_transpose(img)  # a phone photo, the way it was shot
        except Exception:
            pass
        if path.suffix.lower() == ".png" and img.mode in ("RGBA", "LA", "P") and "A" in img.convert("RGBA").getbands():
            rgba = img.convert("RGBA")
            if rgba.getextrema()[3][0] < 255:  # really transparent somewhere
                rgba.thumbnail((max_px, max_px))
                buf = io.BytesIO()
                rgba.save(buf, "PNG", optimize=True)
                return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
        img = img.convert("RGB")
        img.thumbnail((max_px, max_px))
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        pass
    if shutil.which("sips"):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "t.jpg"
            r = subprocess.run(["sips", "-Z", str(max_px), "-s", "format", "jpeg", str(path), "--out", str(out)],
                               capture_output=True)
            if r.returncode == 0 and out.exists():
                return "data:image/jpeg;base64," + base64.b64encode(out.read_bytes()).decode()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=760, help="longest side in pixels")
    ap.add_argument("--out", required=True, help="the finished page")
    ap.add_argument("src", help="the page with src=\"file:<path>\" images")
    a = ap.parse_args()
    html = Path(a.src).read_text(encoding="utf-8")
    keys = {}

    def swap(m):
        p = m.group(1)
        keys.setdefault(p, "i%d" % len(keys))
        return 'src="%s" data-k="%s"' % (PIXEL, keys[p])

    # only outside HTML comments
    parts = re.split(r"(<!--.*?-->)", html, flags=re.S)
    parts = [x if x.startswith("<!--") else re.sub(r'src="file:([^"]+)"', swap, x) for x in parts]
    body = "".join(parts)

    data, missing = {}, []
    for p, k in keys.items():
        uri = encode(Path(p), a.max)
        if uri is None:
            missing.append(p)
            uri = GRAY
        data[k] = uri
    script = ('<script>(function(){var D=%s;var L=document.querySelectorAll("img[data-k]");'
              'for(var i=0;i<L.length;i++){L[i].src=D[L[i].getAttribute("data-k")]}})();</script>') % json.dumps(data)
    marker = "<!-- embed:images -->"
    body = body.replace(marker, script, 1) if marker in body else body + "\n" + script
    Path(a.out).write_text(body, encoding="utf-8")
    size = len(body.encode("utf-8")) / 1e6
    print(f"Page: {a.out} ({len(keys)} images, {size:.1f} MB)")
    if size > 15:
        print("Too big for one page: lower --max or use fewer images.")
    for p in missing:
        print(f"  could not open: {p} (shown as a gray tile; convert it to JPEG and rebuild)")


if __name__ == "__main__":
    sys.exit(main())
