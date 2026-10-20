#!/usr/bin/env bash
# Makes sure Pillow (the image library the scripts use) is available, without asking the owner to type anything.
# 1. Already there? Done.  2. pip --user.  3. If the system Python refuses (externally managed), a private venv
# in ~/.visual-brain/venv that scripts/py picks up automatically.
V="$HOME/.visual-brain/venv/bin/python3"
if python3 -c "import PIL" 2>/dev/null; then echo "Pillow: ready (system Python)."; exit 0; fi
if [ -x "$V" ] && "$V" -c "import PIL" 2>/dev/null; then echo "Pillow: ready (plugin venv)."; exit 0; fi
if ! command -v python3 >/dev/null 2>&1; then
  echo "Pillow: Python 3 is not installed. On a Mac, run: xcode-select --install   then run setup again."; exit 1
fi
if python3 -m pip install --user --quiet pillow 2>/dev/null && python3 -c "import PIL" 2>/dev/null; then
  echo "Pillow: installed (system Python)."; exit 0
fi
mkdir -p "$HOME/.visual-brain"
if python3 -m venv "$HOME/.visual-brain/venv" 2>/dev/null && "$V" -m pip install --quiet pillow 2>/dev/null; then
  echo "Pillow: installed in ~/.visual-brain/venv."; exit 0
fi
echo "Pillow: could not install it automatically. Image boards and palettes will be skipped and marked (limited: no Pillow)."
exit 1
