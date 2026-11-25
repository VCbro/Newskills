---
name: ffmpeg-video
description: Finish, convert and fix any video with FFmpeg — join rendered frames into MP4, add music/voice-over/subtitles, loudness-normalize, make 9:16/1:1/16:9 versions, trim, concat, speed ramps, GIF/WebM previews, poster frames, compress for WhatsApp/Instagram/YouTube, and inspect files with ffprobe. Use as the last step of every code-made video (Remotion, HyperFrames, Three.js, anidoodle, lemo-opuscar, onetake, vox-director, explainers) or whenever the user asks to convert, compress, cut, merge or add audio to a video.
---

# FFmpeg video finishing

Install: Ubuntu `sudo apt install ffmpeg` · macOS `brew install ffmpeg` · Windows `winget install Gyan.FFmpeg`.
Check: `ffmpeg -version`. Always inspect inputs first and outputs last:

```bash
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate,sample_rate -of compact in.mp4
```

Rules: never overwrite the source (write to `out/`), keep `-pix_fmt yuv420p` + `-movflags +faststart`
for anything that will be played on phones/web, and use `-crf` (quality) not `-b:v` unless a size limit is given.

## Frames → video

```bash
ffmpeg -framerate 30 -i frames/%05d.png -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -movflags +faststart out/video.mp4
# transparent (for overlays): ProRes 4444 or VP9 with alpha
ffmpeg -framerate 30 -i frames/%05d.png -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le out/alpha.mov
```

## Audio

```bash
# add music, fade in/out, cut to video length, broadcast loudness (-14 LUFS for social)
ffmpeg -i video.mp4 -i music.mp3 -filter_complex "[1:a]afade=t=in:d=1,afade=t=out:st=13:d=2,loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest out/with-music.mp4
# voice-over over music with ducking (music dips under the voice)
ffmpeg -i video.mp4 -i voice.wav -i music.mp3 -filter_complex "[2:a]volume=0.5[m];[m][1:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[duck];[duck][1:a]amix=inputs=2:duration=first,loudnorm=I=-14[a]" -map 0:v -map "[a]" -c:v copy -c:a aac out/vo.mp4
```

## Shapes for every platform

```bash
# 16:9 → 9:16 (blurred background fill, sharp video centered) — Reels/Shorts/TikTok
ffmpeg -i in.mp4 -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:a copy out/vertical.mp4
# center crop to 1:1
ffmpeg -i in.mp4 -vf "crop='min(iw,ih)':'min(iw,ih)',scale=1080:1080" -c:a copy out/square.mp4
```

## Cut, join, speed

```bash
ffmpeg -ss 00:00:05 -to 00:00:12 -i in.mp4 -c:v libx264 -crf 18 -c:a aac out/clip.mp4      # exact trim
printf "file '%s'\n" a.mp4 b.mp4 c.mp4 > list.txt && ffmpeg -f concat -safe 0 -i list.txt -c copy out/joined.mp4   # same codec/size
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" out/2x.mp4
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "xfade=transition=fade:duration=0.6:offset=4.4" -an out/xfade.mp4    # crossfade
```

## Subtitles & text

```bash
ffmpeg -i in.mp4 -vf "subtitles=subs.srt:force_style='FontName=Inter,FontSize=22,Outline=2,MarginV=60'" -c:a copy out/subbed.mp4   # burn in
ffmpeg -i in.mp4 -i subs.srt -c copy -c:s mov_text out/soft-subs.mp4                                                              # soft subs
```

## Previews & sharing

```bash
ffmpeg -ss 3 -i in.mp4 -frames:v 1 -q:v 2 out/poster.jpg                                                     # poster
ffmpeg -i in.mp4 -vf "fps=15,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" out/preview.gif   # good GIF
ffmpeg -i in.mp4 -c:v libvpx-vp9 -crf 32 -b:v 0 -c:a libopus out/web.webm                                    # web
ffmpeg -i in.mp4 -vf "scale=-2:720" -c:v libx264 -crf 26 -preset slow -c:a aac -b:a 96k out/whatsapp.mp4      # small
# exact size target (e.g. 8 MB for 30 s): bitrate_kbps = 8*8192/30 - 128
ffmpeg -y -i in.mp4 -c:v libx264 -b:v 2050k -pass 1 -an -f null /dev/null && ffmpeg -i in.mp4 -c:v libx264 -b:v 2050k -pass 2 -c:a aac -b:a 128k out/8mb.mp4
ffmpeg -i in.mp4 -vf "select='not(mod(n\,30))',scale=320:-1,tile=6x3" -frames:v 1 out/contact-sheet.png       # review sheet
```

## Fix common problems

| Problem | Fix |
|---|---|
| Plays on PC but not on iPhone/WhatsApp | re-encode `-c:v libx264 -pix_fmt yuv420p -profile:v high -movflags +faststart` |
| Audio out of sync after concat | re-encode instead of `-c copy`, or `-af aresample=async=1` |
| Banding in dark gradients | `-crf 14`, or add `-vf noise=alls=2:allf=t` before encode |
| Variable frame rate screen recording | `-vf fps=30` |
| Too loud / too quiet | `-af loudnorm=I=-14:TP=-1.5:LRA=11` |

Credit: FFmpeg (https://github.com/FFmpeg/FFmpeg), LGPL/GPL. This skill only calls the installed binary.
