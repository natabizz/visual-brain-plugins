---
description: Add the Visual Brain to your workspace. Adds the visual direction template, the landscape files, the local-only raw/visuals folder and a Visual Brain section in CLAUDE.md, and makes sure the image tools work. Never overwrites your files.
---

# /visual-brain:setup

Add the Visual Brain to the workspace in this folder.

1. **Check the folder.** The Visual Brain builds the look from the Marketing Brain's buyer and position. Look for `wiki/brand/icp.md` and `wiki/brand/positioning-messaging.md`.
   - Both drafted: say so in one line and continue.
   - Missing or still templates: say the look is built from the audience and the position, so Marketing Brain exercises 1 and 2 come first. Setup still runs; `/visual-brain:brand` will wait for them.
2. **Run the setup script** and show its output:
   `bash "${CLAUDE_PLUGIN_ROOT}/plugin/setup.sh" "<this folder's absolute path>"`
   It adds `raw/visuals/` to `.gitignore` before any image lands there, copies the templates without overwriting, updates an older Visual Brain section in `CLAUDE.md` (keeping a copy), and installs the image library the scripts need. If bash is not available (Windows), say in one line that the plugin is built for macOS and Linux, and stop.
3. **Say the next step,** in at most three lines:
   - "Run `/visual-brain:brand`. It reads your brand files, studies your audience and the market by itself, and asks only for what it can't find."
   - "Brands you look up to, a moodboard, photos: attach them in the chat when it asks. Nothing is required."
   - "Product images and galleries live in the companion plugin, Product Visual."
4. If the folder is a git repo, show `git status --short` and ask whether to commit ("Add the Visual Brain"). Commit only on a yes.
