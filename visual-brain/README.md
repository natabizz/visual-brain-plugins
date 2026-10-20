# Visual Brain

The brand's visual direction, built from its audience. An add-on to the Marketing Brain (CXL AI Native Marketer).

Visual Brain takes who your buyer is and where your brand stands (the Marketing Brain's ICP and positioning hub), studies what this audience responds to and what the market already looks like, and proposes two or three visual directions that would attract this audience and that competitors can't wear. Each direction is shown in pictures and on the carriers you use, next to how everyone else looks. You choose one; it writes the visual language for it.

It does not design a logo, a typeface or a palette. Your logo, colors and fonts are taken as they are, and the directions show how to use them differently. For a brand without an identity yet, the chosen direction is the brief a designer starts from.

It works at brand level only, so a brand without a single product photo can use it. Product images (a product's positioning, its gallery, briefs, image checks) live in the companion plugin, **Product Visual**, which reads Visual Brain's output.

## What you get

One page that reads like a brand presentation, in the language you write in:
1. **Cover:** the thesis and a three-line summary: the market, the empty space, the recommended direction.
2. **The market:** a wall of what everyone looks like, three patterns, the brands you look up to, and three things none of the brands looked at does.
3. **Who it is for:** five vibe words, each with a buyer's own quote, and three pains the picture must answer.
4. **Where you are now:** your current images and site, what is strong and what is worth a look (left out if you have no images yet).
5. **Directions:** two or three, each with a collage, a palette sampled from real images, three shooting rules, the signature, why it fits and the risk.
   **Every color:** when you sell a range (colorways, lines), one row per variant for the recommended and the chosen direction: the piece's color and the backdrop the direction gives it, checked at the size of a marketplace tile, with your own photo of that variant, or your photo with only the background replaced (a preview), or a reference, or exactly what to shoot. Even with photos of one color only, you see the system for all of them.
6. **How it looks:** the carriers where your audience actually looks (a social media grid and the site first screen by default), as everyone, as you are now, and in each direction.
7. **Tests and choice:** how an audience panel and a rival reacted, the recommendation by five questions (clear at a glance, advantage visible, believable, recognizable on a second meeting, producible again and again), and what to check before choosing.
8. **What to do next:** actions by priority, each with its reason, and the first shoot list: the first set on your main carrier (nine grid frames by default) and the site hero, built from the photos you already have first.

Behind the page: `wiki/brand/visual-guide.md` (the file Claude reads before any visual work) and `projects/visual-brain/landscape/` (the audience, the market, every image looked at, the tests).

## Commands

| Command | Does |
|---|---|
| `/visual-brain:setup` | Prepares the workspace; safe to run again |
| `/visual-brain:brand [quick \| full]` | The whole run: research, directions, tests, the page. Standard by default: about 10 brands, about half an hour to forty minutes. `quick`: up to 6 brands, about twenty minutes. `full`: 15 to 20 brands, about an hour |
| `/visual-brain:choose <your choice> [photos: <folder>]` | Records your choice (one direction or a combination), reads your photo folder again, and rewrites the visual language, every color, what to do next and the page for it, without new research |
| `/visual-brain:page [language] [public]` | The same page in another language, for example `en` for colleagues, from the same files |

## How it works

- **Find first, ask last.** It reads your brand files, finds your pages, your competitors and your audience's places by itself, then asks once for what only you can add: the folder with your product photos, brands you look up to, what must not change, a link to your boards. Attach images or paste links in the chat. Nothing is required.
- **Observations, not orders.** Every judgment comes with its basis; facts that contradict each other in your own materials name both sources. Text and fonts on your reference boards are treated as references, not judged.
- **No invented copy.** Mockups use only lines your brand already uses or facts from your files, marked temporary.
- **Who AI names.** If you have a list of brands AI assistants recommend in your category (an AI visibility check), paste it in the chat: it becomes part of the market map, and the page says whether the brands you look up to show up in AI answers at all.
- **Status on everything.** Every fact, claim and test result is marked confirmed, assumption, your decision or simulation, and the page's first screen says what the recommendation stands on and what is not known yet.
- **Tested by someone who didn't write it.** An audience panel played from your ICP's own words reacts to the directions shown blind, on your own images only; the strongest competitor's creative director says what it could wear tomorrow; an independent judge checks the result. All of these are AI simulations, and the page says so.

## Photo previews (optional)

To show your own photos on each proposed backdrop, Visual Brain can install a cut-out library once (about 200 MB, Python 3.10 or newer). It asks before installing. Without it, every color still gets its pair, its check and a shape preview.

## Install

In Claude (desktop or claude.ai): **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `natabizz/visual-brain-plugins`; or **Customize → Plugins → Add → Upload plugin** with the zip from `dist/`. In a Claude Code session:
```
/plugin marketplace add natabizz/visual-brain-plugins
/plugin install visual-brain@visual-brain-plugins
```
Then, in your Marketing Brain workspace: `/visual-brain:setup`, then `/visual-brain:brand`.

Needs: the Marketing Brain's `icp.md` and `positioning-messaging.md` drafted. The setup installs the image library (Pillow) the scripts use.

## Privacy

Image files stay on your computer: `raw/visuals/` and the built pages, which carry the images inside them, are git-ignored. Images of private people found in research are described with a link, never saved or shown. Other brands' images are shown on the page for internal review only.

## Author

Natalia Bizyukova
