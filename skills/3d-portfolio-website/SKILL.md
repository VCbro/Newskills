---
name: 3d-portfolio-website
description: Build a personal 3D portfolio / landing website with React, Vite, Three.js (React Three Fiber + drei), Framer Motion and Tailwind — 3D hero model, animated sections, project cards, experience timeline, contact form — starting from Adrian Hajdin's open-source 3D developer portfolio. Use when the user asks for a 3D website, portfolio, personal site, or landing page with 3D models/animations.
---

# 3D Portfolio Website

Base project: https://github.com/adrianhajdin/project_3D_developer_portfolio (credit: Adrian Hajdin /
JavaScript Mastery). It has no license file, so its code is not copied into this skills repo:
clone it into the user's project, use it for learning/personal sites, and credit it in the footer/README.
For a commercial client site, rebuild the sections in your own code using it only as a reference.

## Start

```bash
bash "<skill dir>/scripts/new-portfolio.sh" my-portfolio   # clone, install, done
cd my-portfolio && npm run dev                             # http://localhost:5173
```

## What to change (in this order)

1. **Content — `src/constants/index.js`:** name, services, technologies (icons in `src/assets/tech`),
   experiences, testimonials, projects (image, tags, GitHub/live link). Ask the user for these once.
2. **Hero text — `src/components/Hero.jsx`.**
3. **3D models — `src/components/canvas/`** (`Computers.jsx`, `Earth.jsx`, `Ball.jsx`, `Stars.jsx`):
   GLTF files live in `public/`. To swap a model: put a `.glb` in `public/`, `useGLTF('/model.glb')`,
   adjust `scale`/`position`/`rotation`. Compress first: `npx gltf-transform optimize in.glb public/model.glb --texture-compress webp`.
4. **Contact form — `src/components/Contact.jsx`** uses EmailJS and already reads
   `VITE_APP_EMAILJS_SERVICE_ID`, `VITE_APP_EMAILJS_TEMPLATE_ID`, `VITE_APP_EMAILJS_PUBLIC_KEY` from `.env`
   (copy `.env.example` → `.env`, fill from emailjs.com). Never hard-code keys or commit `.env`.
5. **Colours/fonts — `tailwind.config.cjs`, `src/index.css`.**

## Make it better (upgrades this skill adds)

- **Performance:** wrap each `<Canvas>` in `<Suspense>`, `dpr={[1, 2]}`, `frameloop="demand"` for static scenes,
  render a poster image instead of the canvas on mobile (`window.matchMedia('(max-width: 640px)')`).
- **Realism:** `<Environment preset="city" />` from drei, `<ContactShadows />` under the model,
  ACES tone mapping (default in R3F). See `../3d-video-studio/threejs-3d/SKILL.md` §Realism.
- **Upgrade deps** when the user wants the latest: `npm i three@latest @react-three/fiber@latest @react-three/drei@latest`
  (R3F v9 needs React 19 — upgrade `react`/`react-dom` together, then fix breaking imports).
- **SEO:** title, meta description, Open Graph image in `index.html`.
- **Intro video:** a 3D teaser for the site can be made with `3d-video-studio` and placed as a `<video autoplay muted loop playsinline>`.

## Ship

`npm run build` → `dist/`. Deploy on Vercel/Netlify (`npx vercel --prod` or drag `dist/` into Netlify),
or GitHub Pages (set `base` in `vite.config.js` to `/<repo>/`).
