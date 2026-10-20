#!/usr/bin/env bash
# Adds Product Visual to a workspace folder (default: the current folder).
# Order: .gitignore block first, then the template files, then the CLAUDE.md section, then the image library.
# Never overwrites the owner's files.
set -e
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-$PWD}"
cd "$TARGET"
if [ "$PWD" = "$ROOT" ]; then
  echo "This is the plugin's own folder. Run setup in your brand workspace instead." >&2
  exit 1
fi
[ -f CLAUDE.md ] || { printf '# CLAUDE.md\n\nInstructions Claude reads in this folder.\n' > CLAUDE.md; cm_new="created"; }

touch .gitignore
if grep -qx 'raw/visuals/\*' .gitignore; then gi="already there"; else
  printf '\n' >> .gitignore; cat "$ROOT/plugin/gitignore-block.txt" >> .gitignore; gi="added"; fi

created=0; kept=0
while IFS= read -r -d '' src; do
  rel="${src#"$ROOT/templates/"}"
  if [ -e "$rel" ]; then kept=$((kept+1)); continue; fi
  mkdir -p "$(dirname "$rel")"; cp "$src" "$rel"; created=$((created+1))
done < <(find "$ROOT/templates" -type f -print0)
mkdir -p raw/visuals/products raw/visuals/screens raw/visuals/direction raw/visuals/boards

if grep -qE '^## Product Visual' CLAUDE.md; then cm="already there"; else
  printf '\n' >> CLAUDE.md; cat "$ROOT/plugin/claude-md-section.md" >> CLAUDE.md; cm="added"; fi

echo "Folder: $TARGET"
echo ".gitignore block for raw/visuals/: $gi"
echo "Files created: $created. Existing files kept: $kept."
[ -n "${cm_new:-}" ] && echo "CLAUDE.md: $cm_new"
echo "CLAUDE.md Product Visual section: $cm"
for f in wiki/brand/icp.md wiki/brand/positioning-messaging.md; do
  if [ ! -f "$f" ] || grep -q '^status: template' "$f"; then echo "Not drafted yet: $f (Marketing Brain). Product Visual needs it."; fi
done
if [ ! -f wiki/brand/visual-guide.md ] || grep -q '^status: template' wiki/brand/visual-guide.md; then
  echo "No brand look yet (wiki/brand/visual-guide.md). Recommended first: /visual-brain:brand."
elif ! grep -q '^format: visual-brain-2' wiki/brand/visual-guide.md; then
  echo "The brand look is from an earlier Visual Brain version. Recommended: run /visual-brain:brand again."
fi
if [ -d projects/visual-brain/jobs ]; then
  echo "Found projects/visual-brain/jobs/ from an earlier Visual Brain version: kept. Product Visual reads a product's earlier job when you work on that product."
fi
bash "$ROOT/plugin/ensure-pillow.sh" || true
