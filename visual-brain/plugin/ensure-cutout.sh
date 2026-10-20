#!/usr/bin/env bash
# Optional: the cut-out library (rembg) that lets scripts/range.py show the owner's own photos on each
# proposed backdrop (background only, the product untouched). About 200 MB on first use. Run only after the owner says yes.
V="$HOME/.visual-brain/venv/bin/python3"
if [ -x "$V" ]; then PY="$V"; else PY="python3"; fi
if "$PY" -c "import rembg" 2>/dev/null; then echo "Cut-out: ready."; exit 0; fi
if ! "$PY" -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)" 2>/dev/null; then
  echo "Cut-out: needs Python 3.10 or newer (this one is $("$PY" -c 'import platform; print(platform.python_version())' 2>/dev/null)). Previews are skipped; the range still shows colors, checks and shapes."
  exit 1
fi
if [ "$PY" = "$V" ]; then
  "$V" -m pip install --quiet "rembg[cpu]" 2>/dev/null
else
  python3 -m pip install --user --quiet "rembg[cpu]" 2>/dev/null
fi
if "$PY" -c "import rembg" 2>/dev/null; then
  echo "Cut-out: installed. The first preview downloads the model once (about 170 MB)."; exit 0
fi
echo "Cut-out: could not install it automatically. Previews are skipped; the range still shows colors, checks and shapes."
exit 1
