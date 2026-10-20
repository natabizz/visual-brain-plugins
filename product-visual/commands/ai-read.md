---
description: Product Visual. Check how AI reads a listing - from the images alone, then with the text, then on the open web - scored against the product facts, before and after a change.
argument-hint: "<product> <channel> [a|b|both]"
---

# /product-visual:ai-read

Does AI read this product correctly? Mode A: from the listing's own images and text. Mode B: from the open web, the way a shopping assistant answers. The two are scored separately and never mixed.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` first. Talk to the owner in their language.

## 0. Before you run

1. If the product or channel is missing, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which one? Read `projects/product-visual/<product>/product.md`. Its key facts are required: what it is, material, measurements, sizes and how to choose, variants, who it is for. If they are blank, say which, and end with **"Waiting for you:"** attach the label, the size chart or the spec here.
2. **Mode:** `a`, `b` or `both` (default `both`).
3. **Images and text** for mode A: the live gallery, or the drafts (attached in the chat or in `raw/visuals/products/<product>/drafts/<channel>/`), and the listing text saved as `raw/visuals/ai-read/<product>-<channel>/<date>/listing.txt` (next to the images folder, not inside it). Say which you read and its date.

## 1. The question panel

If `ai-read-<channel>.md` already has a panel, reuse it unchanged, so runs compare; otherwise start it from `_ai-read.md`. A new panel has six core questions:
1. What is this product, and what does it do?
2. Who is it for (and who or what it is used with, when that matters)?
3. What is it made of?
4. How do I choose the size?
5. How is it different from [the brand's neighboring line, when there is one]?
6. Which claims does the listing make, and which can you check?

Add up to four from the top of the ranked needs in `audience.md`. For each question, write the correct answer from `product.md`, with the field it comes from.

## 2. Mode A: the listing itself

1. Copy the images to `raw/visuals/ai-read/<product>-<channel>/<date>/images/` as `01.jpg`, `02.jpg`: names must give nothing away.
2. Run the `product-visual:fresh-eyes` agent with the image file paths and the panel's questions written into its task. Never give it `ai-read-<channel>.md` or `product.md`: they hold the answers. **Images only.**
3. Run a new `product-visual:fresh-eyes` agent with the same image paths, the path of `listing.txt` and the same questions. **Images and text.**
4. Save both raw answers in the run folder. Score each: **correct**, **error** or **no data**; for each error, the likely source (image, text, or a conflict between them).
5. In `ai-read-<channel>.md`: the Mode A table, then: facts the images carry; facts only in the text; facts misread.

## 3. Mode B: the open web

1. **Without the brand name:** three to five questions a buyer would ask a shopping assistant for this kind of product, from the ranked needs. Does the product come up, and how is it described?
2. **By product name:** the panel questions. Are the facts right, and where did they come from?
3. Run the `product-visual:ai-shopper` agent with these questions.
4. **Other AI tools** (ChatGPT, Perplexity, Gemini, a marketplace's assistant): this command can't run them. Write the same questions to `raw/visuals/ai-read/<product>-<channel>/<date>/questions.md` with an answer table (tool, date, question, answer, sources shown). The owner can paste the answers into the chat later; then score them the same way.
5. Save raw answers with tool, date and context. In the file: the Mode B table, and where wrong facts came from (which page, which channel).

## 4. Before and after

Add this run to the Before and after table: date, mode A correct out of total, mode B correct out of total, what changed between runs. A difference shows what AI reads now; it does not show why sales moved.

## 5. Findings and close

Into `issues.md`: a fact a buyer needs to choose (size, material, who it is for) read wrong from our own images or text; the same fact missing from the images but right in the text; a wrong fact on the open web traced to one of our pages; wrong facts traced to someone else's page. Then at most five lines: mode A and B scores, whether the product came up without its name, the three changes that would fix the most answers (each naming the image or text line), and next: rerun after the change. If `questions.md` was written, the last line is **"Waiting for you:"** optional: paste the other AI tools' answers here when you have them.
