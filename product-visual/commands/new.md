---
description: Product Visual. Build a product's visual from scratch - who it is for and what they need to see, the product's positioning and UVP, a visual direction (what to show and how) with options, then a storyboard of its images frame by frame with a brief per frame, on one page. For any channel - a marketplace, the brand's site, search, social or ads.
argument-hint: "<product> [main channel]"
---

# /product-visual:new

Build the visual side of one product from zero: people first, frames last.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md` in full first: needs, positioning, direction, the gallery rules, the tests, Gate PV, how to write the page. Apply the Marketing Brain's `frameworks/quality-rules.md` Gate 0 to text lines when the workspace has it.

Talk to the owner in the language they write in. Write the files and the page in the language of the brand's customer-facing copy.

Keep the chat short: one line per step ("Step 3 of 8: competing products, 6 found"). When you need the owner, the message ends with a line that starts **"Waiting for you:"** with the exact question, and nothing after it.

Agents can't list a folder: always give them file paths.

## 0. Before you run

1. **Setup, every time.** Run `bash "${CLAUDE_PLUGIN_ROOT}/plugin/setup.sh" "$PWD"`. It never overwrites the owner's files. Mention its output in one line only if it changed something.
2. **Which product.** If no product was named, list the products in `projects/product-visual/` and end with **"Waiting for you:"** which product? The slug is the product name, lowercase, hyphens (`wool-beanie`).
3. **The product folder.** If `projects/product-visual/<product>/` exists, read every file in it: this is a rebuild, and Decisions are kept. If not, copy `projects/product-visual/_template/` to it and add the product to the table in `projects/product-visual/product-visual.md`.
4. **An earlier job.** If `projects/visual-brain/jobs/<product>-*/` exists (an earlier Visual Brain version), read it and carry over, citing "earlier job, <file>": facts from its `facts-sheet.md` with their original sources, its AI-reading panel into `ai-read-<channel>.md`, its open issues into `issues.md`, its audit findings as evidence. Never delete the old folder.
5. **The brand.** Read `wiki/brand/icp.md`, `wiki/brand/positioning-messaging.md`, `wiki/brand/voice-guide.md` and `wiki/brand/vocabulary.md` when present, and `wiki/brand/visual-guide.md` with `projects/visual-brain/landscape/audience.md` and `landscape.md`.
   - No drafted ICP or hub: stop, and say Marketing Brain exercises 1 and 2 come first.
   - No visual guide, or one without `format: visual-brain-2` in its front matter (an earlier version): continue, mark brand-look checks "(limited: no brand look)", and recommend `/visual-brain:brand` in the summary.
   - A guide in `format: visual-brain-2` without `stage: chosen` (or later): say in one line that the brand's direction is not chosen yet, and end with **"Waiting for you:"** run `/visual-brain:choose` first, or say go to work on the recommended direction (tagged (inferred) wherever it is used).
   - A chosen direction: read what the framework lists under "The chosen direction" (the look, the cast and its lead, the caption rule, what was handed to Product Visual, what to do next and the first shoot list, the owner's Decisions, the rival tests) and note each with its section, for `product.md`'s inputs.
6. **Find it yourself, without asking:**
   - **Facts:** search the workspace for the product's name and its variants: `raw/strategy/`, `raw/brand/`, `raw/voc/`, product facts files, size charts, label photos, spec sheets, the hub and the ICP. Note each fact with its file.
   - **Photos:** image files of this product in `raw/visuals/` and elsewhere in the workspace.
   - **Its pages:** if the product is already live anywhere, find the pages.
   - **Reviews and questions:** the brand's own for this or the nearest product, in `raw/voc/` and on its pages.
   - **Competing products:** the same product type from the shelf and reference brands in `landscape.md` and the hub, and a buyer search on the main channel. Aim for five to eight.
   - **The owner's direction:** moodboards and notes for this product in `raw/visuals/direction/`, `raw/strategy/`, `raw/brand/`.
   - **Probe access now:** try each competing product page (`curl -sL -o /dev/null -w "%{http_code}"`, or a web fetch). Note which refuse, so screenshots can be asked for once, now.
7. **One short summary, then wait:**
   - **Found:** facts (with sources), photos (count), pages, reviews, competing products (one line why each), the owner's direction.
   - **Missing:** in plain words. Separate the **essentials** (what it is, material, sizes and how to choose, variants, price) from the optional.
   - **Blocked:** pages that refuse automated viewing: "if you can, attach screenshots of their galleries".
   - **Questions, only what you could not find,** numbered, at most five. Always include, unless already answered: where the product lives and which place comes first ("a marketplace (which one), your own site, Google, social or ads, or something else; the others can follow"), and "Do you have real photos of the product? Drag them from Finder into this chat." Moodboards and ideas: welcome, never required.
   - "Say go to continue with what I found."
   - Last line: **"Waiting for you:"** the questions in one line, or go.
8. **Go.** Say in one line what arrived and where it was filed (framework, "Files from the owner"). Convert HEIC to JPEG when filing (`sips -s format jpeg <in> --out <out.jpg>`). If an essential fact is still missing, continue and mark everything that depends on it "(limited: no facts)": those claims stay off the images.

## 1. Facts

Fill `product.md`'s Facts table, one source per value. Text on a live listing is not a source. Where two sources disagree, write both under Discrepancies (a size chart against a card that names a size, two charts on two channels). Record the main channel's kind (framework, Channels) and its rules (count, sizes, first image rules) from the channel's own page, with URL and date; behind a sign-in, ask once for a screenshot; a third-party guide only tagged as such.

## 2. Who it is for, and what they need

Write `audience.md`:
1. **Who:** the segment from `icp.md` this product serves first, and who else, with evidence. Who it is not for.
2. **Needs, ranked:** pains, desires, objections, triggers, from the sources in the framework's order. Read the competing products' reviews and questions on their pages (or the proxy files in `raw/voc/`). Each need: count, a verbatim quote cited by platform, product and date, and the source IDs. No customer names, emails or order numbers. Review photos and posts of private people are described, never saved.
3. **Vibe:** from the Visual Brain's `audience.md`, and what is specific to this product (a season, an occasion, a use).
4. **Quotes for the panel:** the most telling verbatim quotes, for the audience panel and the skeptic.

## 3. What competitors say and show

Write `market.md`. For each competing product:
- **What it says:** title, the main promise, claims with proof status as visible on the page, price, rating and review count with the date.
- **What it shows:** its whole gallery, saved to `raw/visuals/screens/<brand>/<date>/` and indexed in `projects/visual-brain/landscape/frames.md` (in the columns the table already has). Image URLs with `curl -L`, then a connected browser tool, then the owner's screenshots. Never work around a refusal. Open every image.
- **Which ranked needs its gallery answers,** and which it leaves open.
Then the patterns: what most galleries do, and **the needs nobody's gallery answers.**

## 4. Positioning and UVP

Write `positioning.md`:
1. The product's job in one sentence: for whom, against what, why this one.
2. **Two or three UVP options,** each with the need it answers, what makes it true, the proof, and how competitors talk about it.
3. **Recommended,** with the reason.
4. **Messages:** main and up to three supporting, in the voice guide's words.
5. **Claims allowed and not allowed,** each with its source.
6. Run the `product-visual:skeptical-buyer` agent with the paths of `positioning.md`, `audience.md` and `market.md`. Record its reasons; an objection no UVP answers goes under "Open".

## 5. Visual direction

Write `direction.md`:
1. Two or three options, as the framework describes: hero story, supporting stories (each tied to a need or the UVP), how it looks within the brand's look, why it fits, how it differs, what it asks for, risk. With a chosen brand direction, the options keep its look and cast and differ in what the images tell.
2. **Images per option:** six to nine, listed in `direction.md`: the product's own clean photos first where they show the idea; references and competitors where they don't, marked as such. The page shows them one by one.
3. **Audience panel:** decide the logo boxes of these images by looking, and write them to `raw/visuals/boards/<date>-<product>-masks.json`. For each option, a board without labels, logos masked: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/board.py" --out raw/visuals/boards/<date>-<product>-panel-<n> --no-labels --masks <masks file> --cols 3 <ID=path> ...`. Shuffle which option becomes board 1, 2, 3, copy them to `raw/visuals/boards/<date>-<product>-panel/board-1.jpg` and so on, and keep the mapping in `raw/visuals/boards/<date>-<product>-panel-key.json` (outside that folder). Run the `product-visual:audience-panel` agent with the path of `audience.md` and the board paths. It returns two ranks: "stops me" and "answers my worry"; record both.
4. **Rival test:** the `product-visual:rival-director` agent as the strongest competing product, with the board paths, the recommended UVP, and a two-line description of each option.
5. **Recommended,** with the reason, weighing the "stops me" rank, the "answers my worry" rank and the rival test. If the panel did not rank it first on either, or the rival could wear it, say why it stays, or recommend another.

