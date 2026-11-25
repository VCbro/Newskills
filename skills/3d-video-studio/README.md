# 🎬 3D Video Studio — code se realistic 3D video → MP4

Ek hi skill-bundle jisme **5 open-source projects** jode gaye hain taaki aap sirf likh kar
realistic 3D video bana sako aur use MP4 me render kar sako.

| Folder | Kya hai | Original (credit) | License |
|---|---|---|---|
| `SKILL.md` | **Orchestrator** — engine chunta hai, shot list, render, finish | is repo ka | MIT |
| `threejs-3d/` | 3D scene: PBR materials, HDRI light, GLTF models, camera path + frame renderer | [mrdoob/three.js](https://github.com/mrdoob/three.js) — mrdoob & three.js authors | MIT |
| `pascal-3d/` | 3 skills: `pascal-3d`, `architect`, `furniture-fit` — 3D ghar/room/building banana | [pascalorg/editor](https://github.com/pascalorg/editor) — Pascal | MIT |
| `remotion/` | 14 skills — React se video (timeline, captions, render, studio, maps, 3D) | [remotion-dev/skills](https://github.com/remotion-dev/skills) · [remotion-dev/remotion](https://github.com/remotion-dev/remotion) — Remotion | Remotion License |
| `hyperframes/` | 9 skills — HTML se video, 456 ready blocks, reverse-any-video, figma, media | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — HeyGen | Apache-2.0 |
| `hyperframes-craft/` | 6 craft skills — motion-doctrine, seam-craft, cut-the-curve, captions-overlay… | heygen-com/hyperframes | Apache-2.0 |
| `HYPERFRAMES_REGISTRY.md` | 456 ready-made blocks/components ki list | auto-generated | — |
| ↳ finishing | `../ffmpeg-video` — audio, 9:16, GIF, compress | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | LGPL/GPL |

## Kaise kaam karta hai

```
Aapka prompt ──► 3d-video-studio (plan + shot list)
                    │
                    ├─► threejs-3d   (3D object, light, camera)       ┐
                    ├─► pascal-3d    (agar ghar / room / building ho)  ├─► Remotion YA HyperFrames ──► MP4
                    └─► prompt-library (idea / reference prompt)       ┘          │
                                                                                  ▼
                                                               ffmpeg-video (music, voice, 9:16, GIF)
```

## Install

```bash
git clone https://github.com/VCbro/Newskills && cd Newskills
bash install.sh            # saari skills ~/.claude/skills me link ho jaati hain
```

Zaroori: **Node 18+**, **FFmpeg**, Chromium (Remotion/HyperFrames khud download kar lete hain).

## Use kaise karein — example prompts (Claude Code me likho)

| Prompt | Kya milega (output) |
|---|---|
| "3d-video-studio se ek **red sports car ka 15 sec product reveal** banao, studio light, 16:9" | `out/final.mp4` 1920×1080 30fps + `poster.jpg` |
| "Mere **2BHK flat ka 3D walkthrough** video banao — 2 bedroom, hall, kitchen" | Pascal me editable 3D ghar + flythrough `final.mp4` |
| "**Solar system** ka 20 sec realistic 3D explainer, Hindi captions ke saath" | `final.mp4` + `.srt` captions |
| "Mera **logo 3D me extrude** karke 5 sec ka intro sting, 9:16 bhi do" | `final.mp4` + `final_9x16.mp4` |
| "Ye Remotion project **HyperFrames me convert** karo" | naya HyperFrames project, frame-by-frame verified |
| "Is reference video ko **reverse karke editable** project banao" | HyperFrames project + render |

Seedhe test karna ho to (koi framework nahi chahiye):

```bash
cd skills/3d-video-studio/threejs-3d/examples
node ../scripts/render-frames.mjs product-turntable.html out 1920 1080 30 180
ffmpeg -framerate 30 -i out/%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 product.mp4
```

Output: 6 second ka glossy 3D object, soft shadow, camera push-in. Yeh pipeline is repo me test ki gayi hai.

## Kaun sa engine kab?

- **Remotion** — React aata ho, data se bahut saare videos (`--props`), captions, SaaS app. Free: individuals + 3 logon tak ki company.
- **HyperFrames** — plain HTML, sabse fast, 456 ready blocks (`npx hyperframes add <name>`), path-traced realistic light.
- **Sirf Three.js** — ek continuous shot (turntable, flythrough).

## Aur kis kaam aa sakti hai

- `threejs-3d` → **3D website** (`../3d-portfolio-website`) ke hero section me bhi.
- `remotion` / `hyperframes` → `anything2explainer` (Remotion use karta hai), `onetake`, `anidoodle`, `lemo-opuscar` ke outputs ke upar captions/titles.
- `hyperframes/slideshow` → video ki jagah live presentation.
- `pascal-3d/furniture-fit` → interior design: "kya ye sofa mere room me fit hoga?"

## Update

```bash
python3 scripts/sync.py remotion-skills hyperframes pascal-editor threejs
python3 scripts/build_catalogs.py
```
