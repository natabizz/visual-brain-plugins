---
description: Visual Brain. Rebuild the direction page from the files, in the owner's language or another one (for example English for colleagues), without new research.
argument-hint: "[language, for example en] [public]"
---

# /visual-brain:page

Make the direction page again from what `/visual-brain:brand` already wrote. No new research, no new tests.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/visual-brain.md`, section "Writing the page", first.

0. **One run at a time.** If `projects/visual-brain/.run-lock` exists and is less than three hours old, another chat is working on these files: say so in one line, with the command and time it holds, and stop, unless the owner says that run is finished. Otherwise write the lock (the command and the time) and delete it when this run closes, also when it stops early.
1. **Check the files.** `wiki/brand/visual-guide.md` must have `format: visual-brain-2` and filled directions. If not, say in one line that `/visual-brain:brand` comes first, and stop.
2. **Language.** The argument names it (`en`, `ru`, `es`...). Without one, use the language the owner writes in.
3. **Source.** If `projects/visual-brain/outputs/visual-direction.src.html` exists and is newer than `visual-guide.md` and the landscape files, translate it; if it is older, fill it again from the files first, as `/visual-brain:brand` step 9 does, then translate: every label and line into the language; customer quotes stay verbatim, with a short translation under them only when the language differs from the quote's; text inside mockups stays in the customer's language; brand and product names stay. If it does not exist, fill `${CLAUDE_PLUGIN_ROOT}/frameworks/direction-book-template.html` from the `.md` files as `/visual-brain:brand` step 9 describes.
4. **Write** `projects/visual-brain/outputs/visual-direction.<lang>.src.html`, then build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 760 --out projects/visual-brain/outputs/visual-direction.<lang>.html projects/visual-brain/outputs/visual-direction.<lang>.src.html`.
5. **Check** that nothing new was added: every line on the page is in the files or on the source page.
5b. **A public version** (`public` in the argument): for a page that may leave the team (a repository, a post, a talk). Leave out every image of another brand (keep the brand names, the patterns and the counts in words), the customer quotes beyond a short line each, and "To check and decide", the discrepancies and the open issues of the brand's own materials. Write it as `visual-direction.<lang>.public.src.html` and build it the same way. Without `public`, say in one line before sharing that the page holds other brands' images and the brand's open issues, for internal review only.
6. **Show:** if this session can publish an Artifact, publish it as a private artifact (only the owner sees it) titled "[Brand] Visual Direction" (add the language in the description) and give the link; otherwise give the file path.

Close in two lines: where the page is, and that sharing it with colleagues is done from the page's Share menu.
