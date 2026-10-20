---
description: Product Visual. After publication, read dated results honestly, rerun AI reading, and decide one next action - without claiming that images caused a change they can't be shown to have caused.
argument-hint: "<product> <channel> [period]"
---

# /product-visual:review

What happened after the new gallery went live, what can and can't be said about it, and the one thing to do next.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` first. Talk to the owner in their language.

## 0. Before you run

1. If the product or channel is missing, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which one? Read `projects/product-visual/<product>/`, including `release-<channel>.md`. Without a publication date, ask for it.
2. Required: dated numbers for a period before and a period after publication, from the channel's own reports (views or sessions, conversion, units, returns, rating), attached in the chat as exports or screenshots; file them in `raw/performance/`. Optional: stock, price, promotions and ad changes in both periods; new reviews and questions.
3. Ask only for what is missing; end with **"Waiting for you:"**.

## 1. Are the two periods comparable?

List everything that differs besides the images: length, season, days out of stock, price, promotions, ads, a new competitor, a change to the listing text. Each is a reason the numbers might have moved without the images.

## 2. Results

`results-<channel>.md` (from `_results.md`): per metric, before, after, source, period. Say what changed, then plainly what can't be concluded: a before and after never proves the images caused it. If the channel offers a controlled image test, note it as the way to find out, with its help page and date.

## 3. Buyer signals

New reviews, questions and return reasons since publication that mention the images, the size, or a gap between the photos and the product. Quote with source IDs, no customer names.

## 4. AI reading again

Rerun `/product-visual:ai-read <product> <channel>` with the same panel; add the row to Before and after.

## 5. One next action

Choose one, with its evidence: **keep** the gallery; **change one image** (which, and what); **gather more data** (what, for how long); **pass it to product** (when complaints are about the product, not the images).

Set the stage to **validated** only when dated results support it and the comparability list names nothing that could explain the change by itself. Do not set up recurring runs, ads or tests on your own. Close in at most five lines.
