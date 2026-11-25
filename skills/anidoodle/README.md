# ✏️ anidoodle — 32 hand-drawn styles, stills se films tak

**Credit:** [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) — Alex Greenshpun (10x Company). License: Apache-2.0 (`anidoodle/LICENSE`, `NOTICE`).

## Kya hai

Code se drawn pictures, loops, story films, 3D motion graphics, explainers, launch videos, website art,
aur drawing lessons — **32 styles** me (crayon, oil, sumi-e ink, ukiyo-e woodcut, pixel art, risograph,
low-poly, toy brick, embroidery, blueprint…). Saath me apna music composer, narration aur subtitles.
Har frame deterministic hai — same code se har machine par same video.

👉 **32 styles ki list:** [`anidoodle/references/styles/INDEX.md`](anidoodle/references/styles/INDEX.md)

## Install

```bash
node skills/anidoodle/anidoodle/engine/tools/scaffold.mjs ~/art --film intro --format 9x16 --duration 12
cd ~/art && npm install && npx playwright-core install chromium
node tools/still.mjs intro --frame 0 --out out/look.png --scale 2   # pehle ek still
node tools/render.mjs intro                                        # MP4 (--out x.gif bhi)
```

Zaroori: Node, Chromium. Real instrument sound pack optional hai — skill download se pehle poochti hai.

## Kaise use karein

| Prompt | Output |
|---|---|
| "anidoodle se **sumi-e ink** style me pahad par 12 sec ki 9:16 film, music ke saath" | `out/intro.mp4` + score |
| "Meri website ke hero ke liye **watercolor** illustration" | PNG still (koi bhi size) |
| "**Toy brick** style me mera logo animate karo, loop" | loop MP4 / GIF |
| "Mere app ka **launch video**, screenshots ye rahe" | launch film har shape me (16:9, 9:16, 1:1) |
| "Mujhe **cat draw karna** sikhao" | step-by-step drawing lesson film |
| "3D me extruded text wala motion graphic" | 3D motion film |

Flow: ek-ek sawal (kya, style, shape, length, sound) → **ek still se look prove** → poori film → `gate.mjs` check.

## Aur kis kaam aa sakti hai

- **3D video** (`references/workflows/three-d.md`) → `3d-video-studio` ke saath.
- **Website art** (`site-art.md`, `interactive.md`) → `3d-portfolio-website` ke liye illustrations.
- **Explainer / machines** → `anything2explainer` / `vox-director` ka alternative look.
- Music + SFX system kisi bhi video ke liye score bana sakta hai; final mix `ffmpeg-video` se.
