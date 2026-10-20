# Visual Brain plugins

The visual layer on top of the CXL Marketing Brain. The Marketing Brain says who the brand is for and what it says; these two plugins say how it should look, next to everyone else on the shelf.

Built for brands of physical products whose buyers choose by looking: marketplaces, the brand's own site and social media. Software and services are not covered.

**Beta.** Tested on one brand so far. Feedback and runs on other brands are welcome.

| Plugin | What it gives you |
|---|---|
| **Visual Brain** | The brand's visual direction. It studies the audience and the visual market (shelf competitors, references, and the brands AI assistants recommend if you have that list), proposes two or three directions, and shows each one on a social media grid and a site first screen next to how everyone looks. A simulated audience panel, shown the directions blind on your own images, and a simulated rival creative director test them; one direction is recommended by five questions (clear, advantage, believable, recognizable, producible), and every fact and test result carries its status. It checks one backdrop per color of your range at marketplace-tile size, and after you choose, it writes the visual language and a shoot list built from the photos you already have. |
| **Product Visual** | A product's images, planned frame by frame. Who the product is for and what they need to see, its positioning and UVP, a direction in the brand's chosen look, then a storyboard with a brief and a readiness status per frame for a marketplace, your site, search, or social. It reads your own galleries so the new one changes their formats rather than repeating them, and with two lines of the same kind it tells them apart. Also audits a live gallery and checks finished images before upload. |

The brand run, the product run and the audit and QA checks each end with one page in your language (`/visual-brain:page en` makes an English one), plus Markdown files Claude reads before any visual work.

## Before you start

- The Marketing Brain's ICP and positioning drafted (exercises 1 and 2).
- A folder with your product photos helps most. Nothing is required: missing inputs are marked, not blocking.
- Time: a standard run looks at about 10 brands, roughly half an hour to forty minutes. `/visual-brain:brand quick` is shorter, `/visual-brain:brand full` goes wider (15 to 20 brands, about an hour).
- Built and tested on macOS; Linux works without the HEIC step. The image scripts need Python 3; setup installs the image library they use. HEIC photos are converted with the macOS `sips` tool; elsewhere, export them as JPEG first. The blind-test agents use a Claude Code field that needs version 2.1.271 or later; older versions ignore it.

## Install

In Claude: **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `natabizz/visual-brain-plugins`, then install Visual Brain and Product Visual.

In Claude Code:

```
/plugin marketplace add natabizz/visual-brain-plugins
/plugin install visual-brain@visual-brain-plugins
/plugin install product-visual@visual-brain-plugins
```

Or download the zips from `dist/` and use **Customize → Plugins → Add → Upload plugin**.

Then open a new chat in your Marketing Brain folder (commands load when a chat starts):

| Command | Does |
|---|---|
| `/visual-brain:setup` | Adds Visual Brain's files to your workspace, once. Never overwrites yours |
| `/visual-brain:brand [quick \| full]` | The whole brand run: market, directions, tests, the page |
| `/visual-brain:choose <your choice>` | Records your choice and rebuilds the guide and page for it |
| `/visual-brain:page [language] [public]` | The page again, in another language; `public` leaves out other brands' images and your open issues |
| `/product-visual:setup` | Adds Product Visual's files to your workspace, once |
| `/product-visual:new <product> [channel]` | A product from scratch, up to the storyboard and briefs |
| `/product-visual:gallery <product> <channel>` | The storyboard for another channel |
| `/product-visual:page <product> [language]` | A product's page again, in another language |
| `/product-visual:audit`, `qa`, `ai-read`, `review` | A live gallery, finished images, how AI reads a listing, dated results |

## Your first run, and what to expect

1. In your Marketing Brain folder, with `wiki/brand/icp.md` and `wiki/brand/positioning-messaging.md` drafted: `/visual-brain:setup`, then `/visual-brain:brand`. It gathers what it can, asks once for what only you can give (a photo folder, brands you look up to), then runs for about half an hour. You get `wiki/brand/visual-guide.md` and one page: the market, two or three directions on your carriers, the tests, a recommendation and what to do next.
2. Choose: `/visual-brain:choose <your choice>`. The guide and the page are rewritten for it.
3. A product: `/product-visual:setup`, then `/product-visual:new <product> <channel>`. You get the product's positioning, a direction, a storyboard with a brief and a readiness status per frame, and one page.

Known limits:
- Built for physical products. A brand without product photos still gets directions, but its panel judges references, and the page says so.
- The tests (audience panel, rival, skeptical buyer, judge) are AI simulations: they show what reads clearly and what is distinct, not what sells.
- A channel's image rules behind a sign-in (a vendor portal) need your screenshot; until then the count and the first frame are marked as waiting.
- Facts come only from sources: a label, a document, a measurement. Anything unproven stays off the images and is listed as open.
- Tested end to end on one brand (physical products, marketplace and own site). Other categories and channels are untested; runs on them are welcome.

## Privacy

Your images stay on your computer: `raw/visuals/` and the built pages, which carry the images inside them, are git-ignored; the Markdown files and the pages' `.src.html` sources are tracked. Customer quotes carry no names or emails. Pages show other brands' images for internal review only. Before sharing a Visual Brain page outside your team, rebuild it with `public`; Product Visual pages show competitor cards and are for internal review.

## Author

Natalia Bizyukova. MIT License.
