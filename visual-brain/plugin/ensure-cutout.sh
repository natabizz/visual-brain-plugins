#!/usr/bin/env bash
# Optional: the cut-out library (rembg) that lets scripts/range.py show the owner's own photos on each
# proposed backdrop (background only, the product untouched). About 200 MB on first use. Run only after the owner says yes.
# rembg needs Python 3.10 or newer. The scripts run on the plugin venv (~/.visual-brain/venv) when it has Pillow, else on
# python3. When that Python is older, this looks for a newer one (python3.13 to 3.10, Homebrew) and rebuilds the
# plugin venv on it, with Pillow and rembg.
VDIR="$HOME/.visual-brain/venv"
V="$VDIR/bin/python3"
if [ -x "$V" ] && "$V" -c "import PIL" 2>/dev/null; then RUN="$V"; else RUN="python3"; fi
ok310() { "$1" -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; }
has() { "$1" -c "import rembg, PIL" 2>/dev/null; }
ready() { echo "Cut-out: installed. The first preview downloads the model once (about 170 MB)."; exit 0; }
skip="Previews are skipped; the range still shows colors, checks and shapes."

if has "$RUN"; then echo "Cut-out: ready."; exit 0; fi

# 1. The Python the scripts already use is new enough: install into it.
if ok310 "$RUN"; then
  if [ "$RUN" = "$V" ]; then
    "$V" -m pip install --quiet pillow "rembg[cpu]" 2>/dev/null && has "$V" && ready
  else
    python3 -m pip install --user --quiet pillow "rembg[cpu]" 2>/dev/null && has python3 && ready
  fi
fi

# 2. Otherwise (or if that failed): a plugin venv on a Python 3.10 or newer.
NEW=""
for p in python3 python3.13 python3.12 python3.11 python3.10 /opt/homebrew/bin/python3 /usr/local/bin/python3; do
  if command -v "$p" >/dev/null 2>&1 && ok310 "$p"; then NEW="$(command -v "$p")"; break; fi
done
if [ -z "$NEW" ]; then
  echo "Cut-out: needs Python 3.10 or newer, and none was found (python3 here is $(python3 -c 'import platform; print(platform.python_version())' 2>/dev/null)). On a Mac with Homebrew: brew install python, then ask again. $skip"
  exit 1
fi
mkdir -p "$HOME/.visual-brain"
# Built beside the current venv and swapped in only when it works, so a failed install leaves Pillow in place.
T="$HOME/.visual-brain/venv-new"
if "$NEW" -m venv --clear "$T" 2>/dev/null && "$T/bin/python3" -m pip install --quiet pillow "rembg[cpu]" 2>/dev/null && has "$T/bin/python3"; then
  rm -rf "$VDIR.old"
  [ -d "$VDIR" ] && mv "$VDIR" "$VDIR.old"
  mv "$T" "$VDIR"
  if has "$V"; then rm -rf "$VDIR.old"; ready; fi
  rm -rf "$VDIR"; [ -d "$VDIR.old" ] && mv "$VDIR.old" "$VDIR"
fi
rm -rf "$T"
echo "Cut-out: could not install it automatically. $skip"
exit 1
