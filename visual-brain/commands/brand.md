---
description: "Visual Brain. Build the brand's visual direction from its audience, its position, the Marketing Brain handoff card and the visual market: a change brief, then usually two directions next to the current base, each shown in layouts for social, site, ads and marketplace next to how everyone looks, into wiki/brand/visual-guide.md plus one page. Modes: foundation, task, audit. Physical products, B2C and B2B; services and software are not supported."
argument-hint: "[foundation | task <material> | audit] [quick | full] [card: <handoff card path>]"
---

# /visual-brain:brand

Build the brand's look: who we are shooting for, what the market already looks like, where the empty space is, and two or three directions that would attract this audience and that competitors can't wear, each shown on the carriers the brand uses. The logo, colors and fonts the brand has are taken as given: the directions show how to use them differently, never redesign them.

Read `${CLAUDE_PLUGIN_ROOT}/frameworks/visual-brain.md` in full first. It defines the three market groups, the eight lines of a visual language, the tests, Gate VB and how to write the page. If the workspace has `frameworks/quality-rules.md` (the Marketing Brain's), apply its Gate 0 to every text line.

Talk to the owner in the language they write in. Write the `.md` files in the language of the brand's customer-facing copy, and the page in the language the owner writes in (customer quotes stay verbatim with a short translation; text on mockups stays in the customer's language). `/visual-brain:page <lang>` makes the page in another language later.

The `.md` files are the brain; the page is a view of them. Write the files first.

Keep the chat short: one line per step ("Step 2 of 10: the market, 10 brands"). No commentary on each image. When you need the owner, the message ends with a line that starts **"Waiting for you:"** with the exact question, and nothing after it.

Agents can't list a folder: always give them file paths.

**Mode** (framework, "Modes"): `foundation` runs every step; `task <material>` runs step 0, the inputs that material needs, 4b for it, 6 for its use, 6b and the judge on the touched checks, with no new research and no new directions; `audit` runs steps 0 to 4b and stops before directions. No mode given: foundation when nothing is chosen in `state.md` or the guide, otherwise ask once which material the task is about. Say the mode and why in the first line. Depth (quick, standard, full) applies to foundation and audit.

## 0. Before you run

0. **One run at a time.** If `projects/visual-brain/.run-lock` exists and is less than three hours old, another chat is working on these files: say so in one line, with the command and time it holds, and stop, unless the owner says that run is finished. Otherwise write the lock (the command and the time) and delete it when this run closes, also when it stops early.
1. **Setup, every time.** Run `bash "${CLAUDE_PLUGIN_ROOT}/plugin/setup.sh" "$PWD"`. It never overwrites the owner's files; it adds what is missing and updates an older Visual Brain section. Mention its output in one line only if it changed something.
1b. **The state record.** Read `projects/visual-brain/state.md`; create it from `${CLAUDE_PLUGIN_ROOT}/templates/projects/visual-brain/state.md` when missing. It says what is in force, the candidates, what was rejected and why, and the inputs of the last run. Every file this run reads in step 2 and 2b is written there with its path and its `last_updated` or `git log -1 --format=%h -- <path>` (framework, "The state record"). An input that changed since the last run marks the results that rest on it "to review".
1c. **The handoff card.** When the Marketing Brain wrote a handoff card for visual work (the path given as `card: <path>`, or a `handoff-*.md` the owner names), read it: the seven questions and the Boundaries block. Its constraint type decides whether visual work is needed: "availability" or "economics" stops the run with one line saying the constraint is not a visual one and who owns it (from the card). Questions 1 to 3 (who and in what situation, what they must understand or choose, which doubt is removed) feed steps 1 and 4b; question 4 and 5 limit what images may promise; the Boundaries limit what this run may do (no publishing, no spend). The three Visual Brain fields (what stays and what changes, sources and method with status, how it is checked) are written by this run. No card: say "no handoff card: built from the ICP and hub" in the summary and go on.
2. **The brand files.** Read `wiki/brand/icp.md`, `wiki/brand/positioning-messaging.md`, and, when present, `wiki/brand/voice-guide.md` and `wiki/brand/vocabulary.md`.
   - If `icp.md` or `positioning-messaging.md` is missing or still `status: template`, stop: the look is built from the audience and the position, so Marketing Brain exercises 1 and 2 come first. Say so in two lines.
   - Note each file's `stage`. A hypothesis-stage ICP makes this a hypothesis too.
   - **Business type.** Read `business_type` from the front matter of `icp.md` (and the hub, when it has one). Services or software, B2B or B2C (an agency, a SaaS, a consultancy, an audit): stop and say in two lines: "Visual Brain covers brands that sell physical products. Services and software are not supported yet: their main visual assets are screenshots, charts and report pages, which this plugin does not judge." B2B physical product (the buyer is a retailer, a distributor or a trade buyer): run, and apply the framework's "B2B: the trade buyer" rules in every step. Missing or unclear: read it from the hub's category and the brand's channels, say in the summary which one you assumed, and ask once.
