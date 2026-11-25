# 🚀 Newskills — Claude Code ke liye best open-source video, 3D aur website skills

Ek jagah **52 skills + 99 film styles + 32 drawing styles + 52 art styles + 456 video blocks + 703 prompts**.
Kaam: code se realistic 3D video, explainers, launch videos, art films, aur 3D websites, sab MP4 tak render.
Har skill ke saath uske **original author ka credit** hai (neeche table aur [`CREDITS.md`](CREDITS.md)).

## ⚡ Install (2 minute)

```bash
git clone https://github.com/VCbro/Newskills.git
cd Newskills
bash install.sh                 # saari skills ~/.claude/skills me
```

Ek hi project ke liye: `bash install.sh --project /path/to/project`. Windows (bina symlink): `bash install.sh --copy`.
Phir Claude Code restart karo aur normal bhasha me likho, jaise *"3d-video-studio se car ka 15 sec 3D reveal banao"*.

**Common zaroorat:** Node 18+, Python 3, FFmpeg, Chromium (Playwright). Har skill ke README me uski exact list hai.

## 📦 Skills

| # | Skill folder | Kya banata hai | Output | Original repo (credit) | License |
|---|---|---|---|---|---|
| 1 | [**3d-video-studio**](skills/3d-video-studio/README.md) (34 skills: Three.js + Pascal + Remotion + HyperFrames) | Code se **realistic 3D video**: product reveal, ghar walkthrough, logo sting, 3D explainer | MP4 (16:9 / 9:16 / 1:1) | [three.js](https://github.com/mrdoob/three.js) · [pascalorg/editor](https://github.com/pascalorg/editor) · [remotion](https://github.com/remotion-dev/remotion) · [remotion skills](https://github.com/remotion-dev/skills) · [hyperframes](https://github.com/heygen-com/hyperframes) | MIT · MIT · Remotion · Remotion · Apache-2.0 |
| 2 | [**ffmpeg-video**](skills/ffmpeg-video/README.md) | Har video ka finishing: music, voice, 9:16, GIF, compress | MP4 / GIF / WebM | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | LGPL/GPL (binary) |
| 3 | [**3d-portfolio-website**](skills/3d-portfolio-website/README.md) | 3D personal **website** (React + Three.js) | Live site / `dist/` | [adrianhajdin/project_3D_developer_portfolio](https://github.com/adrianhajdin/project_3D_developer_portfolio) | no license (clone-only) |
| 4 | [**lemo-opuscar**](skills/lemo-opuscar/README.md) | **99 film styles** me short films ([list](skills/lemo-opuscar/STYLES.md)) | MP4 film + poster + subs | [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | MIT + CC BY-NC 4.0 docs |
| 5 | [**anidoodle**](skills/anidoodle/README.md) | **32 hand-drawn styles**: stills, loops, films, 3D, music | PNG / MP4 / GIF / HTML | [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) | Apache-2.0 |
| 6 | [**huashu-art-motion**](skills/huashu-art-motion/README.md) | **52 art-history styles** + 9 explainer grammars, reverse animations | MP4 | [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | MIT |
| 7 | [**vox-director**](skills/vox-director/README.md) | Topic → **Vox-style collage explainer** / ad | MP4 + captions | [alisa0808/vox-director](https://github.com/alisa0808/vox-director) | MIT (paid API needed) |
| 8 | [**anything2explainer**](skills/anything2explainer/README.md) | Topic → **3–5 min science explainer** with voice-over | MP4 + subs | [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) | PolyForm Noncommercial |
| 9 | [**onetake**](skills/onetake/README.md) | **Launch / product motion video** (10–60 s) | 4K MP4 | [feitangyuan/onetake](https://github.com/feitangyuan/onetake) | PolyForm Noncommercial |
| 10 | [**documentary-studio**](skills/documentary-studio/README.md) | **Documentary**: evidence board, paper-cut, real-reference 3D, newsreel, maps — **sahi Hindi text + captions** | MP4 + `.srt` + credits | [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) + is repo | MIT |
| 11 | [**open-3d-skills**](skills/open-3d-skills/README.md) (8 skills) | Code se real landmarks/machines 3D, exploded view, 60fps recording, scroll films, site check | HTML + MP4 | [Moh4696/open-3d-skills](https://github.com/Moh4696/open-3d-skills) | MIT |
| — | [**prompt-library**](prompt-library/README.md) (alag folder) | 703 viral code-video prompts | ideas | [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | MIT |

Har ek skill ki ek line wali list (naam, kaam, path): [`SKILLS_INDEX.md`](SKILLS_INDEX.md).

## 🧭 Kaunsi skill kab?

| Mujhe chahiye… | Use karo |
|---|---|
| Realistic **3D** product / car / logo / space video | `3d-video-studio` → `ffmpeg-video` |
| **Ghar / room / building** ka 3D model ya walkthrough | `3d-video-studio` (Pascal) |
| Kisi **art style** me story film (watercolor, ukiyo-e, newsreel…) | `lemo-opuscar` ya `anidoodle` ya `huashu-art-motion` |
| **Documentary** (history, true crime, biography) — Hindi bhi | `documentary-studio` |
| Asli building / jagah / machine ka **3D reconstruction** | `documentary-studio` route C + `open-3d-skills` |
| Kisi bhi video par **Hindi captions** | `documentary-studio/scripts/hindi_captions.py` |
| **Science / tech explainer** (lamba, voice-over) | `anything2explainer` (free TTS) · `vox-director` (collage look, paid API) |
| **App / product launch** clip | `onetake` · `anidoodle` launch · `hyperframes` |
| Koi video **dekh kar same banana** | `hyperframes/reverse-any-video` · `huashu-art-motion` |
| **3D website / portfolio** | `3d-portfolio-website` (+ `threejs-3d`) |
| Idea nahi hai | `prompt-library` |
| Music, Reels version, GIF, compress | `ffmpeg-video` |

## 🔄 Update / naya repo add karna

```bash
python3 scripts/sync.py                 # saari skills latest version par
python3 scripts/sync.py onetake         # sirf ek
python3 scripts/build_catalogs.py       # index + style lists dobara banao
bash install.sh                         # nayi skills Claude Code me
```

**Naya repo add karna:** `scripts/sources.json` me ek entry jodo (`repo`, `author`, `license`, `copy`)
→ `python3 scripts/sync.py <id>` → us folder ka `README.md` likho. Har synced folder me `UPSTREAM.md`
batata hai kaunse commit se aaya.

Repo halka rakhne ke liye upstream ki demo videos/GIFs aur 20 MB se badi files copy nahi ki jaati.

## ⚖️ Credits & license

Saari upstream skills unke authors ki hain, unke license ke saath (har folder me `LICENSE` + `UPSTREAM.md`).
**Commercial use se pehle dhyan do:** `anything2explainer` aur `onetake` sirf non-commercial use ke liye hain.
`lemo-opuscar` ke docs CC BY-NC hain. Remotion badi companies ke liye paid hai.
Is repo ka apna code (orchestrator, `threejs-3d`, `ffmpeg-video`, `3d-portfolio-website`, scripts, READMEs): MIT.
Poori list: [`CREDITS.md`](CREDITS.md).

Maintained by [VCbro](https://github.com/VCbro).
