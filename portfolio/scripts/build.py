#!/usr/bin/env python3
"""Build a case page from its .src.html.

- data-img="<path relative to the workspace>"  ->  an embedded, resized image (data URI).
  Photos become JPEG at --max px wide; PNG with transparency (logos) stays PNG.
- <!--MAP-->  ->  the market map SVG, drawn to scale from --map <map.json> (see templates/map.example.json).
  Points stay where the source puts them; only labels move apart.

Usage:
  python3 build.py --root . --map projects/portfolio/<case>/map.json \
      --out projects/portfolio/outputs/<case>.html projects/portfolio/<case>/case.src.html

Built pages carry the images: keep them out of git (the command adds the .gitignore line).
"""
import argparse, base64, io, json, re, sys
from pathlib import Path
from PIL import Image


def img_uri(path, max_w):
    im = Image.open(path)
    png = path.suffix.lower() == ".png" and im.mode in ("RGBA", "LA", "P")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if png:
        im.save(buf, "PNG", optimize=True); mime = "image/png"
    else:
        im.convert("RGB").save(buf, "JPEG", quality=76, optimize=True, progressive=True); mime = "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(buf.getvalue()).decode()


def market_svg(m):
    W, H, L, R, T, B = 1200, 560, 70, 30, 30, 70
    pw, ph = W - L - R, H - T - B
    X = lambda v: L + v / 100 * pw
    Y = lambda v: T + (1 - v / 100) * ph
    ink = "#2E2E2D"; mute = "#5B5853"
    cols = m.get("colors", {"market": ink, "own": "#A86F68", "direction": "#827B56"})
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Market map" xmlns="http://www.w3.org/2000/svg" font-family="IBM Plex Mono, monospace">']
    o = m.get("open_space")
    if o:
        s.append(f'<rect x="{X(o["x_min"]):.0f}" y="{Y(100):.0f}" width="{X(100)-X(o["x_min"]):.0f}" height="{Y(o["y_min"])-Y(100):.0f}" fill="none" stroke="{ink}" stroke-width="1.5" stroke-dasharray="6 6"/>')
        for i, line in enumerate(o.get("label", [])):
            s.append(f'<text x="{X(o["x_min"]+1):.0f}" y="{Y(96-i*4.5):.0f}" font-size="{13 if i == 0 else 12}" fill="{ink if i == 0 else mute}">{line}</text>')
    for v in (0, 25, 50, 75, 100):
        s.append(f'<line x1="{X(v):.0f}" y1="{T}" x2="{X(v):.0f}" y2="{T+ph}" stroke="{ink}" stroke-opacity=".08"/>')
        s.append(f'<line x1="{L}" y1="{Y(v):.0f}" x2="{L+pw}" y2="{Y(v):.0f}" stroke="{ink}" stroke-opacity=".08"/>')
        s.append(f'<text x="{X(v):.0f}" y="{T+ph+22}" font-size="12" fill="{mute}" text-anchor="middle">{v}</text>')
        s.append(f'<text x="{L-12}" y="{Y(v)+4:.0f}" font-size="12" fill="{mute}" text-anchor="end">{v}</text>')
    s.append(f'<line x1="{L}" y1="{T+ph}" x2="{L+pw}" y2="{T+ph}" stroke="{ink}" stroke-width="2"/>')
    s.append(f'<line x1="{L}" y1="{T}" x2="{L}" y2="{T+ph}" stroke="{ink}" stroke-width="2"/>')
    xa, ya = m["x_axis"], m["y_axis"]
    s.append(f'<text x="{L}" y="{H-12}" font-size="12" fill="{ink}">{xa[0]}</text>')
    s.append(f'<text x="{L+pw}" y="{H-12}" font-size="12" fill="{ink}" text-anchor="end">{xa[1]}</text>')
    s.append(f'<text transform="translate(18 {T+ph}) rotate(-90)" font-size="12" fill="{ink}">{ya[0]}</text>')
    s.append(f'<text transform="translate(18 {T}) rotate(-90)" font-size="12" fill="{ink}" text-anchor="end">{ya[1]}</text>')
    placed = []
    for p in m["points"]:
        col = cols[p["kind"] if p["kind"] in cols else "market"]
        r = 7 if p["kind"] == "market" else 9
        s.append(f'<circle cx="{X(p["x"]):.1f}" cy="{Y(p["y"]):.1f}" r="{r}" fill="{col}" fill-opacity="{0.85 if p["kind"] == "direction" else 1}"/>')
        anchor, dx = ("end", -14) if p["x"] > 70 else ("start", 14)
        lx, ly = X(p["x"]) + dx, Y(p["y"]) + 4
        # move the label, never the point, when it would sit on another label
        while any(abs(lx - qx) < 60 and abs(ly - qy) < 16 for qx, qy in placed):
            ly -= 20
        placed.append((lx, ly))
        weight = "400" if p["kind"] == "market" else "600"
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="14" font-weight="{weight}" fill="{col}" text-anchor="{anchor}">{p["name"]}</text>')
    s.append("</svg>")
    return "".join(s)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("src"); a.add_argument("--out", required=True)
    a.add_argument("--root", default="."); a.add_argument("--map"); a.add_argument("--max", type=int, default=1400)
    o = a.parse_args()
    root = Path(o.root)
    html = Path(o.src).read_text(encoding="utf-8")
    if not html.lstrip().lower().startswith('<meta charset'):
        html = '<meta charset="utf-8">\n' + html
    cache, missing = {}, []
    def rep(m):
        rel = m.group(1)
        if rel not in cache:
            p = root / rel
            if not p.exists():
                missing.append(rel); cache[rel] = ""
            else:
                cache[rel] = img_uri(p, o.max)
        return f'src="{cache[rel]}"'
    html = re.sub(r'data-img="([^"]+)"', rep, html)
    if "<!--MAP-->" in html:
        if not o.map:
            sys.exit("The page has <!--MAP--> but no --map file was given.")
        html = html.replace("<!--MAP-->", market_svg(json.loads(Path(o.map).read_text(encoding="utf-8"))))
    if missing:
        sys.exit("Missing images: " + ", ".join(missing))
    Path(o.out).parent.mkdir(parents=True, exist_ok=True)
    Path(o.out).write_text(html, encoding="utf-8")
    print(f"{o.out}: {len(html)/1e6:.2f} MB, {len(cache)} images")


if __name__ == "__main__":
    main()
