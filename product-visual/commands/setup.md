---
description: Add Product Visual to your workspace. Adds the product folder template, the local-only raw/visuals folder and a Product Visual section in CLAUDE.md, and makes sure the image tools work. Never overwrites your files.
---

# /product-visual:setup

Add Product Visual to the workspace in this folder.

1. **Check the folder.** Product Visual builds on the Marketing Brain's buyer and position (`wiki/brand/icp.md`, `wiki/brand/positioning-messaging.md`) and on the Visual Brain's look (`wiki/brand/visual-guide.md`).
   - Say in one line which are drafted. Missing ICP or hub: Marketing Brain exercises 1 and 2 come first. Missing visual guide: recommend `/visual-brain:brand`; Product Visual still works and marks brand-look checks "(limited: no brand look)".
2. **Run the setup script** and show its output:
   `bash "${CLAUDE_PLUGIN_ROOT}/plugin/setup.sh" "<this folder's absolute path>"`
   If bash is not available (Windows), say in one line that the plugin is built for macOS and Linux, and stop.
3. **Say the next step** in at most three lines:
   - "To build a product's visual from zero: `/product-visual:new <product>`. It finds what it can and asks only for what it can't."
   - "Product photos, a label, a size chart, a moodboard: attach them in the chat when it asks."
   - "For a live listing: `/product-visual:audit <product> <channel>`."
4. If the folder is a git repo, show `git status --short` and ask whether to commit ("Add Product Visual"). Commit only on a yes.
