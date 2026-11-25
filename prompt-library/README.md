# 💡 Prompt Library — Awesome Opus 5.5 Videos (alag folder)

**Credit:** [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) — yihui-dev; har prompt
uske original creator ka hai (har entry me `author` aur `post_url`). License: MIT.

Yeh skill nahi, **703 real prompts ki library** hai — log Claude se code (HTML, Canvas, SVG, Three.js, GLSL, GSAP)
me jo viral videos banwa rahe hain, unke prompts. Category-wise counts: [`INDEX.md`](INDEX.md).

| Category | Count |
|---|---|
| motion graphics | 369 |
| 3d | 117 |
| explainer | 116 |
| interactive / games | 101 |

## Kaise use karein

- Folder: `awesome-opus5-5-videos/prompts/*.md` (ek file = ek prompt), data: `awesome-opus5-5-videos/data/videos.json`.
- Claude ko bolo: *"prompt-library se 5 best **3d** prompts dikhao jo Three.js use karte hain"* → phir *"iska apne topic par version banao aur `3d-video-studio` se MP4 render karo"*.
- Ya khud dhundho:

```bash
python3 -c "import json;[print(v['slug'],'|',v['prompt'][:90]) for v in json.load(open('prompt-library/awesome-opus5-5-videos/data/videos.json')) if v['category']=='3d']"
```

## Kin skills ke saath

`3d-video-studio` (3d prompts) · `onetake` / `anidoodle` (motion) · `anything2explainer` / `vox-director` (explainer) ·
`3d-portfolio-website` (interactive). Inspiration ke liye use karo, creator ko credit do.