## 6. The storyboard

For the main channel, on the recommended positioning and direction (tagged (inferred) until the owner chooses), write `gallery-<channel>.md` from `_gallery.md` as the framework's "The storyboard" describes:
- **Count** and why: the ranked needs and stories, the channel's dated limit, the owner's number.
- **One card per frame,** in the order of the buyer's path: job, need with its quote, in frame, view, who, text, look, proof, the image in hand or "To shoot: what", route, copyable.
- **The first frame** follows the channel's first image rules; where they differ from the chosen look (a plain white ground on a marketplace, say), the look starts at the second frame, and the file says so with the rule's source.
- **The cast and the caption** from the chosen direction: only its cast, its lead on the first frame, its caption rule on brand frames, the measurements only on the proof frames handed over.
- **Views check:** the views this product's buyers need to see, from the ranked needs and their questions; each covered by a frame, or moved to the listing text with the reason.
- **Proof frames handed over** by Visual Brain each get a frame, or the file says why not.
- One brief per frame in `briefs/<channel>/frame-NN.md` from `briefs/_brief.md`.
- Where the plan needs a real photo the owner doesn't have, the frame says "To shoot", and the shot list goes at the end of the gallery file, grouped by setup and joined to the brand's first shoot list where a setup repeats.
- Run the `product-visual:rival-director` agent on the first frame's and the hero frame's briefs, and the `product-visual:skeptical-buyer` agent on the plan (file paths). Mark each frame "copyable" or not from the rival's answer. Each objection either has a frame that answers it or is listed as open.