3. **Files from an earlier Visual Brain.** A guide without `format: visual-brain-3` in its front matter, or a `landscape.md` or `frames.md` without a Group column, comes from an earlier version. A `visual-brain-2` guide is read as the current base: its directions, decisions and carriers are kept as input, and the sections 0.10.0 adds (change brief, layouts by use, status axes, method status) are written by this run; until then the judge marks them "not written yet (added in 0.10.0)", a flag, never a blocking fail. Before writing anything:
   - Copy each of them to `projects/visual-brain/archive/<name>-<date>.md`.
   - Start the new guide from `${CLAUDE_PLUGIN_ROOT}/templates/wiki/brand/visual-guide.md` and the new `landscape.md` from `${CLAUDE_PLUGIN_ROOT}/templates/projects/visual-brain/landscape/landscape.md`. Carry over the old guide's Decisions table and every owner decision in it.
   - Rewrite `frames.md` in the new columns and keep every old row: group "own" for `OWN-` IDs, "shelf" for `CMP-`, "reference" for `REF-`; the old notes go into "What it shows".
   - Say in one line that the earlier files are kept in the archive.
4. **Find it yourself, without asking:**
   - **The brand's pages and images:** URLs in `raw/brand/urls.md`, `raw/brand/scraped/`, the hub and the ICP sources; then a web search for the brand name. Keep only the brand's own pages. List image files already in `raw/visuals/`.
   - **Shelf:** the hub's competitive alternatives, competitor pages in `raw/brand/off-brand/`, and who shows up when you search the brand's main channel for its category as a buyer would.
   - **References:** brands the owner has named as references anywhere in the workspace (`raw/strategy/`, `raw/visuals/direction/`, decisions in an earlier guide), premium brands in the category, and brands the audience names in `raw/voc/`.
   - **Brands AI names:** a list of brands AI assistants recommend in the category, in `raw/strategy/` or pasted in the chat (file it in `raw/strategy/ai-brand-mentions-<date>.md`, verbatim, with its source and date). Use it as the framework's "Brands AI assistants name" describes: grouped brands are collected, the long tail is listed, never collected.
   - **Adjacent:** aesthetics, accounts and brands outside the category that the ICP or the research says this audience follows.
   - **Where the audience is:** the ICP's "where they find you" (the channels they buy in) and "where they spend time", the brand's live sales channels (marketplaces, the site, wholesale), and the sources each cites. A blank field stays blank and is listed as not known: never fill it with what is typical for the category (a social network the data does not name is not a carrier).
   - **Depth:** standard unless the command was run with `quick` or `full` (framework, "Depth"). It sets how many brands and frames are collected and which tests run.
   - **The product photos:** folders of the brand's own photos the workspace or the owner's notes point to; image files in `raw/visuals/own/`. A folder the owner names is read in place and indexed by variant and cast (framework, "Photo folders").
   - **Existing direction:** moodboards and brand assets in `raw/visuals/direction/` and `raw/brand/guides/`; the voice guide's persona and signature element. A Figma or other board link the owner gives: read it with a connected Figma tool, one screenshot per frame, and file each frame in `raw/visuals/direction/` as the brand's own material; without the tool, ask once for the frames exported as images and dragged into the chat. Text and fonts on reference boards are references, not judged. A brand book the owner calls out of date is not followed.
   - **The site and social now:** the brand's live home page (a screenshot with a connected browser tool; otherwise one screenshot from the owner, optional). Social accounts found are listed in the summary and used as "now" only after the owner confirms they are the brand's or the product's.
   - **Probe access now:** for every reference and shelf brand, try its home page and one product page (`curl -sL -o /dev/null -w "%{http_code}"`, or a web fetch). Note which refuse, so the owner can be asked for screenshots once, now, instead of after the work is done.
