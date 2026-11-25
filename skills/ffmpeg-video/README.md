# 🎞️ FFmpeg Video — har skill ka last step

**Credit:** [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) — FFmpeg developers (LGPL/GPL).
Skill is repo ne likhi hai (MIT). FFmpeg ka source code copy nahi kiya — skill aapke system par installed `ffmpeg` chalati hai.

## Kya karti hai

Rendered frames → MP4, music / voice-over (auto ducking), loudness, subtitles, 9:16 / 1:1 versions,
trim, join, crossfade, speed, GIF, WebM, poster, WhatsApp size, exact MB target, contact sheet, aur common fixes.

## Install

| OS | Command |
|---|---|
| Ubuntu / WSL | `sudo apt install ffmpeg` |
| macOS | `brew install ffmpeg` |
| Windows | `winget install Gyan.FFmpeg` |

## Example prompts

| Prompt | Output |
|---|---|
| "Is video me `music.mp3` lagao, fade in/out, Instagram loudness" | `out/with-music.mp4` |
| "Voice-over `vo.wav` + background music, music voice ke time dheemi ho" | `out/vo.mp4` |
| "Is 16:9 video ka Reels (9:16) version banao" | `out/vertical.mp4` 1080×1920 |
| "Isko 8 MB ke andar compress karo" | `out/8mb.mp4` |
| "Iska accha GIF preview aur poster image do" | `out/preview.gif`, `out/poster.jpg` |
| "subs.srt ko video me burn karo" | `out/subbed.mp4` |
| "Is video par **Hindi** captions" | `documentary-studio/scripts/hindi_captions.py` se (FFmpeg/libass Hindi matras tod deta hai) |

Saari commands is repo me ek test video par chala kar check ki gayi hain (music, voice ducking, 9:16, GIF).

## Kin skills ke saath use hoti hai

**Sabke saath:** `3d-video-studio`, `anidoodle`, `huashu-art-motion`, `lemo-opuscar`, `vox-director`,
`anything2explainer`, `onetake`, aur prompt-library ke code videos. Inme se kai skills khud bhi FFmpeg maangti hain.
