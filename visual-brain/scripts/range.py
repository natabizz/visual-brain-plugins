#!/usr/bin/env python3
"""The range check: one backdrop per variant, checked at tile size.

For each variant of the product (a colorway, a line), it finds the product's color,
proposes a backdrop by the direction's rule, and checks whether the product's edge
still reads against that backdrop at thumbnail size. When it doesn't, it shows
three more backdrops (deeper and quieter, lifted, a quiet neutral) and says which pass.

Usage:
  py range.py [--steps 20] [--tile 260] [--out sheet.jpg] [--previews DIR] [--own "Name=#hex" ...] VARIANT [VARIANT ...]

VARIANT is one of:
  "Olive=#5E6B2F"                 the product color, as hex (from the product file)
  "Olive=path/to/photo.png@0.30,0.05,0.70,0.40"
                                  a real photo and a box around the product, as fractions
                                  of width and height (left, top, right, bottom); the
                                  product color is sampled inside the box
  "Olive=path/to/photo.png"       a real photo without a box: the center third is sampled

Option A is a tonal backdrop: the product's hue, a little less saturated, --steps lightness
units darker. B goes deeper and quieter, C lighter, D is a quiet neutral. When the
direction's rule gives another backdrop, pass it with --own "Name=#hex" (one per variant):
it is checked as option E. A pass means the difference (CIEDE2000) is 15 or more and the
lightness gap 10 or more. These are working thresholds for a color heuristic, not a
standard: below them the product's edge tends to sink into the backdrop at thumbnail size.
The sheet shows every pair at tile size, so the eye makes the final call.

With --previews and a photo, the real photo is cut out and set on each backdrop
(background only, the product untouched), if the cut-out library (rembg) is installed
(plugin/ensure-cutout.sh, after the owner says yes), or if the photo given is already a
cut-out PNG with transparency (from a connected image tool). Without either, the sheet
uses a plain shape in the product color, and says so.

Prints a table to paste into the guide, and writes a sheet at tile size.
"""
import math
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is missing: run the plugin setup first.")

# ---------- color math (sRGB, D65) ----------

def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _unlin(c):
    c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055
    return max(0, min(255, round(c * 255)))

def rgb_to_lab(rgb):
    r, g, b = (_lin(v) for v in rgb)
    x = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.0
    z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 216 / 24389 else (24389 / 27 * t + 16) / 116
    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))

def lab_to_rgb(lab):
    L, a, b = lab
    fy = (L + 16) / 116
    fx = fy + a / 500
    fz = fy - b / 200
    inv = lambda t: t ** 3 if t ** 3 > 216 / 24389 else (116 * t - 16) / (24389 / 27)
    x, y, z = inv(fx) * 0.95047, inv(fy), inv(fz) * 1.08883
    r = 3.2404542 * x - 1.5371385 * y - 0.4985314 * z
    g = -0.9692660 * x + 1.8760108 * y + 0.0415560 * z
    bl = 0.0556434 * x - 0.2040259 * y + 1.0572252 * z
    return tuple(_unlin(max(0.0, min(1.0, v))) for v in (r, g, bl))

def lab_to_lch(lab):
    L, a, b = lab
    return (L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360)

def lch_to_lab(lch):
    L, C, h = lch
    return (L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h)))

def hexs(rgb):
    return "#%02X%02X%02X" % tuple(rgb)

