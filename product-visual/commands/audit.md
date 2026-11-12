---
description: Product Visual. Look at a live gallery through the audience's eyes - what each image does for the buyer, what it misses, how it reads on the shelf and to AI, and what is worth considering - against the product's needs, direction and competitors.
argument-hint: "<product> <channel>"
---

# /product-visual:audit

What the live gallery of one product on one channel does for its buyers today, image by image.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` first. Talk to the owner in their language; write files in the language of the brand's customer-facing copy. One line per step. When you need the owner, the message ends with a line that starts **"Waiting for you:"**, and nothing after it. Agents get file paths, never folders.

## 0. Before you run

1. **Setup, every time:** `bash "${CLAUDE_PLUGIN_ROOT}/plugin/setup.sh" "$PWD"`; mention it only if it changed something.
2. **Which product and channel.** If either is missing, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which product and channel?
3. **The product folder.** Read `projects/product-visual/<product>/`, or create it from `_template/`. Read an earlier job as `/product-visual:new` step 0.4 does. Read `business_type` in `wiki/brand/icp.md` as `/product-visual:new` step 0.5 does: service or software, stop with "Product Visual is for physical products: services and software are not supported."
4. **Find it yourself:** what `/product-visual:new` step 0.6 finds (facts, photos, reviews, probe access), plus the live listing on this channel (from the brand's pages or a search for the product name) and this channel's buyer search. Competing products come from this channel only (framework, "Competitors per channel"): the set under this channel in `market.md` when it exists, else collected in step 1.
5. **One summary, then wait** (one ask for the whole run): what you found (links, paths), what is missing (separating essentials), blocked pages, and only the questions you could not answer yourself: the label photo, the size chart, real photos ("drag them from Finder into this chat"). "Say go to continue." Last line: **"Waiting for you:"**.
6. **Go.** If `audience.md` is still a template, or `market.md` has no set for this channel, fill them first as `/product-visual:new` steps 1 to 3 do (facts, needs, and competitors on this channel), without asking again: an audit judges images against the buyers' needs. Positioning and direction are optional here; without them the audit says "(limited: no direction)".

## 1. Collect

The whole live gallery, every position, and the full galleries of three to five competing products from this channel's set in `market.md`. With no set for this channel, collect one now with this channel's own search for the category as a buyer would type it, and write it into `market.md` under this channel with the date and how it was found; when it can't be collected, the comparisons say "(limited: no competitors for <channel>)". Never use another channel's set. Image URLs with `curl -L`, then a connected browser tool, then the owner's screenshots; never work around a refusal. Save to `raw/visuals/screens/<brand>/<date>/`, index in `frames.md` (in its existing columns), open every image. Record the channel's image rules with URL and date in `product.md`.

## 2. What each image does

For each image of ours, in `audit-<channel>.md` (from `_audit.md`):
- **What it does for the buyer:** which ranked need from `audience.md` it answers, with the quote.
- **What it misses:** a need it could answer and doesn't; something a buyer could misread.
- **True to the product?** Variant, color, construction, scale, against `product.md` and the real photos.
- **Claims:** every visible claim, including icons, badges and scenes, with proof status. A claim with no proof, or one the facts contradict, is a discrepancy, stated as a fact with both sources.
- **Worth considering:** one or two options, each with its basis. Not orders: the owner decides.

Then the gallery as a whole: **needs no gallery looked at answers** (opportunity), **needs competitors answer and we don't** (where we lag), **images that answer no need,** and, when the brand has more than one line, **whether a buyer can tell this line from the brand's other one** from the galleries alone. What a competitor's page says in text that its images don't show is a separate line. Judge our images as strictly as the competitors'.

## 3. Tests

1. **Blind shelf:** the main image among the mains of this channel's set, for this channel's buyer search. Measure the thumbnail size from a mobile screenshot when there is one, else 360 px and say so. Decide logo boxes by looking, write them to a masks file, and build it: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/shelf.py" --out raw/visuals/shelf/<date>-<product>-<channel> --size <px> --masks <file> <ID=path> ...` (the masks are kept in that folder for later runs). Run the `product-visual:fresh-eyes` agent with the file paths the script printed, the channel and the search: per letter, what is it, who is it for, which would you open first and why; then "One of these says: [the positioning line, or the hub's line]. Which one?" Score against `key.json`, which only you read. Offer the human version once.
2. **Rival test:** `product-visual:rival-director` as the strongest competing product of this channel's set, with the paths of our gallery images and theirs.
3. **Skeptical buyer:** `product-visual:skeptical-buyer` with the paths of `audit-<channel>.md`, `audience.md` and our images; as a retail buyer when the framework's "A retail buyer for B2B" applies.
4. **AI reading, mode A:** as `/product-visual:ai-read` step 2, with the six core questions written into the agent's task (never the file that holds the correct answers). The full panel is `/product-visual:ai-read`.

## 4. Judge

`product-visual:gate-judge` with the paths of the audit, `product.md`, `audience.md`, `market.md`, the test results and the framework: the checks on the files that list `audit` under "Runs in": PV.1, PV.2, PV.3, PV.7, PV.8, PV.9 (as an observation), PV.10, PV.12. The audit page has no carriers, so PV.14 does not run. Findings into `issues.md`.

## 5. The page

Copy `${CLAUDE_PLUGIN_ROOT}/frameworks/review-template.html` to `projects/product-visual/outputs/<product>-<channel>-audit.src.html` and fill it in audit mode, in the language the owner writes in: the short version, image by image (does, misses, worth considering), the needs map against this channel's competitors, the shelf result, the AI reading, discrepancies, to check and decide. Images as `src="file:<path>"`. Build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 480 --out projects/product-visual/outputs/<product>-<channel>-audit.html projects/product-visual/outputs/<product>-<channel>-audit.src.html`. A build that reports a missing image is fixed before the page is shown. Keep the `.src.html`: `/product-visual:page` rebuilds from it. No IDs or codes. Share as `/product-visual:new` step 8 does.

## 6. Close

At most five lines: the strongest image and the biggest gap in one line each, how the main image read on the shelf, the number of discrepancies, the page link, and next: `/product-visual:new <product>` to rebuild from the audience (or `/product-visual:gallery <product> <channel>` if positioning and direction are already chosen).
