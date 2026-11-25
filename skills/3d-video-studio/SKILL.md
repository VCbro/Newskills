---
name: 3d-video-studio
description: Make a realistic 3D video entirely from code and render it to MP4 — product reveals, architecture walkthroughs, space/science scenes, 3D logo stings, explainers with 3D objects. Combines Three.js (3D scene), Pascal (3D buildings and rooms), Remotion (React video timeline) or HyperFrames (HTML video timeline), and FFmpeg (encode, audio, formats). Use when the user asks for a 3D video, 3D animation, realistic render, product turntable, room/building flythrough, or "code se 3D video banao".
---

# 3D Video Studio

One brief → one 3D scene in code → one rendered `.mp4`. This skill routes the work across the
sub-skills that sit next to it. Read only the parts the task needs.

| Need | Use | Read |
|---|---|---|
| The 3D scene itself (meshes, PBR materials, lights, camera path, GLTF models) | Three.js | `threejs-3d/SKILL.md` |
| A building, house, room, floor plan, furniture layout as 3D | Pascal | `pascal-3d/pascal-3d/SKILL.md` (+ `architect`, `furniture-fit`) |
| Timeline in **React** (props, data-driven, captions, Studio preview) | Remotion | `remotion/remotion-best-practices/SKILL.md`, 3D: `remotion/remotion-markup/3d.md` |
| Timeline in **plain HTML** (fast, 450 ready blocks, path-traced light) | HyperFrames | `hyperframes/hyperframes/SKILL.md`, 3D: `hyperframes/hyperframes/references/types/3d.md`, `references/path-tracing.md` |
| Motion law, transitions, captions in HyperFrames | HyperFrames craft | `hyperframes-craft/motion-doctrine/SKILL.md` first |
| Converting Remotion ↔ HyperFrames, or Three.js / p5 code into a video | | `hyperframes/remotion-to-hyperframes/SKILL.md` |
| Music, voice, SFX, final encode, vertical/square versions, GIF, compress | FFmpeg | `../ffmpeg-video/SKILL.md` |
| Ideas / proven prompts for 3D scenes | Prompt library | `../../prompt-library/awesome-opus5-5-videos` (filter `category: "3d"`) |

## Pick the engine (one per film)

- **Remotion** when the user knows React, wants props/data (`--props`), captions from a transcript,
  or a SaaS that renders many videos. 3D goes in `<ThreeCanvas>` from `@remotion/three` (React Three Fiber).
- **HyperFrames** when you want plain HTML/JS, the fastest path, ready-made 3D blocks
  (`npx hyperframes add <block>`, list in `HYPERFRAMES_REGISTRY.md`), or path-traced realism.
- Neither framework is needed for a single continuous shot: a Three.js page rendered frame by frame
  (`threejs-3d/scripts/render-frames.mjs`) and joined with FFmpeg is enough.

Don't mix engines inside one film. Say which one you picked and why in one line.

## Work loop

1. **Brief (one round of questions max):** subject, length (default 15 s), shape (16:9 1920×1080,
   9:16 1080×1920, 1:1 1080×1080), fps (30 default, 60 for fast motion), look (realistic studio /
   cinematic night / clay / low-poly), sound (silent / music / voice-over). "You pick" → pick and say why.
2. **Shot list:** 3–6 shots, each with camera move, what changes, and duration in frames.
   One hero object; fly *into* it rather than orbiting forever.
3. **Prove the look on ONE still** (render frame at the payoff moment), show it, then build end to end.
4. **Build deterministically:** every frame is a pure function of the frame number. No `Math.random()`
   (use a seeded hash), no `Date.now()`, no `requestAnimationFrame` timing, simulations precomputed.
5. **Realism checklist** (see `threejs-3d/SKILL.md` §Realism): physically based materials, HDRI
   environment light, ACES tone mapping, soft contact shadow, depth of field only on the payoff,
   motion blur via sub-frame accumulation for fast moves, no pure black / pure white.
6. **Render:** Remotion `npx remotion render <id> out/video.mp4`; HyperFrames
   `npx hyperframes render --quality looks -o out.mp4`; plain Three.js → PNG frames → FFmpeg.
7. **Finish with FFmpeg:** add music/voice (`-af loudnorm`), make 9:16 and 1:1 cuts, a poster
   frame, a small preview GIF. Check the output with `ffprobe` (duration, fps, resolution, audio).
8. **Deliver:** `out/final.mp4` (+ `final_9x16.mp4`, `poster.jpg`) and say where they are.

## Prerequisites

Node 18+, FFmpeg on PATH, a Chromium (Remotion/HyperFrames download their own if missing).
Remotion is free for individuals and companies up to 3 people; bigger companies need a license
(`remotion/remotion-license`). Never claim otherwise.
