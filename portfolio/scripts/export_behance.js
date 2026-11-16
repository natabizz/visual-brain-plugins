// Export a built case page as Behance modules: one JPG per <section data-module>, 2800 px wide (1400 at 2x),
// plus a 1400x1050 cover. Usage: node export-behance.js <built.html> <outdir>
// Behance specs (third-party guides, check in the upload form): module 1400 px wide, up to 2800 for retina;
// cover 1400x1050 recommended, 808x632 minimum.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1400, height: 1050 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(src));
  await p.waitForTimeout(2000);
  for (const m of await p.$$('section[data-module]')) {
    const name = await m.getAttribute('data-module');
    await m.screenshot({ path: `${out}/${name}.jpg`, type: 'jpeg', quality: 88 });
    console.log(name);
  }
  await p.addStyleTag({ content: '.cover .frame{min-height:1050px!important;height:1050px}' });
  await p.waitForTimeout(300);
  await (await p.$('section.cover')).screenshot({ path: `${out}/00-behance-cover.jpg`, type: 'jpeg', quality: 90 });
  await b.close();
})();
