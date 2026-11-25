# 🌐 3D Portfolio Website

**Credit:** [adrianhajdin/project_3D_developer_portfolio](https://github.com/adrianhajdin/project_3D_developer_portfolio)
— Adrian Hajdin (JavaScript Mastery). Upstream me license file nahi hai, isliye unka code is repo me **copy nahi**
kiya gaya; skill zaroorat par seedha unke repo se clone karti hai aur README me credit jod deti hai.

## Kya banta hai

React + Vite + Three.js (React Three Fiber + drei) + Framer Motion + Tailwind wali personal website:
3D computer hero, ghoomti Earth, tech balls, stars background, experience timeline, project cards, contact form (EmailJS).

## Install & run

```bash
bash skills/3d-portfolio-website/scripts/new-portfolio.sh my-portfolio
cd my-portfolio && npm run dev        # http://localhost:5173
```

## Example prompts

| Prompt | Output |
|---|---|
| "3d-portfolio-website se meri portfolio banao — naam X, skills React/Node, 3 projects" | `my-portfolio/` ready site, `npm run dev` |
| "Hero me computer ki jagah mera `car.glb` model lagao" | updated `canvas/Computers.jsx` + compressed model |
| "Site ko mobile par fast karo aur deploy karo" | poster fallback, `dist/`, Vercel/Netlify link |
| "Latest Three.js / R3F par upgrade karo" | upgraded deps + fixed imports |

## Aur kis kaam aa sakti hai

- `../3d-video-studio` se site ke liye 3D **intro/teaser video** banao aur hero me `<video>` lagao.
- `../3d-video-studio/threejs-3d` ke realism rules (HDRI, contact shadows, tone mapping) site me bhi lagte hain.
- `prompt-library` ke `category: "interactive"` / `threejs` prompts landing-page ideas ke liye.

Commercial client site ke liye unka code reference ki tarah use karo aur sections apne code me dobara likho.
