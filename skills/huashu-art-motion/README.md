# 🖼️ Huashu Art Motion (花叔) — art-history styles + explainer animation

**Credit:** [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) — alchaincyf (Huashu / 花叔). License: MIT.
Skill docs mostly Chinese me hain — Claude unhe padh kar aapse Hindi/English me baat karega.

## Kya hai

- Kisi bhi animation ko **dekh kar todna aur dobara banana** (拆解复刻).
- **36 tested art styles** (cave painting, Egypt, Greek, Gothic, Renaissance, Impressionism, Klimt, Munch,
  Dunhuang, Kusama, Ghibli-jaisa, Shinkai-jaisa, vaporwave, 8-bit, Pixar-jaisa…) + **16 research recipes**
  (Giotto, Raphael, Michelangelo, Renoir, Gauguin, Chagall, Persian miniature…).
- **9 explainer animation grammars** (3b1b-jaisa math, Kurzgesagt-jaisa, Vox-jaisa, whiteboard, kinetic type,
  finance chart, keynote UI…), jinme se 8 voice-over parameters se clip render kar sakte hain.
- Voice-over (口播) ke saath poori film, optional voice cloning.

👉 Style index: [`huashu-art-motion/references/风格配方/INDEX.md`](huashu-art-motion/references/风格配方/INDEX.md) ·
grammars: [`references/动画语法/`](huashu-art-motion/references/动画语法)

## Install

Zaroori: [uv](https://docs.astral.sh/uv/), FFmpeg, Playwright Chromium:

```bash
uv run --with playwright playwright install chromium
```

## Kaise use karein

| Prompt | Output |
|---|---|
| "huashu-art-motion se **art history speedrun** — ek hi kamra 10 styles me badalta hua" | style-by-style MP4 |
| "Is reference animation ko **tod kar same style** me naya banao" | breakdown + rebuilt clip, side-by-side `compare.py` |
| "Mere voice-over `vo.wav` par **Kurzgesagt-jaisa explainer**" | narrated explainer MP4 |
| "**Monet** style me sunrise ka 8 sec shot" | single shot MP4 |
| "**3b1b-style** math animation: Pythagoras theorem" | parametric clip |

## Aur kis kaam aa sakti hai

- Styles ko `lemo-opuscar` / `anidoodle` ke saath mila kar series bana sakte ho.
- Explainer grammars `anything2explainer` aur `vox-director` ka alternative.
- Final mix / 9:16: `ffmpeg-video`.

Note: famous artists/studios ke "style ki grammar" seekhi jaati hai — unki images, characters ya compositions copy nahi karni.
