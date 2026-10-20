---
description: Product Visual. Check finished or draft images against the briefs, the product facts and the real photos, run the shelf, rival and AI-reading tests on the finished set, and prepare a release list - without publishing.
argument-hint: "<product> <channel>"
---

# /product-visual:qa

Check the made images before anyone uploads them. Unknown is not pass.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` first. Talk to the owner in their language. One line per step. When you need the owner, the message ends with a line that starts **"Waiting for you:"**, and nothing after it. Agents get file paths, never folders.

## 0. Before you run

1. If the product or channel is missing, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which one? Read `projects/product-visual/<product>/`. Without `gallery-<channel>.md` and `briefs/<channel>/`, stop: QA checks images against a plan. Point to `/product-visual:gallery`.
2. **The images:** attached in the chat (dragged from Finder), or already in `raw/visuals/products/<product>/drafts/<channel>/` or `finished/<channel>/`. File each attachment there named by its frame number in the gallery plan (`01.jpg`, `02.jpg`). An attachment without a file path can only be looked at: say which checks can't run on it. If an image is missing, QA runs on the rest and lists the missing frames.
3. Say which version of each image you check (file name and modified date), and go.

## 1. True to the product

For each image, open it and the real photos its brief names, and compare variant, color, construction, details, proportions and scale against `product.md`. Zoom where needed. Each item: pass, fail, unknown (can't be seen at this resolution) or not applicable. A generated or retouched image that changes the product is "redo", however good it looks.

## 2. Against the brief

- Exact text on the image, letter by letter, against the brief.
- The direction: does it look like the chosen direction and the brand's look?
- Size and format: real pixel dimensions, read with `sips -g pixelWidth -g pixelHeight <file>` (or Pillow), not from the file name.
- **Mobile:** resize a copy to the size the channel shows on a phone and look at it. Text that can't be read at that size is "needs work".

## 3. Claims

Every visible claim, including icons, badges and scenes, against `product.md`. A claim that crept in during production without proof means "needs work". A fit or size demonstration must be a real photo, never generated.

## 4. Tests on the finished set

1. **Blind shelf:** the new main image against the same competing mains and size as the audit's shelf, reusing the `masks.json` kept in that shelf's folder for the competitors; for the new main image, and for any image that changed, look again and draw its logo boxes anew (or as `/product-visual:audit` step 3.1 if there was no shelf). Compare with the earlier result.
2. **Rival test** on the main image and the hero frame.
3. **Skeptical buyer** on the finished set: which objection is still unanswered?
4. **AI reading, mode A** on the finished set, as a new dated run in `ai-read-<channel>.md`; compare with the earlier run.

## 5. Verdicts and judge

1. Each image gets **ready**, **needs work** (exactly what, citing the check) or **redo** (why, and what the brief should change). A frame whose image is ready moves to the status "ready for production" in the gallery file and on the page; a frame at "needs work" or "redo" goes to "needs confirmation: <the finding>" when a fact or a photo behind it is unconfirmed (a claim without proof, a generated image where a real one is required), and otherwise keeps "ready to shoot" with the finding named. These are checks against briefs the owner approved, so they are stated plainly.
2. `product-visual:gate-judge` with the file paths: Gate PV, every check, PV.9 blocking. Findings into `issues.md`. Write `qa-<channel>.md` from `_qa.md`. When every image is ready and no blocking check fails, set `stage: checked` in `product.md`.

## 6. Release list

Only when every frame of the plan has a file marked "ready" (no frame missing, nothing at "needs work" or "redo") and the judge's last run has no blocking fail (`stage: checked`): list the exact files and versions, and ask, ending with **"Waiting for you:"** do you approve these files for release? On a yes, write `release-<channel>.md` from `_release.md`:

| Frame | File | Order | Size and format | Version | Alt text | Approved by | Date |
|---|---|---|---|---|---|---|---|

Alt text per image when the channel supports it, from the facts; otherwise "not used". This command does not upload or publish. Any change to an approved file sends it back through QA.

## 7. The page and close

Copy `${CLAUDE_PLUGIN_ROOT}/frameworks/review-template.html` to `projects/product-visual/outputs/<product>-<channel>-qa.html` and fill it in QA mode; images as `src="file:<path>"`, then `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/fill.py" --max 480 <page>`. Share as `/product-visual:new` step 8 does. Then at most five lines: the verdict count, what's left to do, how the main image read on the shelf compared with before, the page link, and **next:** the owner uploads, then `/product-visual:ai-read <product> <channel>` on the live listing and `/product-visual:review` once there are dated results.