5. **One short summary, then wait.** In this shape:
   - **Found:** the brand's pages and image count; shelf brands (one line why each); references (and who named them); adjacent; where the audience is; a list of brands AI assistants recommend, if one is in the workspace.
   - **Blocked:** sites that refuse automated viewing. "If you can, attach 3 to 5 screenshots of each: drag them from Finder into this chat."
   - **Depth and time:** "Running the standard version: about 10 brands, about half an hour to forty minutes. Say full for the wide picture (15 to 20 brands, about an hour) or quick for a first look (up to 6 brands, about twenty minutes)."
   - **Six questions, all optional:**
     1. Where are your product photos? A folder on your computer (its path, for example `/Users/you/Desktop/Brand/Photos`) or a board link. Every photo in it is looked at, by color or line and by who is in it.
     2. Which brands do you look up to, in or outside your category? (Names, links, or images.)
     3. What must not change? (Logo, colors, photos you love.)
     4. Anything you already know you want, or don't want, in the look?
     5. Do you have a list of brands AI assistants recommend in your category (from an AI visibility check)? Paste it here: it goes into the market map. Skip this one if the list was found in the workspace.
     6. Does the brand or the product have Instagram or other social accounts? Links. (Name the ones found and ask which are the brand's.)
   - "Say go to continue with what I found."
   - Last line: **"Waiting for you:"** the questions in one line, or go.
6. **Go.** Say in one line what arrived and where it was filed (framework, "Files from the owner"). Convert HEIC or other unusual image files to JPEG when filing: `sips -s format jpeg <in> --out <out.jpg>`. If an attachment has no file path, say once that the image checks need the file itself and ask to drag it from Finder into the chat; until then, list which checks can't run on it. Add every brand the owner names as a reference to References and probe it. A pasted list of brands AI assistants recommend is filed verbatim in `raw/strategy/ai-brand-mentions-<date>.md` and used as the framework's "Brands AI assistants name" describes, never added to References as a whole. Then step 1.

## 1. The audience in pictures

Write `projects/visual-brain/landscape/audience.md` (from its template if missing) from `icp.md`, the hub, `raw/voc/` and research in the places the audience spends time:
- **Vibe:** five to eight words, each with its evidence.
- **What they love to see:** recurring kinds of images in their places, with links and dates. Look at the posts, don't guess from titles. Forum and personal posts are described, never saved as images.
- **What puts them off:** with quotes and sources.
- **Where they look:** platforms and formats, and what each format asks of an image.
- **Pains and desires a look can answer** (identity level), with quotes. Leave product features to Product Visual.
- **Occasions.**
- **Quotes for the audience panel:** verbatim, cited by platform, product and date. No names, emails or order numbers.
Every line carries its source. A line the sources don't support is tagged (inferred) in the file.

## 2. The market

Collect the brands the depth allows (framework, "Depth"): owner-named references first. For each, aim for the depth's number of images (standard four to six, quick four, full six to eight): main product images, lifestyle or campaign images, the home page hero.
- **Getting images,** stopping at the first way that works for a site: the image URLs on the page with `curl -L`; a browser tool connected to this session; screenshots the owner attached. Don't work around a refusal.
- Save to `raw/visuals/screens/<brand>/<date>/<frame-id>.<ext>`, one row per image in `frames.md`.
- **Open every image.** Never describe one you have not seen.
- **Palette:** `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/palette.py" --colors 6 <files>` per brand.
- In `landscape.md`, per brand: group, why included, price point with date, the eight lines of its visual language, who it speaks to (with evidence from `audience.md`), the frames that show each line. Brands you could not get go under "Could not get" with what was tried.
- **An owner-named reference still missing** after this step: say so in one line and ask for 3 to 5 screenshots of <brand> (they can come any time before the choice). Continue, marked "(limited: no <brand>)" where it matters; when the screenshots arrive, add the brand and check the directions against it.

## 3. The map

Choose two axes from what the brands actually differ on. Place every brand, with a one-line reason. Name the empty space, or say where the least crowded position is. An empty space on the map is where the brands looked at are not, not proof that buyers want something there: write it as a hypothesis ([Г]) with how demand for it will be checked, never as an opportunity. Write it in `landscape.md` under Map.

## 4. Where you are now

Skip this step, and say so on the page, if the brand has no images.
1. The brand's own visual language by the same eight lines, from its own images, and its place on the map.
2. **Recognition test** (standard and full depth only; skipped in quick, and the page says so). Three or four images each from the brand and from two shelf brands. Decide logo boxes by looking at each image and write them to `raw/visuals/boards/<date>-recognition-masks.json`. Build a blind board: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/board.py" --out raw/visuals/boards/<date>-recognition --blind --masks <masks file> --cols 4 <ID=path> ...`. Run the `visual-brain:fresh-eyes` agent with the file paths the script printed (the board and its lettered tiles): "Group these images by brand. Say which group looks most consistent and which least, and why." Score against `key.json`, which only you read.
3. **Strengths, where it lags, discrepancies,** as the framework defines them. Judge the brand's own material as strictly as the competitors'.
4. **The site now:** when the brand has a live site, file the screenshot of its first screen under `raw/visuals/screens/site/<date>/` with a row in `frames.md`, and note up to three observations (the brand's own layout rules, the description for search and AI against the position).

## 4b. Change brief

Write the guide's section "Change brief" as the framework describes (framework, "Change brief"): every material looked at in step 4 marked keep, strengthen, fix, replace, missing or not measured, with its observation and source; then keep, strengthen, fix, remove, create, each with its basis; the expected effect; the level each item will be checked on; and what is not a visual problem, handed back to the Marketing Brain with its constraint type. The handoff card's questions 1 to 3, when there is a card, are the buyer questions here. In audit mode, the page and the close follow this step; nothing after it runs.

## 5. Directions

0. **A choice in force** (`decision: chosen` in `state.md` or the guide): do not draft new directions. Check the chosen one against the change brief and the handoff card and write "Applicability" under it: what still holds, what the brief asks it to change, each change with its basis. Then go to step 6 with the chosen direction and the current base.
1. Draft usually two directions as the framework describes, plus the current base (the brand's look now, from step 4) as the column they are compared with. A third only when the evidence leaves two genuinely different answers, with the reason on the page. Each must answer the audience (cite `audience.md`), sit somewhere on the map (cite the empty space or the move), and differ from the others in more than color. When the owner has a direction already (boards, a moodboard), its strongest part is one direction and what it lacks for this audience is another.
2. For each direction, in `visual-guide.md`: the name, the one line, three words yes and three no, six collage images (the brand's own clean frames first; the brand's own photos from the owner's boards count as own, other images on them are references; at most two references, marked, or more when the brand has fewer than four own frames, every one marked; no infographics or text-heavy listing frames), how to shoot (three rules), the signature or "none", why, how it differs, what it asks for, the risk.
3. **Palette per direction:** `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/palette.py" --colors 6 <the direction's images>`. Take the colors under "Palette for the set" (up to six, already distinct) and name each by its role in plain words. When the brand sells a range and the direction sets a rule per variant, the palette is the set of pairs from step 5b.
4. **Audience panel** (for a B2B brand, the panel plays the trade buyer: framework, "B2B: the trade buyer"). Decide the logo boxes of the panel images by looking (brand names printed on images count as logos), and write them to `raw/visuals/boards/<date>-panel-masks.json`. For each direction, a board of six images without labels, logos masked: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/board.py" --out raw/visuals/boards/<date>-panel-<n> --no-labels --masks <masks file> --cols 3 <ID=path> ...`. Shuffle which direction becomes board 1, 2 and 3, copy the boards to `raw/visuals/boards/<date>-panel/board-1.jpg` and so on, and write which is which to `raw/visuals/boards/<date>-panel-key.json` (outside that folder). The boards hold only the brand's own images and "To shoot" tiles (framework, Tests): a reference the direction relies on is shown to the panel in a second, labeled message ("another brand's image, for the idea"), never on a board. A frame not yet shot goes on the board as a tile: `<ID>=#HEX <the frame in a few words>`. With fewer than three own clean images in all, show the panel the references apart, each labeled with the board it stands for, and record the ranks as made on references. Run the `visual-brain:audience-panel` agent with `projects/visual-brain/landscape/audience.md` and the board file paths. Record both ranks ("stops me" and "answers my worry") and its words, as "the simulation suggests". If its answer shows it read something as the brand's that isn't (a test artifact), fix the boards and run it again; record both runs.
5. **Rival test.** Run the `visual-brain:rival-director` agent as the strongest shelf brand, with the panel board paths, the hub's positioning line, a two-line description of each direction, and that brand's own material: the path of `landscape.md` (its entry) and the paths of four to six of its images from `frames.md`.
6. Mark one direction **recommended** (or say the current base is enough, when the brief finds nothing to change), with the reason, what it takes from the others, and why each other direction is not recommended (the rejected options, kept on the page). A direction is a look: never recommend one for its proof frames (size cards, how-to grids); those go to "What to do next" and to Product Visual. Answer the framework's five questions (clear, advantage, believable, recognizable, producible) for each direction in a table, each cell with its evidence, weighted by the brand's main carrier; the panel's ranks and the rival's verdict are evidence, not the verdict. If the recommended one is not first on the questions the carrier weights most, say why it stays, or recommend another.
7. Write the results to `projects/visual-brain/landscape/tests-<date>.md`.

## 5b. Every variant

When the brand sells a range (colorways, lines), for the recommended direction, as the framework's "Every variant" describes:
1. For each variant, pick the clearest own photo of it and decide by looking where the product sits in it (a box as fractions of width and height). No photo: take its color from the product file.
2. Run `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/range.py" --out raw/visuals/boards/<date>-range.jpg --previews raw/visuals/boards/<date>-range "<Variant>=<photo>@<x0,y0,x1,y1>" ...` (or `"<Variant>=#HEX"`), adding `--own "<Variant>=#HEX"` per variant when the direction's rule is not a tonal backdrop, so the direction's own backdrop is the one checked (option E). It prints the pairs and the tile-size check, and writes a sheet; with the cut-out library installed, each variant's own photo is shown on every backdrop, background only. If it says the cut-out library is missing, ask once: "Previews of your photos on each backdrop need a one-time download, about 200 MB. Install it?" On yes, run `bash "${CLAUDE_PLUGIN_ROOT}/plugin/ensure-cutout.sh"` and run the range again; on no, or if it can't install, go on with the shapes (a connected image tool that removes backgrounds may make the cut-outs instead: pass those PNGs as the photos). Open the sheet and look: the check is a number, the eye decides.
3. In `visual-guide.md` under the direction: one row per variant: the product color, the rule's backdrop, the check, the passing options when the rule's backdrop fails, and the example (own photo on the backdrop; a background-replaced preview, captioned as one; a marked reference; or "To shoot" with the frame).
4. Previews are never filed as the brand's photos and never go on a carrier without the caption.

## 6. Layouts by use

Show the current base and every direction in the layouts of **all four uses** (framework, "Layouts by use"): social, site, ads, marketplace. The channels decide the order and the label, never whether a use is shown: the channels in `icp.md` "where they find you" and the brand's live sales channels are **main**; a use where the brand is live or the owner confirmed it is **confirmed**; the rest are **proposed**, with "no data yet that buyers are here". A use may be skipped only with its reason written on the page. Write in the guide under "Layouts by use" the label and source of each use, and per layout and column the images and the one text line:
- **Marketplace search tile:** a row of search results as the buyer sees them on that marketplace for the category query: "as everyone" (the first results, several brands, with their real titles and prices as seen, dated) and each direction (the brand's tile in the same row: the main image in the direction, the title the listing already uses). One block per marketplace that matters, at most two.
- **Social media grid:** "as everyone" (nine shelf images, several brands), "now" (only when the brand has its own account with posts), and each direction (nine images, at most one text tile).
- **Site first screen:** "now" (the home page screenshot, when there is a live site) and each direction: the logo (a transparent PNG from the brand's assets), a hero image, one line and a button in a band under the image, four images in a row.
- **B2B physical product:** the wholesale tile (Faire or the retailer's buyer portal, in the marketplace-tile block) and the line sheet cover (framework, "B2B: the trade buyer").
- **Feed post 4:5 and story 9:16 (social):** one post and one story or reels cover per column, with the brand's handle and a line the brand already uses.
- **Site on a phone, and the top of a product page:** the first screen at phone width; the product page top with the gallery's first image, the product's title as the store uses it, the price from the product file, the button.
- **Ads:** a feed ad 4:5 and a story ad 9:16, marked "Sponsored", with a line the brand already uses and a button; a shopping tile when the brand sells on a platform with them. Concept, budget and launch belong to Campaign Engine: the caption says so.
- **Marketplace main image and the first three frames:** per marketplace in the search-tile block, the main image and the first three gallery frames in the direction (the full gallery is Product Visual's).
- A carrier the owner names, in the same way.
Platform sizes come from a dated source (the platform's help page, with the date seen); an older one is marked.
Text on mockups: only a line the brand already uses or a fact from its files, in the customer's language, marked temporary. Follow the brand's own layout rules: text never covers the person, the animal or the product unless the brand's rules allow it.
**Clean frames only** in the brand's own columns ("as everyone" is the shelf by design): no listing infographics, badges, text-heavy frames or screenshots, and never another brand's images in a grid or a site mockup. **In hand first:** before a tile becomes "To shoot", look through the indexed own photos for that variant and that cast member. Where none fits, the tile is a color tile from the direction's palette with "To shoot:" and what exactly, in the page language. These tiles feed the shoot list. **The whole range:** with several variants, the grid shows at least three in turn, and the site's row more than one.

## 6b. What to do next

Write `visual-guide.md` section "What to do next" for the recommended direction (each shoot-list frame and each layout image names its method and the method's status, framework "Method status"; generation is marked as needing the owner's yes), as the framework describes: up to eight actions grouped now, next, later, each with its basis on the page and what it takes; fixes found in "Where you are now" belong here; the first shoot list (the first set on the main carrier, nine grid frames by default, and the site hero: what, who, where, light, the need it answers, in hand or to shoot), built from the indexed own photos first, each "to shoot" frame with the reason none in hand fits and who goes in it by the cast rule, each frame's backdrop from the pairs in 5b; the proof frames handed to Product Visual.

## 7. The visual language

For the recommended direction (tagged (inferred) until the owner chooses), write the guide's visual language: mood, palette (sampled, by role), light, setting, casting, styling, composition, type and graphics (the brand's own fonts and logo, used, never redesigned), use and avoid, by format. Every line with a reference image.

**Signature element:** up to three candidates, each tied to something only this brand has (its own animals or people, its method, an owned word, an asset). Run each through the `visual-brain:rival-director` agent. Recommend the one a rival could not wear and keep true.

## 8. Write the guide, then judge it

1. Fill `wiki/brand/visual-guide.md`: the short version (with the confidence summary: how many lines of each label, and which decisions stand on [Г]), audience, market, where you are now, directions, carriers, the visual language, what to do next, to check and decide, decisions (each with date, reason and the options rejected), sources. Every fact, claim and test result with its status and its label (framework, "Facts have a status"). Write `format: visual-brain-3`; set `status: draft`, the four axes `evidence`, `decision`, `execution`, `effect` (framework, "Status axes"; `decision: candidate` until the owner chooses), `stage` for Product Visual (simulated once the AI tests ran with no blocking fail; an older file's `tested` means the same), `last_updated`, `sources`, and `inputs:` the versions recorded in `state.md`.
2. Run the `visual-brain:gate-judge` agent with the paths of `visual-guide.md`, `audience.md`, `landscape.md`, `frames.md`, the tests file and `${CLAUDE_PLUGIN_ROOT}/frameworks/visual-brain.md`: Gate VB, the checks on the files (VB.1 to VB.7, VB.10, VB.11, VB.13, VB.15, VB.16, VB.17, VB.19 to VB.25, VB.27, VB.28); the checks on the page (VB.8, VB.9, VB.12, VB.14, VB.18) run in step 9, once the page exists; VB.26 runs at step 11.
3. Rewrite what the inputs can fix. What they can't goes under "To check and decide" in plain words. Never delete a finding from the tests.

## 9. The page

1. Copy `${CLAUDE_PLUGIN_ROOT}/frameworks/direction-book-template.html` to `projects/visual-brain/outputs/visual-direction.src.html` and fill it from the `.md` files, in the owner's language. Keep its style, structure and script; follow the instructions in its first comment; delete the template comments and unused blocks.
   - The first screen is the decision (framework, "Writing the page"): the recommended direction and its basis, what the buyer must see or feel, what it stands on, what is not known yet, the next three actions, the carriers chosen and why (and which defaults were left out). Status marks on facts and test results; "the simulation suggests" on every test line.
   - Images: `src="file:<path>"` (the image's path in the workspace). Build: `bash "${CLAUDE_PLUGIN_ROOT}/scripts/py" "${CLAUDE_PLUGIN_ROOT}/scripts/embed.py" --max 760 --out projects/visual-brain/outputs/visual-direction.html projects/visual-brain/outputs/visual-direction.src.html`. Never paste image data or print it in the chat.
   - Plain words: no frame IDs, gate codes or tags on the page. Captions say brand, what it shows, where and when. Quotes are cited by platform, product and date.
   - Check the page against the files, and run the `visual-brain:gate-judge` agent on the page source (`visual-direction.src.html`, never the built page: it holds image data) with the framework for the checks about the page (VB.8, VB.9, VB.12, VB.14, VB.18); fix, then build again: every claim is in a file; every direction and the current base have their layouts in all four uses, labeled; every direction has its collage, palette, rules and its test results; every mockup line is the brand's own; grids and site mockups hold only clean frames of the brand or "To shoot" tiles; with a range, every variant has its row, its check and its example, and the grid shows at least three variants (or every variant, when the brand has fewer); "What to do next" and the shoot list are there.
2. Show it: if this session can publish an Artifact, publish the page as a private artifact titled "[Brand] Visual Direction" (only the owner sees it; sharing it is the owner's choice) and give the link. Otherwise give the file path and say to open it in a browser.

## 10. Close

At most five lines in the chat, in this order:
- The recommended direction in one line, and the other options by name.
- What was not seen, if anything, and how to add it.
- The page link; the files are in `wiki/brand/visual-guide.md` and `projects/visual-brain/landscape/`. For colleagues: `/visual-brain:page en` makes the English page.
- Next: choose (a direction, or a combination: the look of one, the cast of another), here or later with `/visual-brain:choose <your choice>`; then `/product-visual:new <product>` (the Product Visual plugin, from the same marketplace) builds a product's visual on it.
- **"Waiting for you:"** which direction do you choose? A combination is fine.

On the answer: do what `/visual-brain:choose` does (its command file: `${CLAUDE_PLUGIN_ROOT}/commands/choose.md`) and say so in one line.

## 11. Hand off to Portfolio and update the state

1. Write `projects/visual-brain/outputs/portfolio-handoff.md` (framework, "Hand off to Portfolio"): the cover status, and for each visual module its source file and section or "not available", with the image provenance list. Visual Brain does not lay out the case; `/portfolio:case` reads this file.
2. Update `state.md`: the inputs used, the candidates and the recommendation (never as chosen), what was rejected, the next task.

## Connect it to the repo

Only if missing, never overwriting the owner's text:
1. `CLAUDE.md`'s Visual Brain section holds the line: **`wiki/brand/visual-guide.md` is this repo's visual direction.** Read it before briefing, generating, choosing or judging any image.
2. `AGENTS.md`, if the repo has one, gets the same line.
