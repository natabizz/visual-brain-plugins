---
description: Product Visual. Plan or re-plan a product's storyboard for one channel (a marketplace, the brand's site, search, social or ads) - frames from the audience's needs and the chosen direction, the count from the channel's dated limit, and one standalone brief per frame.
argument-hint: "<product> <channel>"
---

# /product-visual:gallery

Plan the storyboard for one channel, on the positioning and direction already set for this product.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` first (The chosen direction, Channels, The storyboard, What to do next, the tests, Gate PV). Talk to the owner in their language; write files in the language of the brand's customer-facing copy. One line per step in the chat. When you need the owner, the message ends with a line that starts **"Waiting for you:"**, and nothing after it. Agents get file paths, never folders.

## 0. Before you run

1. If the product or channel is missing, list the products and end with **"Waiting for you:"**. Read every file in `projects/product-visual/<product>/`. Without `audience.md`, `positioning.md` and `direction.md`, stop and point to `/product-visual:new <product>`.
2. **Which positioning and direction?** The ones in Decisions. If none is chosen yet, use the recommended ones and tag the gallery (inferred). If the owner names another option now, record it in Decisions with the date.
3. **The brand's chosen direction:** read `wiki/brand/visual-guide.md` as the framework's "The chosen direction" lists (the look, the cast and its lead, the caption rule, what was handed to Product Visual, the first shoot list, Decisions). If it changed since the product's last run (its `last_updated`), say so in one line and follow the new one.
4. **Find it yourself:** the channel's kind (framework, Channels) and its rules (image count, sizes, first image rules) from the channel's own page with URL and date, into `product.md`; a third-party guide only tagged as such; real photos and drafts in `raw/visuals/products/<product>/`.
5. If `gallery-<channel>.md` exists, this is a re-plan: keep its Decisions. A changed plan sends a product at `checked` or `validated` back to `chosen` in `product.md` (or to `planned` when nothing is chosen yet), and a `release-<channel>.md` for the old plan is marked "superseded, needs QA" at the top: an approval covers the plan it was given for.
6. **One ask, only if needed:** if the rules page can't be reached, or photos the plan obviously needs are missing, one message saying what will change and what you need (the rules link or a screenshot; "drag photos from Finder into this chat"), ending with **"Waiting for you:"**. Otherwise go straight on. Never from memory.

## 1. The plan

Write `gallery-<channel>.md` from `_gallery.md`:
- **Count:** the ranked needs and the direction's stories, the channel's limit, the owner's number, and the working. More needs than the limit: which go to the listing text, and why. A frame with no need is dropped.
- **One card per frame, in the order of the buyer's path on this channel** (stop, understand, believe, choose, picture it in their life): job; the need it serves with a quote and source; in frame; view and crop; who (from the chosen cast, and why this one); the text (exact words in the voice guide's words, or no text, and where it sits); the look (from the direction); the proof and its source; the image in hand (a real photo path) or "To shoot: what"; the route (shoot, retouch, background only, layout); copyable or not. Fit, size, material, construction and tests are never generated.
- **The first frame** follows the channel's first image rules; where they differ from the chosen look, the look starts at the second frame, with the rule's source.
- **Views check:** the views the buyers need to see, each covered by a frame or moved to the listing text with the reason. The proof frames handed over by Visual Brain each get a frame, or the reason they don't.
- **What competitors show at this point:** the matching competitor frames from `market.md`, and how this frame differs.
- **What to do next:** up to six actions, now, next, later, each with its basis; fixes to facts buyers see today first.
- **Shot list:** every "To shoot" frame, grouped by setup (who, setting, light, backdrop), so one session covers them, joined to the brand's first shoot list where a setup repeats.

## 2. Briefs

One brief per frame in `briefs/<channel>/frame-NN.md` from `_brief.md`, every field filled. A designer, photographer or image tool must be able to work from the brief alone: real photo paths, exact text, what must not change, reference images and what to take from each, size and format, done when.

## 3. Tests and judge

1. `product-visual:rival-director` on the first frame's and the hero frame's briefs (file paths), as the strongest competing product. Mark the frames the rival saw "copyable" or not from its answer; the other frames "not tested".
2. `product-visual:skeptical-buyer` on the plan (file paths): each objection has a frame that answers it, or is listed as open.
3. Claim to proof on every planned message: a claim without proof is removed from the image.
4. `product-visual:gate-judge` with the file paths and `wiki/brand/visual-guide.md`: Gate PV, the checks on the files: PV.1 to PV.6, PV.8, PV.10 to PV.13, PV.15. Findings into `issues.md`; what the inputs can't fix goes to "To check and decide". PV.14 runs on the page in step 4.

## 4. The page

Update the Carriers, Storyboard and What to do next sections of `projects/product-visual/outputs/<product>.src.html` (from `${CLAUDE_PLUGIN_ROOT}/frameworks/product-book-template.html`) for this channel: the carrier for the channel's kind (framework, Channels), clean, with "To shoot" tiles where photos are missing; the frames in order, each card with all its fields and the image in hand or the "To shoot" tile; the views table; the actions and the shot list. Keep the other sections. Images as `src="file:<path>"`, then build with `embed.py` as `/product-visual:new` step 8 does. Share it the same way. Before building, run the `product-visual:gate-judge` agent on the page source (the `.src.html`, never the built page), the gallery file and the framework: PV.14; fix, then build.

## 5. Close

At most five lines: the number of frames and why, how many need a shoot, the first action under "now", the open objections, the page link, and next: make the images, then attach them in this chat named by frame number (`01.jpg`, `02.jpg`) and run `/product-visual:qa <product> <channel>`.
