# 🧠 anything2explainer — koi bhi topic → 3–5 min science explainer

**Credit:** [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) — Vincent Wei.
License: **PolyForm Noncommercial 1.0.0** — personal/non-commercial use free; commercial use ke liye author ki permission chahiye.
Banaye gaye videos aapke hain. Fonts: SIL OFL.

## Kya hai

Topic do → black background motion-graphics explainer (star-field ya dot-wave backdrop), **voice-over,
subtitles aur chapter progress bar** ke saath. Chinese ya English. Remotion par bana hai — template,
primitives library, TTS / storyboard / render tools, style rules, multi-agent workflow aur QC checks sab included.
Sample film: RAG explainer (`examples/`).

## Install

```bash
cd skills/anything2explainer/anything2explainer
bash template/scripts/new_project.sh ~/explainers rag-video     # template copy + npm install + tsc
```

Zaroori: Node, Python 3, FFmpeg, ~5 GB free disk. **Free TTS default:** Chinese `edge-tts` (Yunxi),
English `kokoro` (am_liam). Apni TTS ho to `audio.wav` khud daal sakte ho.

## Kaise use karein

| Prompt | Output |
|---|---|
| "anything2explainer: **Blockchain kya hai**, 3 min, English" | MP4 + subtitles + chapter bar |
| "**Black hole** par 5 min ka explainer, dot-wave background" | MP4 |
| "Script ye rahi, bas video banao" | storyboard → TTS → render |

Flow: script (paragraph = shot) → confirm points (script, storyboard, voice) → `tts_build.py` → render → QC.

## Aur kis kaam aa sakti hai

- Ye Remotion use karti hai → `3d-video-studio/remotion` skills (captions, render, 3D `ThreeCanvas`) yahan bhi kaam aati hain — explainer me 3D model daal sakte ho.
- Hindi voice-over: apni TTS ka `audio.wav` daal kar timeline banao.
- Final 9:16 shorts cut: `ffmpeg-video`.
