# 🧊 Open 3D Skills — 8 skills: 3D websites, reconstructions, recording

**Credit:** [Moh4696/open-3d-skills](https://github.com/Moh4696/open-3d-skills) — exploraX. License: MIT.

| Skill | Kya karti hai | Kahan kaam aati hai |
|---|---|---|
| [`threejs-scene`](skills/threejs-scene/SKILL.md) | Sirf code se real-time 3D: buildings, landmarks, vehicles, machines, landscapes; physically based sky/sun, soft shadows | **Documentary 3D reconstruction**, 3D website, video ka 3D layer |
| [`exploded-view`](skills/exploded-view/SKILL.md) | Machine/product ka interactive exploded view: x-ray, section cut, leader-line labels | "Kaise kaam karta hai" explainers, product pages |
| [`frame-capture`](skills/frame-capture/SKILL.md) | Kisi bhi web page (three.js, canvas, GSAP) ko virtual clock par **smooth 60fps MP4** mein record karna; side-by-side comparison | Har HTML/3D scene ko video banana (`3d-video-studio` ke `render-frames.mjs` ka bada bhai) |
| [`motion-assets`](skills/motion-assets/SKILL.md) | AI images/clips ka plan + cost **kharch se pehle**, ek style mein | Documentary illustration, website assets |
| [`alpha-cutout`](skills/alpha-cutout/SKILL.md) | Character/product clip ko transparent video banana (Safari mein bhi) | Website overlays, video compositing |
| [`scroll-film`](skills/scroll-film/SKILL.md) | Scroll karne par chalne wali film (camera move, product turn) | 3D landing pages |
| [`cursor-rig`](skills/cursor-rig/SKILL.md) | Painted character jo cursor ki taraf sir ghumata hai | Portfolio / brand sites |
| [`site-check`](skills/site-check/SKILL.md) | 3D page ko Chromium + Safari engines mein desktop/tablet/phone par check karna, frame time, errors | Har 3D website deploy se pehle |

## Example prompts

| Prompt | Output |
|---|---|
| "threejs-scene se **India Gate** ka 3D model, golden hour, phir 10 sec flythrough video (frame-capture)" | HTML scene + `india-gate.mp4` |
| "Car engine ka **exploded view** explainer" | interactive page + recorded MP4 |
| "Meri 3D portfolio site ko **site-check** karo" | screenshots + performance report |
| "Product ka **scroll-film** landing section" | scroll-scrubbed section |

## Aur kis kaam aa sakti hai

- `../documentary-studio` route C (real-reference 3D) inhi par chalta hai.
- `../3d-portfolio-website`: `scroll-film`, `cursor-rig`, `site-check`, `threejs-scene` site ko premium banate hain.
- `../3d-video-studio`: `frame-capture` se kisi bhi Three.js page ka 60fps video.
