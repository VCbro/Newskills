# 🎞️ Documentary Studio — code se documentary, Hindi ke saath

Ek skill jo documentary banane ke liye repo ki saari kaam ki skills ko jodti hai: **evidence board (archive photos +
red string), paper-cut / collage, real-reference 3D reconstruction, newsreel, maps aur data**. Saath mein **sahi
Hindi text, Hindi captions aur Hindi voice** ka support hai.

| Folder | Kya hai | Credit | License |
|---|---|---|---|
| `SKILL.md` | **Orchestrator**: route chunna, truth rules, work loop, Hindi | is repo ka | MIT |
| `cinematic-film/` | Narrated film engine: ek camera ek "board" par chalta hai; photos, documents, maps, stamps, counters narrator ke shabd par aate hain; SFX, mix, captions | [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) — exploraX | MIT |
| `scripts/hindi_text.py` | cinematic-film board par **Hindi text sahi** (matras, sanyukt akshar) | is repo ka | MIT |
| `scripts/hindi_captions.py` | **Kisi bhi video par sahi Hindi captions** (SRT ya timing.json se) | is repo ka | MIT |
| `fonts/NotoSansDevanagari.ttf` | Hindi font | Google Noto | SIL OFL |
| ↳ `../open-3d-skills/` | real building/landmark 3D, exploded machine, 60fps recording | [Moh4696/open-3d-skills](https://github.com/Moh4696/open-3d-skills) | MIT |

## Kaunsa route kab?

| Aapki documentary | Route | Kya dikhega |
|---|---|---|
| History, biography, true crime, company story | **A. Evidence board** (`cinematic-film`) | Cork wall par asli photos, akhbar ki kataran, stamps, laal dhaaga, map par route, gin-te numbers |
| Myth, culture, bachchon ke liye, warm explainer | **B. Paper-cut / collage** | Kaagaz ki katran wali duniya (lemo `papercut-red`, `paper-popup`, `shadow-puppet`; anidoodle `fox`; vox-director) |
| Asli jagah, building, jahaz, machine | **C. Real-reference 3D** | Reference photos aur naap se bana 3D model, flythrough, exploded view, "पुनर्निर्माण" label |
| Asli footage wali ghatna | **D. Archive / newsreel** | lemo `newsreel`, `caption-news`, `visual-investigation`, `kino-montage` |
| Yuddh, migration, climate, economy | **E. Maps & data** | Asli map boundaries, satellite briefing, charts |
| 3–10 min "kaise kaam karta hai" | **F. Long explainer** | `anything2explainer` ya huashu grammars |

## Install

```bash
pip install skia-python numpy pillow scipy          # cinematic-film
sudo apt install ffmpeg espeak-ng libegl1          # Linux (macOS: brew install ffmpeg)
pip install edge-tts                               # optional: free Hindi neural voice
python3 skills/documentary-studio/cinematic-film/scripts/check_setup.py
```

Linux par `import skia` ke liye `libegl1` chahiye (`libEGL.so.1` error isi ka hai).

## Example prompts

| Prompt | Output |
|---|---|
| "documentary-studio: **Bhagat Singh** par 90 sec Hindi documentary, asli photos ke saath" | `out/final.mp4` + Hindi captions + `.srt` + `credits.md` + `facts.md` |
| "**Taj Mahal kaise bana** — 3D reconstruction ke saath 60 sec" | 3D model (reference photos se) + board film, "पुनर्निर्माण" label |
| "**Titanic** ki raat — true crime style evidence board, English" | `wall` look film, map route, timeline stamps |
| "**Ramayan ki kahani** paper-cut style mein, 9:16" | paper-cut film (lemo `shadow-puppet` / `papercut-red`) |
| "1947 **partition** ka map explainer" | migration routes on real map + data counters |
| "Is video par **Hindi captions** laga do" (`video.mp4` + `subs.srt`) | `out.mp4` sahi Hindi captions ke saath |

## Is repo mein test kiya gaya

- cinematic-film template (English): voice, render, SFX, mix. 25 sec film 1 min 8 sec mein bani (720p, 3 workers).
- **Hindi version:** Hindi script, espeak-ng Hindi voice, `hindi_text` se board par Hindi, `hindi_captions` se captions. Matras aur sanyukt akshar sahi aaye.
- Upstream bug fix: cinematic-film sirf A–Z letters ginta tha, isliye Hindi par crash hota tha. Fix `scripts/patches/cinematic-film.py` mein hai, aur har sync ke baad apne aap dobara lagta hai.
- edge-tts Hindi voice yahan network ki wajah se test **nahi** ho saki; aapke computer par chalegi.

## Aur kis kaam aa sakti hai

- `hindi_captions.py` **har skill ke output** par kaam karta hai: 3D video, anidoodle, lemo, onetake.
- `hindi_text.py` ka tareeka (Pillow raqm → image) kisi bhi Skia/Canvas engine mein Hindi ke liye use ho sakta hai.
- cinematic-film ke `studio` / `charcoal` looks se **product launch** aur **founder story** videos bhi bante hain.
