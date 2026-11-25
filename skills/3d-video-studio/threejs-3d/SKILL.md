---
name: threejs-3d
description: Build realistic real-time 3D scenes with Three.js (WebGL/WebGPU) — PBR materials, HDRI lighting, GLTF models, camera paths, particles, shaders — for video frames, websites or interactive pieces, and render them deterministically frame by frame to PNG/MP4. Use for any Three.js / React Three Fiber work, a 3D hero for a website, or the 3D layer of a code-made video.
---

# Three.js 3D

Docs for agents: `references/llms.txt` → https://threejs.org/docs/llms.txt and
https://threejs.org/docs/llms-full.txt (includes TSL). Fetch those for API details instead of guessing.
Install: `npm i three` (tested against r187) (React: `npm i three @react-three/fiber @react-three/drei`).
Import addons from `three/addons/...` (e.g. `three/addons/loaders/GLTFLoader.js`).

## Scene skeleton (realistic default)

```js
import * as THREE from 'three';
import { HDRLoader } from 'three/addons/loaders/HDRLoader.js';   // r180+ (RGBELoader is deprecated)
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setSize(W, H, false);
renderer.setPixelRatio(1);                         // exact output size for video
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

const scene = new THREE.Scene();
const env = await new HDRLoader().loadAsync('studio.hdr');   // Poly Haven HDRIs are CC0
env.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = env;                       // light + reflections
scene.background = new THREE.Color('#0d0f14');
const camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
```

## Realism

- **Materials:** `MeshPhysicalMaterial` / `MeshStandardMaterial`. Metal: `metalness 1, roughness 0.25–0.45`.
  Plastic: `metalness 0, roughness 0.4`. Glass: `transmission 1, thickness 0.5, ior 1.5, roughness 0.05`.
  Car paint: `clearcoat 1, clearcoatRoughness 0.05`. Use real texture maps (normal/roughness/AO) when available.
- **Light:** HDRI for ambient + reflections, one warm key `DirectionalLight` with soft shadows,
  one cool rim. Rotate the environment (`scene.environmentRotation`) so highlights sweep across the object.
- **Grounding:** contact shadow (`ContactShadows` in drei, or a shadow-catcher plane with `ShadowMaterial`).
- **Camera:** 35–50 mm feel (fov 30–40), slow eased moves (`easeInOutCubic`), slight handheld noise from a
  seeded function, depth of field only on the payoff shot.
- **Post:** `EffectComposer` + `UnrealBloomPass` on the brightest points only, `OutputPass` last. Clamp values —
  one NaN pixel blacks the frame through bloom.
- **Avoid:** pure black, pure white, default grey `MeshBasicMaterial`, spinning-forever orbits, `Math.random()`.

## Deterministic rendering for video

Every frame must be a pure function of `frame`:

```js
window.renderFrame = (frame, fps) => {
  const t = frame / fps;
  camera.position.copy(cameraPath(t));     // your keyed path
  camera.lookAt(target);
  mixer?.setTime(t);                        // GLTF animations
  renderer.render(scene, camera);
};
```

Then `node scripts/render-frames.mjs page.html out/frames 1920 1080 30 450` (Playwright opens the page,
calls `renderFrame(i)` for each frame and saves PNGs) and encode:

```bash
ffmpeg -framerate 30 -i out/frames/%05d.png -c:v libx264 -pix_fmt yuv420p -crf 16 -preset slow -movflags +faststart out/video.mp4
```

In Remotion use `@remotion/three` `<ThreeCanvas>` and `useCurrentFrame()`; in HyperFrames draw in the
`hf-seek` listener — see `../SKILL.md`.

## Models & assets (free, check each license)

- HDRIs, textures, models: Poly Haven (CC0), ambientCG (CC0), Kenney (CC0), Sketchfab (per-model license).
- Compress GLB: `npx gltf-transform optimize in.glb out.glb --texture-compress webp`.

## Websites

For a 3D portfolio / landing page use React Three Fiber + drei (see `../../3d-portfolio-website/SKILL.md`).
Lazy-load the canvas, cap `dpr` at `[1, 2]`, and show a static poster on mobile/low-power devices.
