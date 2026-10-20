---
description: Product Visual. Rebuild a product's page from its files, in the owner's language or another one (for example English for colleagues), without new research.
argument-hint: "<product> [language, for example en]"
---

# /product-visual:page

Make a product's page again from what `/product-visual:new` and `/product-visual:gallery` already wrote. No new research, no new tests.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md`, section "Writing the pages", first.

1. **Which product.** If none was named, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which product?
2. **Check the files.** `projects/product-visual/<product>/positioning.md` and `direction.md` must be filled. If not, say in one line that `/product-visual:new <product>` comes first, and stop.
3. **Language.** The second argument names it (`en`, `ru`, `es`...). Without one, use the language the owner writes in.
4. **Source.** If `projects/product-visual/outputs/<product>.src.html` exists, translate it: every label and line into the language; customer quotes stay verbatim, with a short translation under them only when the language differs from the quote's; text inside mockups stays in the customer's language; brand, product and line names stay. If it does not exist, fill `${CLAUDE_PLUGIN_ROOT}/frameworks/product-book-template.html` from the files as `/product-visual:new` step 8 describes.
5. **Write** `projects/product-visual/outputs/<product>.<lang>.src.html`, then build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 760 --out projects/product-visual/outputs/<product>.<lang>.html projects/product-visual/outputs/<product>.<lang>.src.html`.
6. **Check** that nothing new was added: every line on the page is in the files or on the source page.
7. **Share:** if this session can publish an Artifact, publish it as a private artifact titled "[Product] Visual" (add the language in the description) and give the link; otherwise give the file path.

Close in two lines: where the page is, and that sharing it with colleagues is done from the page's Share menu.