def parse_hex(s):
    h = s.strip().lstrip("#")
    if not re.fullmatch(r"[0-9A-Fa-f]{6}", h):
        sys.exit("Not a hex color (six digits, like #A3222C): " + s.strip())
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def de2000(l1, l2):
    L1, a1, b1 = l1
    L2, a2, b2 = l2
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360
    h2p = math.degrees(math.atan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    dh = h2p - h1p
    if C1p * C2p == 0:
        dh = 0
    elif dh > 180:
        dh -= 360
    elif dh < -180:
        dh += 360
    dHp = 2 * math.sqrt(C1p * C2p) * math.sin(math.radians(dh / 2))
    Lm = (L1 + L2) / 2
    Cmp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hm = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hm = (h1p + h2p) / 2
    else:
        hm = (h1p + h2p + 360) / 2 if h1p + h2p < 360 else (h1p + h2p - 360) / 2
    T = (1 - 0.17 * math.cos(math.radians(hm - 30)) + 0.24 * math.cos(math.radians(2 * hm))
         + 0.32 * math.cos(math.radians(3 * hm + 6)) - 0.20 * math.cos(math.radians(4 * hm - 63)))
    dth = 30 * math.exp(-(((hm - 275) / 25) ** 2))
    Rc = 2 * math.sqrt(Cmp ** 7 / (Cmp ** 7 + 25 ** 7))
    Sl = 1 + (0.015 * (Lm - 50) ** 2) / math.sqrt(20 + (Lm - 50) ** 2)
    Sc = 1 + 0.045 * Cmp
    Sh = 1 + 0.015 * Cmp * T
    Rt = -math.sin(math.radians(2 * dth)) * Rc
    return math.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2 + Rt * (dCp / Sc) * (dHp / Sh))


def upright(img):
    """Turn a phone photo the way it was shot (its EXIF orientation), so masks and crops land right."""
    try:
        from PIL import ImageOps
        return ImageOps.exif_transpose(img)
    except Exception:
        return img

# ---------- sampling ----------

def open_photo(path):
    try:
        return upright(Image.open(path))
    except Exception as e:
        sys.exit("Can't open %s (%s). Convert it to JPEG first." % (path, e.__class__.__name__))

