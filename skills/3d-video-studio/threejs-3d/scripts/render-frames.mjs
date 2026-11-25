#!/usr/bin/env node
// Render a deterministic Three.js (or any canvas) page frame by frame to PNGs.
// The page must define `window.renderFrame(frame, fps)` (sync or async) and may set
// `window.ready = Promise` for loading models/HDRIs.
//
// Usage: node render-frames.mjs <page.html|url> <outDir> <width> <height> <fps> <frames>
// Then:  ffmpeg -framerate <fps> -i <outDir>/%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 out.mp4
//
// Offline: set THREE_LOCAL=/path/to/node_modules/three to serve three.js from disk instead of the CDN.
// Needs Playwright: `npm i -D playwright && npx playwright install chromium`.
import { createRequire } from 'node:module';
import { mkdir, readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
// CommonJS require also finds a globally installed / NODE_PATH playwright.
const { chromium } = createRequire(import.meta.url)('playwright');

const [page_, outDir = 'frames', w = '1920', h = '1080', fps = '30', frames = '150'] = process.argv.slice(2);
if (!page_) {
  console.error('usage: render-frames.mjs <page.html|url> <outDir> <width> <height> <fps> <frames>');
  process.exit(1);
}
const url = /^https?:/.test(page_) ? page_ : pathToFileURL(resolve(page_)).href;
const W = +w, H = +h, FPS = +fps, N = +frames;
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
if (process.env.THREE_LOCAL) {
  await page.route(/\/three@[^/]+\/(.*)$/, async (route) => {
    const rel = route.request().url().match(/\/three@[^/]+\/(.*)$/)[1];
    try {
      const body = await readFile(resolve(process.env.THREE_LOCAL, rel));
      await route.fulfill({ body, contentType: 'text/javascript' });
    } catch { await route.abort(); }
  });
}
page.on('console', (m) => m.type() === 'error' && console.error('[page]', m.text()));
await page.goto(url, { waitUntil: 'networkidle' });
await page.evaluate(async () => { if (window.ready) await window.ready; });
if (!(await page.evaluate(() => typeof window.renderFrame === 'function'))) {
  console.error('page has no window.renderFrame(frame, fps)');
  process.exit(1);
}
const canvas = (await page.$('canvas')) ?? page;
for (let i = 0; i < N; i++) {
  await page.evaluate(([f, fps]) => window.renderFrame(f, fps), [i, FPS]);
  await canvas.screenshot({ path: `${outDir}/${String(i).padStart(5, '0')}.png` });
  if (i % FPS === 0) process.stdout.write(`\rframe ${i + 1}/${N}`);
}
console.log(`\ndone: ${N} frames in ${outDir}`);
await browser.close();
