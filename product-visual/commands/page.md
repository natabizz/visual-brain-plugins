---
description: Product Visual. Rebuild a product's page, or its audit or QA page for a channel, from its files, in the owner's language or another one (for example English for colleagues), without new research.
argument-hint: "<product> [audit|qa <channel>] [language, for example en]"
---

# /product-visual:page

Make a product's page again from what `/product-visual:new` and `/product-visual:gallery` already wrote, or an audit or QA page from what `/product-visual:audit` and `/product-visual:qa` wrote. No new research, no new tests.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md`, section "Writing the pages", first.

1. **Which product.** If none was named, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which product?
2. **Which page.** Without `audit` or `qa`, the product page (steps 5 and 6). With `audit <channel>` or `qa <channel>`, that page (step 7).
3. **Check the files.** For the product page, `projects/product-visual/<product>/positioning.md` and `direction.md` must be filled. If not, say in one line that `/product-visual:new <product>` comes first, and stop. For an audit or QA page, `audit-<channel>.md` or `qa-<channel>.md` must exist; if not, point to `/product-visual:audit` or `/product-visual:qa`, and stop.
4. **Language.** The last argument names it (`en`, `ru`, `es`...). Without one, use the language the owner writes in.
5. **Source.** If `projects/product-visual/outputs/<product>.src.html` exists and is newer than the product's `.md` files, translate it; if it is older, fill it again from the files first, as `/product-visual:new` step 8 does, then translate: every label and line into the language; customer quotes stay verbatim, with a short translation under them only when the language differs from the quote's; text inside mockups stays in the customer's language; brand, product and line names stay. If it does not exist, fill `${CLAUDE_PLUGIN_ROOT}/frameworks/product-book-template.html` from the files as `/product-visual:new` step 8 describes.
6. **Write** `projects/product-visual/outputs/<product>.<lang>.src.html`, then build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 760 --out projects/product-visual/outputs/<product>.<lang>.html projects/product-visual/outputs/<product>.<lang>.src.html`.
7. **An audit or QA page.** The source is `projects/product-visual/outputs/<product>-<channel>-audit.src.html` (or `-qa.src.html`). If it exists and is newer than `audit-<channel>.md` (or `qa-<channel>.md`), use it; if it is older or missing (pages made before this version were built in place, without a source), fill `${CLAUDE_PLUGIN_ROOT}/frameworks/review-template.html` from the files again, as the command's page step describes. Translate as in step 5 when a language is given, writing `<product>-<channel>-audit.<lang>.src.html` (or `-qa.<lang>.src.html`); without one, write the source under its own name. Build it to the `.html` of the same name, without `.src`: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 480 --out projects/product-visual/outputs/<product>-<channel>-audit[.<lang>].html projects/product-visual/outputs/<product>-<channel>-audit[.<lang>].src.html`.
8. **Check** that nothing new was added: every line on the page is in the files or on the source page.
9. **Show:** if this session can publish an Artifact, publish it as a private artifact (only the owner sees it) titled "[Product] Visual" ("[Product] [Channel] Audit" or "QA" for those pages; add the language in the description) and give the link; otherwise give the file path.

Close in two lines: where the page is, and that sharing it with colleagues is done from the page's Share menu.
