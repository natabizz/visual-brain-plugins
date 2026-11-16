// Mechanical checks on a built case page. Usage: node qa.js <built.html>
// Prints PASS/FAIL per check; exits 1 on any FAIL. Content checks (sources, honesty) are in the command, step 6.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const file = path.resolve(process.argv[2]);
  const html = fs.readFileSync(file, 'utf8');
  const out = [];
  const check = (name, ok, detail = '') => out.push(`${ok ? 'PASS' : 'FAIL'}  ${name}${detail ? ': ' + detail : ''}`);
  check('charset declared', /^\s*<meta charset="utf-8">/i.test(html));
  check('no em dashes', !html.includes('\u2014'));
  check('no broken encoding', !/[ÃÂ]|路/.test(html.replace(/data:[^"]+/g, '')));
  check('no empty images', !/src=""/.test(html));
  const b = await chromium.launch();
  for (const w of [1400, 400]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto('file://' + file); await p.waitForTimeout(1200);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    check(`no sideways scroll at ${w}px`, sw <= w, `scrollWidth ${sw}`);
    if (w === 1400) {
      const mods = await p.$$eval('section[data-module]', s => s.map(e => e.getAttribute('data-module')));
      check('modules found', mods.length >= 8, mods.join(', '));
      const need = ['social', 'site', 'ads'];
      for (const n of need) check(`applications module: ${n}`, mods.some(m => m.includes(n)));
      const broken = await p.$$eval('img', i => i.filter(x => !x.complete || x.naturalWidth === 0).length);
      check('all images load', broken === 0, `${broken} broken`);
    }
    await p.close();
  }
  await b.close();
  console.log(out.join('\n'));
  process.exit(out.some(l => l.startsWith('FAIL')) ? 1 : 0);
})();
