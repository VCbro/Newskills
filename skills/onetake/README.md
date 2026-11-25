# ⚡ onetake — high-end product / launch motion videos (10–60 s)

**Credit:** [feitangyuan/onetake](https://github.com/feitangyuan/onetake) — Patrick (feitangyuan).
License: **PolyForm Noncommercial 1.0.0** — *"onetake is free for noncommercial use only."*

## Kya hai

Apple-launch jaisi short product videos: kinetic type, **real UI as material**, ek "hand/cursor" jo har
reaction cause karta hai, ek shot se doosre me flow (hard cuts sirf jahan zaroori). Ek single HTML
composition — HyperFrames/Remotion ki zaroorat nahi. Looks presets (paper, dusk, tabletop, ember…),
synthetic SFX palette, reference-video analysis, voice-over + subtitles.

Demo case sources `onetake/cases/` me hain (badi demo MP4s repo halka rakhne ke liye hataayi gayi — original repo me dekh sakte ho).

## Install

Zaroori: Python 3, FFmpeg, Node, aur:

```bash
pip install playwright numpy scipy pillow matplotlib fonttools brotli opencv-python
playwright install chromium
# narration ke liye: pip install faster-whisper (+ Kokoro TTS)
```

```bash
cd skills/onetake/onetake
python3 scripts/stills.py comp.html --times 0.7,2.4,3.8 --out stills.png    # check frames
python3 scripts/render.py comp.html --out draft.mp4 --sfx sfx.wav          # 1920×1080 draft
python3 scripts/render.py comp.html --out film.mp4 --final --sfx sfx.wav   # 4K final
```

## Kaise use karein

| Prompt | Output |
|---|---|
| "onetake se meri **app ka 20 sec launch clip**, ye screenshots hain" | `film.mp4` (4K) + draft |
| "Is reference video jaisa rhythm — `analyze_ref.py`" | energy map, cuts → same feel ka naya clip |
| "Feature demo **voice-over aur subtitles** ke saath, 45 sec" | narrated MP4 |
| "Same film **dusk look** me" | `look.py apply dusk` |

## Aur kis kaam aa sakti hai

- 3D product shot chahiye → `3d-video-studio` se clip banao, onetake comp me video ki tarah daalo.
- Vertical version / compress: `ffmpeg-video`.
- Similar launch tooling: `anidoodle` (`launch-video.md`), `hyperframes` (launch type).
