#!/usr/bin/env bash
# Adds the Visual Brain to a workspace folder (default: the current folder).
# Order: .gitignore block first, then the template files, then the CLAUDE.md section, then the image library.
# Never overwrites the owner's files. Files written by an older Visual Brain are kept in projects/visual-brain/archive/.
set -e
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$PWD}"
cd "$TARGET"
if [ "$PWD" = "$ROOT" ]; then
  echo "This is the plugin's own folder. Run setup in your brand workspace instead." >&2
  exit 1
fi
DATE="$(date +%Y-%m-%d)"
ARCH="projects/visual-brain/archive"

[ -f CLAUDE.md ] || { printf '# CLAUDE.md\n\nInstructions Claude reads in this folder.\n' > CLAUDE.md; cm_new="created"; }

# 1. Image files stay local: the gitignore block goes in BEFORE raw/visuals/.
touch .gitignore
if grep -qx 'raw/visuals/\*' .gitignore; then gi="already there"; else
  printf '\n' >> .gitignore; cat "$ROOT/plugin/gitignore-block.txt" >> .gitignore; gi="added"; fi
# Lines added in later versions go in once each.
while IFS= read -r line; do
  case "$line" in ''|'#'*) continue ;; esac
  grep -qxF -- "$line" .gitignore || { printf '%s\n' "$line" >> .gitignore; gi="updated"; }
done < "$ROOT/plugin/gitignore-block.txt"

# 2. An older Visual Brain project file (0.4, with product commands) is kept in the archive and replaced.
old=""
if [ -f projects/visual-brain/visual-brain.md ] && grep -qE '/visual-brain:(listing|audit)' projects/visual-brain/visual-brain.md; then
  mkdir -p "$ARCH"; mv projects/visual-brain/visual-brain.md "$ARCH/visual-brain-project-$DATE.md"; old="project file archived"
fi

# 3. Template files, skipping anything that exists.
created=0; kept=0
while IFS= read -r -d '' src; do
  rel="${src#"$ROOT/templates/"}"
  if [ -e "$rel" ]; then kept=$((kept+1)); continue; fi
  mkdir -p "$(dirname "$rel")"; cp "$src" "$rel"; created=$((created+1))
done < <(find "$ROOT/templates" -type f -print0)
mkdir -p raw/visuals/own raw/visuals/screens raw/visuals/direction raw/visuals/boards

# 4. The Visual Brain section in CLAUDE.md: add it, or replace an older one (a copy is kept).
if grep -qE '^## Visual Brain' CLAUDE.md; then
  if grep -qE '/visual-brain:(listing|audit)' CLAUDE.md; then
    mkdir -p "$ARCH"; cp CLAUDE.md "$ARCH/CLAUDE-$DATE.md"
    python3 - "$ROOT/plugin/claude-md-section.md" <<'PY'
import re, sys
new = open(sys.argv[1]).read().strip("\n") + "\n"
s = open("CLAUDE.md").read()
m = re.search(r"^## Visual Brain[^\n]*\n.*?(?=^## |\Z)", s, flags=re.S | re.M)
if m:
    s = s[:m.start()] + new + ("\n" if m.end() < len(s) else "") + s[m.end():]
else:
    s = s.rstrip("\n") + "\n\n" + new
open("CLAUDE.md", "w").write(s)
PY
    cm="updated (the old section is kept in $ARCH/CLAUDE-$DATE.md)"
  else cm="already there"; fi
else
  printf '\n' >> CLAUDE.md; cat "$ROOT/plugin/claude-md-section.md" >> CLAUDE.md; cm="added"
fi

echo "Folder: $TARGET"
echo ".gitignore block (images and built pages stay local): $gi"
echo "Files created: $created. Existing files kept: $kept.${old:+ Older Visual Brain $old.}"
[ -n "${cm_new:-}" ] && echo "CLAUDE.md: $cm_new"
echo "CLAUDE.md Visual Brain section: $cm"
for f in wiki/brand/icp.md wiki/brand/positioning-messaging.md; do
  if [ ! -f "$f" ] || grep -q '^status: template' "$f"; then
    echo "Not drafted yet: $f (Marketing Brain). /visual-brain:brand waits for it."
  fi
done
bash "$ROOT/plugin/ensure-pillow.sh" || true