def sample(path, box):
    im = open_photo(path).convert("RGBA")
    w, h = im.size
    if box is None:
        box = (1 / 3, 1 / 3, 2 / 3, 2 / 3)
    x0, y0, x1, y1 = box
    crop = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h))).resize((80, 80))
    px = crop.get_flattened_data() if hasattr(crop, "get_flattened_data") else crop.getdata()
    labs = [rgb_to_lab(p[:3]) for p in px if p[3] >= 128]  # a cut-out's empty pixels are skipped
    if len(labs) < 20:
        sys.exit("Too few product pixels inside the box of %s: draw the box around the product." % path)
    labs.sort(key=lambda l: math.hypot(l[1], l[2]), reverse=True)
    top = labs[: len(labs) // 2]
    use = top if math.hypot(*_median(top)[1:]) > 15 else labs
    return lab_to_rgb(_median(use))

def _median(labs):
    out = []
    for i in range(3):
        v = sorted(l[i] for l in labs)
        out.append(v[len(v) // 2])
    return tuple(out)

# ---------- backdrops ----------

PASS_DE = 15.0   # below this the product's edge sinks into the backdrop at tile size
PASS_DL = 10.0

def check(prod_rgb, rgb):
    lab_b, lab_p = rgb_to_lab(rgb), rgb_to_lab(prod_rgb)
    de = de2000(lab_p, lab_b)
    dl = abs(lab_p[0] - lab_b[0])
    return de, dl, de >= PASS_DE and dl >= PASS_DL

def backdrops(prod_rgb, steps, own=None):
    L, C, h = lab_to_lch(rgb_to_lab(prod_rgb))
    opts = [
        ("A, tonal", (max(8.0, L - steps), C * 0.85, h)),
        ("B, deeper and quieter", (max(6.0, L - steps * 1.7), C * 0.5, h)),
        ("C, lifted", (L + steps, C * 0.6, h)),
        ("D, quiet neutral", (L + 25 if L < 50 else L - 25, min(C, 5.0), h)),
    ]
    out = []
    for name, lch in opts:
        lch = (max(4.0, min(96.0, lch[0])), lch[1], lch[2])
        rgb = lab_to_rgb(lch_to_lab(lch))
        out.append((name, rgb) + check(prod_rgb, rgb))
    if own is not None:
        out.append(("E, the direction's own", own) + check(prod_rgb, own))
    return out

# ---------- previews ----------

_session = None

def cutout(path):
    global _session
    im0 = open_photo(path)
    if im0.mode in ("RGBA", "LA") and im0.getextrema()[-1][0] < 250:
        im0 = im0.convert("RGBA")
        im0.thumbnail((1200, 1200))
        return im0  # already cut out (by a connected image tool, say): used as it is
    try:
        from rembg import remove, new_session
    except ImportError:
        return None
    try:
        if _session is None:
            _session = new_session("u2net")
        im = im0.convert("RGB")
        im.thumbnail((1200, 1200))
        return remove(im, session=_session)
    except Exception as e:
        print("  note: the cut-out failed for %s (%s); a plain shape is used instead." % (os.path.basename(path), e.__class__.__name__))
        return None

def seamless(rgb, size):
    """A plain seamless: a touch lighter at the top, a touch darker at the floor."""
    w, h = size
    L, a, b = rgb_to_lab(rgb)
    bg = Image.new("RGB", (w, h))
    px = bg.load()
    rows = [lab_to_rgb((max(0, min(100, L + 5 - 10 * y / max(1, h - 1))), a, b)) for y in range(h)]
    for y in range(h):
        c = rows[y]
        for x in range(w):
            px[x, y] = c
    return bg

def on_backdrop(cut, rgb, size):
    from PIL import ImageFilter
    bg = seamless(rgb, cut.size)
    alpha = cut.split()[3]
    shadow = Image.new("L", cut.size, 0)
    shadow.paste(alpha.point(lambda v: 90 if v > 128 else 0), (0, max(2, cut.size[1] // 80)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(max(4, cut.size[0] // 60)))
    bg.paste(Image.new("RGB", cut.size, (0, 0, 0)), (0, 0), shadow)
    bg.paste(cut, (0, 0), cut)
    # The whole product stays in the square: the scene is fitted on a seamless square, never cropped.
    s = int(max(bg.size) * 1.08)
    sq = seamless(rgb, (s, s))
    sq.paste(bg, ((s - bg.width) // 2, (s - bg.height) // 2))
    return sq.resize((size, size))

def shape_tile(prod, rgb, size):
    t = Image.new("RGB", (size, size), rgb)
    d = ImageDraw.Draw(t)
    w, h = size * 0.42, size * 0.5
    cx, cy = size / 2, size * 0.52
    box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    if hasattr(d, "rounded_rectangle"):
        d.rounded_rectangle(box, radius=size * 0.05, fill=prod)  # a neutral stand-in for the product
    else:
        d.rectangle(box, fill=prod)
    return t

def font(sz):
    for f in ("/System/Library/Fonts/Helvetica.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, sz)
            except OSError:
                pass
    return ImageFont.load_default()

# ---------- main ----------

def main(argv):
    steps, tile, out, prev = 20.0, 260, "range-sheet.jpg", None
    owns = {}
    vars_ = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--steps", "--tile", "--out", "--previews", "--own"):
            if i + 1 >= len(argv):
                sys.exit("%s needs a value" % a)
            v = argv[i + 1]; i += 2
            try:
                if a == "--steps":
                    steps = float(v)
                elif a == "--tile":
                    tile = int(v)
                elif a == "--out":
                    out = v
                elif a == "--own":
                    if "=" not in v:
                        sys.exit("--own is Name=#hex (the direction's own backdrop for that variant): " + v)
                    on, oh = v.split("=", 1)
                    owns[on.strip()] = parse_hex(oh)
                else:
                    prev = v
            except ValueError:
                sys.exit("%s needs a number, got: %s" % (a, v))
            continue
        vars_.append(a); i += 1
    if not vars_:
        sys.exit(__doc__)
    if tile < 40 or steps <= 0:
        sys.exit("--tile must be 40 or more and --steps more than 0")

    rows = []
    for v in vars_:
        if "=" not in v:
            sys.exit("Each variant is Name=#hex or Name=photo[@box]: " + v)
        name, src = v.split("=", 1)
        photo, box = None, None
        if src.strip().startswith("#"):
            prod = parse_hex(src)
            how = "from the product file"
        else:
            photo = src
            m = re.match(r"^(.*)@\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)\s*$", src)
            if m and not os.path.exists(src):
                photo = m.group(1).rstrip()
                box = tuple(float(m.group(k)) for k in range(2, 6))
                if not all(0 <= b <= 1 for b in box) or box[0] >= box[2] or box[1] >= box[3]:
                    sys.exit("The box after @ is x0,y0,x1,y1 as fractions of the photo, each from 0 to 1: " + src)
            if not os.path.exists(photo):
                sys.exit("No such photo: " + photo)
            prod = sample(photo, box)
            how = "sampled from " + os.path.basename(photo)
        opts = backdrops(prod, steps, owns.get(name.strip()))
        rows.append((name.strip(), prod, how, opts, photo))

    print("The range: one backdrop per variant, checked at %d px (pass: difference %.0f or more, lightness gap %.0f or more)" % (tile, PASS_DE, PASS_DL))
    has_own = any(len(r[3]) > 4 for r in rows)
    print("| Variant | Product color | A, tonal | B, deeper and quieter | C, lifted | D, quiet neutral |" + (" E, the direction's own |" if has_own else ""))
    print("|---|---|---|---|---|---|" + ("---|" if has_own else ""))
    for name, prod, how, opts, photo in rows:
        cells = ["%s %s (%.0f / %.0f)" % (hexs(rgb), "pass" if ok else "too close", de, dl) for oname, rgb, de, dl, ok in opts]
        if has_own and len(opts) == 4:
            cells.append("not given")
        print("| %s | %s (%s) | %s |" % (name, hexs(prod), how, " | ".join(cells)))
        rule = opts[-1] if len(opts) > 4 else opts[0]
        if not rule[4]:
            good = [o[0].split(",")[0] for o in opts if o[4] and o is not rule]
            print("  note: for %s the rule's backdrop (%s) is too close to the piece at tile size; %s." % (name, rule[0].split(",")[0], ("options that pass: " + ", ".join(good)) if good else "no option passes: change the light or the crop"))

    # the sheet
    pad, label_w = 12, 170
    W = label_w + (5 if has_own else 4) * (tile + pad) + pad
    H = pad + len(rows) * (tile + 34 + pad)
    sheet = Image.new("RGB", (W, H), (246, 244, 241))
    d = ImageDraw.Draw(sheet)
    f, fs = font(18), font(13)
    used_photo = False
    seen = set()
    for r, (name, prod, how, opts, photo) in enumerate(rows):
        safe = re.sub(r"[^\w.-]+", "-", name).strip("-.") or "variant-%d" % (r + 1)
        base, k = safe, 2
        while safe.lower() in seen:
            safe = "%s-%d" % (base, k)
            k += 1
        seen.add(safe.lower())
        y = pad + r * (tile + 34 + pad)
        d.text((pad, y + 4), name, fill=(28, 26, 25), font=f)
        d.rectangle((pad, y + 32, pad + 40, y + 72), fill=prod)
        d.text((pad, y + 78), hexs(prod), fill=(90, 85, 80), font=fs)
        cut = cutout(photo) if (photo and prev is not None) else None
        for c, (oname, rgb, de, dl, ok) in enumerate(opts):
            x = label_w + pad + c * (tile + pad)
            t = on_backdrop(cut, rgb, tile) if cut is not None else shape_tile(prod, rgb, tile)
            if cut is not None:
                used_photo = True
                if prev:
                    os.makedirs(prev, exist_ok=True)
                    on_backdrop(cut, rgb, 1200).save(os.path.join(prev, "%s-%s.jpg" % (safe, oname[0])), quality=90)
            sheet.paste(t, (x, y))
            d.text((x, y + tile + 6), "%s %s  %s" % (oname.split(",")[0], hexs(rgb), "pass" if ok else "too close"), fill=(28, 26, 25) if ok else (163, 34, 44), font=fs)
    sheet.save(out, quality=88)
    print("Sheet: %s (%s)" % (out, "real photos, background replaced; the product untouched" if used_photo else "plain shapes in the product color; real-photo previews need the cut-out library (rembg)"))
    if prev is not None and not used_photo:
        print("No previews: the cut-out library (rembg) is not installed and no cut-out PNG was given, or no variant was given as a photo. To enable: bash %s (about 200 MB, ask the owner first)." % os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "plugin", "ensure-cutout.sh"))

if __name__ == "__main__":
    main(sys.argv[1:])
