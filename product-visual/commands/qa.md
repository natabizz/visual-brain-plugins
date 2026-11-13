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

1. **Blind shelf:** the new main image against the same competing mains (this channel's set in `market.md`; never another channel's) and size as the audit's shelf, reusing the `masks.json` kept in that shelf's folder for the competitors; for the new main image, and for any image that changed, look again and draw its logo boxes anew (or as `/product-visual:audit` step 3.1 if there was no shelf; with no set for this channel, collect it first as `/product-visual:audit` step 1 does, or mark the shelf "(limited: no competitors for <channel>)"). Compare with the earlier result.
2. **Rival test** on the main image and the hero frame, as the strongest competing product of this channel's set.
3. **Skeptical buyer** on the finished set: which objection is still unanswered? As a retail buyer when the framework's "A retail buyer for B2B" applies.
4. **AI reading, mode A** on the finished set, as a new dated run in `ai-read-<channel>.md`; compare with the earlier run.

## 5. Verdicts and judge

1. Each image gets **ready**, **needs work** (exactly what, citing the check) or **redo** (why, and what the brief should change). A frame whose image is ready moves to the status "ready for production" in the gallery file and on the page; a frame at "needs work" or "redo" goes to "needs confirmation: <the finding>" when a fact or a photo behind it is unconfirmed (a claim without proof, a generated image where a real one is required), and otherwise keeps "ready to shoot" with the finding named. These are checks against briefs the owner approved, so they are stated plainly.
2. `product-visual:gate-judge` with the file paths: Gate PV, only the checks on the files that list `qa` under "Runs in": PV.2, PV.5, PV.7, PV.9 (blocking), PV.10, PV.12, PV.13, PV.18, PV.19. The page check PV.14 runs in step 7, on the page source, once it exists; PV.20 (the panel) belongs to `new` and does not run here. Findings into `issues.md`. Write `qa-<channel>.md` from `_qa.md`. When every image is ready and no blocking check fails, set `stage: checked` in `product.md`.

## 6. Release list

Only when every frame of the plan has a file marked "ready" (no frame missing, nothing at "needs work" or "redo") and the judge's last run has no blocking fail (`stage: checked`): list the exact files and versions, and ask, ending with **"Waiting for you:"** do you approve these files for release? On a yes, write `release-<channel>.md` from `_release.md`:

| Frame | File | Order | Size and format | Version | Alt text | Approved by | Date |
|---|---|---|---|---|---|---|---|

Alt text per image when the channel supports it, from the facts; otherwise "not used". This command does not upload or publish. Any change to an approved file sends it back through QA.

## 7. The page and close

1. **The QA page.** Copy `${CLAUDE_PLUGIN_ROOT}/frameworks/review-template.html` to `projects/product-visual/outputs/<product>-<channel>-qa.src.html` and fill it in QA mode, in the language the owner writes in; images as `src="file:<path>"`. Build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 480 --out projects/product-visual/outputs/<product>-<channel>-qa.html projects/product-visual/outputs/<product>-<channel>-qa.src.html`. A build that reports a missing image is fixed before the page is shown. Keep the `.src.html`: `/product-visual:page` rebuilds from it. The QA page has no carriers, so PV.14 does not run on it.
2. **The product page.** When `projects/product-visual/outputs/<product>.src.html` exists, update its frame statuses (and the finished images in the gallery strip and carrier where a frame is "ready"), then run PV.14 on that source: first yourself, then the `product-visual:gate-judge` agent with the path of the `.src.html` (never the built page), the gallery file and the framework. Fix, then rebuild it with `embed.py` as `/product-visual:new` step 8 does. When the source does not exist, PV.14 does not run.
3. Share as `/product-visual:new` step 8 does. Then at most five lines: the verdict count, what's left to do, how the main image read on the shelf compared with before, the page link, and **next:** the owner uploads, then `/product-visual:ai-read <product> <channel>` on the live listing and `/product-visual:review` once there are dated results.