## 6b. What to do next

In `gallery-<channel>.md`, under "What to do next": up to six actions grouped now, next, later, each with its basis and what it takes. Fixes to facts buyers see today (a size chart that disagrees with itself or with a card, a claim without proof) go first under "now". Then the shot list.

## 7. Judge

Run the `product-visual:gate-judge` agent with the paths of `product.md`, `audience.md`, `market.md`, `positioning.md`, `direction.md`, the gallery file, the briefs, the test results, `wiki/brand/visual-guide.md` and `${CLAUDE_PLUGIN_ROOT}/frameworks/product-visual.md`: Gate PV, checks PV.1 to PV.6, PV.8, PV.10 to PV.15 (PV.14 runs on the page in step 8). Rewrite what the inputs can fix; what they can't goes to "To check and decide" in plain words. Every finding into `issues.md`. Set `stage: planned` in `product.md` when no blocking check fails.

## 8. The page

Copy `${CLAUDE_PLUGIN_ROOT}/frameworks/product-book-template.html` to `projects/product-visual/outputs/<product>.src.html` and fill it from the files, in the language the owner writes in. Keep its style, structure and script; follow the instructions in its first comment; delete the template comments and unused blocks.
- Option palettes: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/palette.py" --colors 6 <the option's images>`; use "Palette for the set".
- Carriers, by the main channel's kind (framework, Channels): a marketplace search card next to three competitor cards (their real titles and prices, dated) and the gallery; or the own site's product page first screen and gallery strip; or a search result among three competitors; or a social carousel in a phone. Columns: "as everyone", "now" (when live) and each option. Only real titles, prices and facts on mockups. Clean carriers: the brand's columns take only the product's own images, the first image a clean photo; a missing photo is a "To shoot" color tile; competitors only in "as everyone" and as competitor cards.
- The storyboard section: one card per frame with all its fields, the views table under it. Then "What to do next" and the shot list.
- Run PV.14 yourself on the filled page before building: no other brand's image in a brand column, no line that isn't the brand's own or a sourced fact.
- Images: `src="file:<path>"`. Build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 760 --out projects/product-visual/outputs/<product>.html projects/product-visual/outputs/<product>.src.html`. Never paste image data or print it in the chat.
- Plain words: no IDs, codes or tags. Quotes cited by platform, product and date. Check every claim on the page against the files.

Share it: if this session can publish an Artifact, publish it privately titled "[Product] Visual" and give the link; otherwise give the file path and say to open it in a browser.

## 9. Close

At most five lines, in this order:
- The recommended positioning and direction in one line each, and the other options by name.
- The storyboard: number of frames, how many need a shoot, and the first action under "now".
- What was missing, if anything.
- The page link; the files are in `projects/product-visual/<product>/`.
- **"Waiting for you:"** which positioning and which direction do you choose?

On the answer: record both in Decisions with the date and set `stage: chosen`. If the positioning differs from the recommended one, redo steps 5 and 6 on it; if only the direction differs, redo step 6 (or run `/product-visual:gallery <product> <channel>`). Rebuild the page and say so in one line.
