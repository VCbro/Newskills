# 📰 Vox Director — ek topic → poora paper-collage explainer video

**Credit:** [alisa0808/vox-director](https://github.com/alisa0808/vox-director) — alisa0808. License: MIT.

## Kya hai

Ek topic do — skill script likhti hai, collage-style keyframes banati hai, unhe animate karti hai,
narrator voice-over, background music aur captions lagati hai, aur FFmpeg se final video jodti hai.
Styles: american-retro, swiss-modern, punk-zine, atomic-age aur aur bhi (`references/prompt-guide.md`).

## Install / zaroori cheezein

| Cheez | Kyun |
|---|---|
| `ATLASCLOUD_API_KEY` (paid, [atlascloud.ai](https://www.atlascloud.ai/console/api-keys)) | images, motion, TTS (`xai/tts-v1`), music (`minimax/music-2.6`) |
| FFmpeg + ffprobe | assembly |
| Python 3 + Pillow (`pip install pillow`) | captions / watermark |

⚠️ Yeh skill **paid API** use karti hai — har video par credits lagte hain.

## Kaise use karein

| Prompt | Output |
|---|---|
| "vox-director: **Silicon Valley kaise bana** — 60 sec explainer" | `out/<project>/final.mp4` + captions |
| "**Paisa kaise kaam karta hai**, swiss-modern style, 9:16" | vertical explainer |
| "Pehle 3 styles ka **bakeoff** dikhao phir chuno" | `style_bakeoff.py` se 3 sample frames |
| "Mere brand ka 30 sec **ad**" | ad-style collage video |

Steps: script → style bakeoff → `keyframes.py` → `clips.py` → `audio.py` → assemble.

## Aur kis kaam aa sakti hai

- Free alternative chahiye to: `anything2explainer` (free TTS) ya `huashu-art-motion` ka Vox-jaisa grammar.
- 3D shots beech me chahiye to `3d-video-studio` se clip banao aur `ffmpeg-video` se jodo.
