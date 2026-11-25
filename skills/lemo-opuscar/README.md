# 🎥 Lemo-Opuscar — 99 film styles, sab code se

**Credit:** [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) — Lemomo (LemoLab / SecondFirst Pty Ltd).
License: code MIT · Markdown/docs **CC BY-NC 4.0 (non-commercial)** · demo films CC BY 4.0. Details: `lemo-opuscar/LICENSE`.

## Kya hai

Ek skill jo **99 alag film styles** ki library ko chalati hai: oil painting, watercolor, ukiyo-e, newsreel,
satellite briefing, product teardown, pixel RPG, blueprint, LiDAR survey, aur bhi bahut. Har style ka apna
`STYLE.md` (look ke rules) aur ek demo film hai. Claude aapke topic par usi style me poori short film code se banata hai.

👉 **Saari 99 styles ki list aur unka look: [`STYLES.md`](STYLES.md)**

## Install

Skill pehli baar chalne par library khud clone karti hai (`~/lemo-opuscar`):

```bash
sh skills/lemo-opuscar/lemo-opuscar/scripts/setup.sh        # library + missing tools check
sh skills/lemo-opuscar/lemo-opuscar/scripts/setup.sh deps   # core tools (kuch minute)
```

Zaroori: Node, FFmpeg, Python. ✦ wali styles ke liye aapka apna image generator chahiye.
Voice/music optional: `setup.sh deps voice`, `setup.sh deps music`.

## Kaise use karein

| Prompt | Output |
|---|---|
| "lemo-opuscar — kaun kaun se styles hain?" | categories ke saath style list |
| "**Watercolor** style me barish par 30 sec ki film" | `<project>/` me final film (MP4), poster, subtitles |
| "**Satellite Briefing** style me Mumbai ke floods ka explainer" | real satellite data wala explainer film |
| "**Exploded Teardown** me mere product ka breakdown" | product parts alag hote hue film |
| "Mere topic ke liye style tum chuno" | 2–3 styles suggest karke, ek round sawal, phir film |
| "Ukiyo-e ko apne colours ke saath **apni style** bana do" | `~/lemo-my-styles/` me aapki saved style |

Flow: **style chuno → ek round sawal → TREATMENT.md (plan) → production → delivery** (`DIRECTOR.md` §11 wali files).

## Aur kis kaam aa sakti hai

- `teardown`, `glass-product`, `white-model`, `lidar-survey`, `blueprint` styles → **3D product / architecture** videos (`3d-video-studio` ke saath).
- `map-explainer`, `satellite-briefing`, `dataviz` → news/data explainers (`anything2explainer` jaisa kaam).
- Final cut ke baad `ffmpeg-video` se 9:16 / music / GIF.

Non-commercial docs license ki wajah se commercial use se pehle LICENSE padhein.
