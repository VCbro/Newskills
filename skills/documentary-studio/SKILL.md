---
name: documentary-studio
description: Make a narrated documentary or factual film from code, in Hindi, English or any language — history, biography, true crime, investigation, science, place or company stories — with real references (archive photos with licences, real maps, real documents, satellite and data), paper-cut / collage looks, evidence boards, newsreel cuts, and 3D reconstructions of real buildings, places and machines. Routes the work to cinematic-film, lemo-opuscar, anidoodle, vox-director, huashu-art-motion, hyperframes, open-3d-skills, 3d-video-studio and ffmpeg-video, and adds correct Hindi text and captions. Use for "documentary banao", "make a documentary about", "history video", "true crime video", "paper cut documentary", "3D reconstruction of", "explainer with real photos".
---

# Documentary Studio

A documentary is **true story + real references + one strong look + a voice**. This skill picks the
look, keeps the facts honest, and hands the build to the right engine. Sub-skills sit next to this
file or elsewhere in this repo; read only what the chosen route needs.

## 1. Pick the route (one look per film)

| Route | Best for | Engine (read first) | Looks / styles |
|---|---|---|---|
| **A. Evidence board** (default) | history, biography, true crime, company story | `cinematic-film/SKILL.md` | `wall` (cork + red string), `slate`, `paper`, `night`, `blueprint`, `studio` |
| **B. Paper-cut / collage** | warm explainers, kids, culture, myths | lemo-opuscar / anidoodle / vox-director | lemo `papercut-red`, `paper-popup`, `paper-lantern`, `vintage-collage`, `shadow-puppet`; anidoodle `fox` (cut-paper), `paperCraft` (toy theatre), `scrapbook`; vox-director collage (paid API); hyperframes `style-sampling` "Collage Explainer" |
| **C. Real-reference 3D** | a real building, monument, place, ship, machine, crash, battle site | `../open-3d-skills/skills/threejs-scene` + `../3d-video-studio` | procedural landmark from photos + plans; `../open-3d-skills/skills/exploded-view` for machines; Pascal (`architect`) for floor plans; lemo `white-model`, `lidar-survey`, `teardown`; hyperframes "3D True Crime" |
| **D. Archive / newsreel** | events with real footage or photos | lemo-opuscar | `caption-news`, `newsreel`, `news-package`, `kino-montage`, `visual-investigation`, `archive-lighttable`, `halftone-dossier`, `dark-documentary`, `silent-film` |
| **E. Maps & data** | wars, migrations, climate, economy | cinematic-film `make_map.py` + lemo | `map-explainer`, `satellite-briefing`, `transit-map`, `dataviz`, `briefing-board`; `../3d-video-studio/remotion/remotion-maps` |
| **F. Long science explainer** | 3–10 min "how it works" | `../anything2explainer` | black MG look, chapters; or `../huashu-art-motion` grammars (Vox, Kurzgesagt-like, whiteboard) |

Routes mix by **inserting a clip**, never by mixing engines inside one scene: e.g. a 6 s 3D reconstruction
(route C) rendered to MP4 and placed on the evidence board (route A) as a "screen" item, or cut in with
`ffmpeg-video` (crossfade). Say which route you picked and why in one line.

## 2. Truth rules (non-negotiable)

1. **Research first, write `facts.md`:** every claim → source URL. Numbers and dates are checked twice.
2. **Real references stay real.** Archive photos/documents come with licence + credit
   (`cinematic-film/scripts/fetch_commons.py`, rules in `cinematic-film/references/archive.md`). Write `credits.md`.
3. **Recreations are labelled** on screen: "पुनर्निर्माण / RECREATION" for 3D or drawn documents,
   "AI चित्रण / AI ILLUSTRATION" for AI stills. Never AI images of real people or as evidence of real events.
4. **3D reconstructions follow references:** collect 3–10 reference photos, a plan/map with scale, and real
   dimensions; list them in `references.md`; match proportions before adding detail. Unknown parts are kept
   plain (white-model) rather than invented.
5. Quotes only what was really said or written. Living people: no defamation, no private details.

## 3. Work loop (gates = stop for the user's OK)

1. **Brief:** topic, language (हिंदी default if the user writes Hindi), length (60–90 s ≈ 150–230 English
   words ≈ 130–200 Hindi words), shape (16:9 / 9:16), route, voice.
2. **Research → `facts.md` → script** (`script.json` for cinematic-film: `text`, `spoken` with numbers as
   words — "उन्नीस सौ सैंतालीस" —, `hero`, `typed`). **Gate:** script + facts.
3. **References:** archive images, maps, 3D reference photos. **Gate:** asset list with licences.
4. **Scratch voice → timing** (section 4). **Gate:** look test stills of the opening.
5. **Build** in the route's engine; for Hindi on-screen text add the two lines in section 4.
6. **Draft 30 s at 720p. Gate.** Then final voice, sound (`build_sfx.py`, `mix_soundtrack.py`), full render.
7. **Captions** (section 4), 9:16 cut and poster with `../ffmpeg-video`. Deliver film + `.srt` + `credits.md` + `facts.md`.

## 4. Hindi (and other Indic languages)

- **On-screen text (cinematic-film):** its engine has no complex-script shaping, so matras break. At the top
  of the project's `scene.py`:
  ```python
  import sys; sys.path.insert(0, "<repo>/skills/documentary-studio/scripts")
  import hindi_text; hindi_text.install()
  ```
  Text is then shaped by Pillow + raqm with `fonts/NotoSansDevanagari.ttf` (set `INDIC_FONT` for another font).
  Letter tracking is ignored for Hindi (it would split conjuncts); `reveal` type-on becomes a left-to-right wipe.
- **Captions:** do NOT use FFmpeg `subtitles=` for Hindi (libass often mis-shapes ि and conjuncts). Use
  `python3 scripts/hindi_captions.py film.mp4 <project>/audio/timing.json out.mp4` (also writes `out.srt`),
  or with any `.srt`. Options: `--style box|outline`, `--highlight "शब्द,शब्द"`, `--size`, `--pos`.
- **Voice:** scratch `tts_say.py --voice hi` (espeak-ng); good free neural voice:
  `tts_say.py --cmd 'edge-tts --voice hi-IN-SwaraNeural -f {txt} --write-media {out}'` (or `hi-IN-MadhurNeural`);
  a human recording or any paid TTS saved as `audio/takes/<take>.wav` works the same.
  Hindi letters/sec is lower than English (~6 vs ~15): `split_takes.py` flags compare lines to the median, so that is fine.
- cinematic-film's timing scripts were patched for non-Latin letters (`cinematic-film/PATCHES.md`).

## 5. Finish checklist

Look at stills before claiming anything works: readable type at phone size, no dark text on dark board,
captions not covering the hero, labels on every recreation, numbers match `facts.md`, credits complete,
loudness about −14 to −16 LUFS, 9:16 version reframed (not just squeezed).
