#!/usr/bin/env python3
"""Generate catalog files from the synced upstream skills.

Run after scripts/sync.py:
    python3 scripts/build_catalogs.py [--cache DIR]

Writes:
  SKILLS_INDEX.md                         every SKILL.md in this repo: name, what it does, path
  skills/lemo-opuscar/STYLES.md           all Lemo-Opuscar film styles (~99) with one-line look
  skills/3d-video-studio/HYPERFRAMES_REGISTRY.md   ~450 HyperFrames blocks/components by type
  prompt-library/INDEX.md                 prompt counts per category (awesome-opus5-5-videos)
"""
import json, pathlib, re, sys, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
CACHE = ROOT / ".cache" / "upstream"
if "--cache" in args:
    CACHE = pathlib.Path(args[args.index("--cache") + 1]).resolve()


def frontmatter(path: pathlib.Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    meta = {}
    if not m:
        return meta
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        mm = re.match(r"^(name|description):\s*(.*)$", line)
        if mm:
            key, val = mm.groups()
            val = val.strip()
            if val in (">", "|", ">-", "|-"):
                buf = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                    buf.append(lines[i].strip()); i += 1
                val = " ".join(b for b in buf if b)
                meta[key] = val
                continue
            meta[key] = val.strip('"\'')
        i += 1
    return meta


def short(s, n=220):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def skills_index():
    rows = []
    for p in sorted(ROOT.glob("skills/**/SKILL.md")):
        rel = p.relative_to(ROOT)
        parts = rel.parts
        # skip example/fixture SKILL.md files nested deep inside an upstream skill's own folders
        if any(x in parts for x in ("examples", "fixtures", "_archive")):
            continue
        meta = frontmatter(p)
        if not meta.get("name"):
            continue
        group = parts[1]
        rows.append((group, meta["name"], short(meta.get("description", "")), rel.parent.as_posix()))
    out = ["# Skills index (auto-generated)", "",
           "`python3 scripts/build_catalogs.py` se bana hai — haath se edit mat karo.",
           f"Kul **{len(rows)} skills**. Group ka README padho kaise use karna hai.", ""]
    for group in sorted({r[0] for r in rows}):
        out += [f"## {group}  ·  [README](skills/{group}/README.md)", "", "| Skill | Kya karti hai | Path |", "|---|---|---|"]
        for g, name, desc, path in rows:
            if g == group:
                out.append(f"| `{name}` | {desc.replace('|', '/')} | [`{path}`]({path}) |")
        out.append("")
    (ROOT / "SKILLS_INDEX.md").write_text("\n".join(out))
    names = collections.Counter(r[1] for r in rows)
    dup = [n for n, c in names.items() if c > 1]
    if dup:
        print("WARNING duplicate skill names:", dup)
    print(f"SKILLS_INDEX.md: {len(rows)} skills")


def lemo_styles():
    lib = CACHE / "lemomo-ai__lemo-opuscar" / "styles"
    idx = lib / "README.md"
    if not idx.exists():
        print("lemo cache missing, skip"); return
    out = ["# Lemo-Opuscar — saare film styles (auto-generated)", "",
           "Source: [lemomo-ai/lemo-opuscar/styles](https://github.com/lemomo-ai/lemo-opuscar/tree/main/styles) · "
           "Credit: Lemomo (LemoLab) · Docs license CC BY-NC 4.0.", "",
           "**Use:** Claude ko bolo — *\"lemo-opuscar se `<Style>` style me `<topic>` par 30 second ki film banao\"*. "
           "Output: project folder me `final.mp4` (+ poster, subtitles), sab code se rendered.", ""]
    count = 0
    for line in idx.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            out += ["", line, "", "| Style | 中文 | Folder | Look (style ka saar) |", "|---|---|---|---|"]
            continue
        m = re.match(r"^\| (.+?) \| (.+?) \| \[`([^`]+)`\]", line)
        if m:
            en, zh, folder = m.groups()
            look = ""
            sm = lib / folder / "STYLE.md"
            if sm.exists():
                for l in sm.read_text(encoding="utf-8").splitlines():
                    if l.startswith("> ") and not l.startswith("> Ref"):
                        look = short(l[2:], 200); break
            out.append(f"| **{en}** | {zh} | `{folder}` | {look.replace('|', '/')} |")
            count += 1
    out.insert(2, f"Kul **{count} styles**.")
    (ROOT / "skills/lemo-opuscar/STYLES.md").write_text("\n".join(out) + "\n")
    print(f"lemo STYLES.md: {count}")


def hyperframes_registry():
    reg = CACHE / "heygen-com__hyperframes" / "registry" / "registry.json"
    if not reg.exists():
        print("hyperframes cache missing, skip"); return
    items = json.loads(reg.read_text())["items"]
    by = collections.defaultdict(list)
    for it in items:
        by[it.get("type", "?").split(":")[-1]].append(it["name"])
    out = ["# HyperFrames registry — ready-made blocks (auto-generated)", "",
           f"Kul **{len(items)} items**. Install: `npx hyperframes add <name>` (project ke andar). "
           "Skill: `hyperframes-registry`. Credit: HeyGen, Apache-2.0.", ""]
    for t in sorted(by):
        out += [f"## {t} ({len(by[t])})", "", ", ".join(f"`{n}`" for n in sorted(by[t])), ""]
    (ROOT / "skills/3d-video-studio/HYPERFRAMES_REGISTRY.md").write_text("\n".join(out))
    print(f"HYPERFRAMES_REGISTRY.md: {len(items)}")


def prompt_index():
    data = ROOT / "prompt-library/awesome-opus5-5-videos/data/videos.json"
    if not data.exists():
        return
    vids = json.loads(data.read_text())
    if isinstance(vids, dict):
        vids = next((v for v in vids.values() if isinstance(v, list)), [])
    cats, tech = collections.Counter(), collections.Counter()
    for v in vids:
        if not isinstance(v, dict):
            continue
        c = v.get("category") or v.get("section") or "other"
        cats[c if isinstance(c, str) else str(c)] += 1
        for t in v.get("tech_tags") or v.get("tags") or v.get("tech") or v.get("stack") or []:
            tech[str(t)] += 1
    out = ["# Prompt library index (auto-generated)", "",
           f"`awesome-opus5-5-videos` me **{len(vids)} entries** (`data/videos.json`) aur "
           f"**{len(list((ROOT / 'prompt-library/awesome-opus5-5-videos/prompts').glob('*.md')))} prompt files**.", "",
           "| Category | Count |", "|---|---|"]
    out += [f"| {c} | {n} |" for c, n in cats.most_common()]
    if tech:
        out += ["", "| Tech | Count |", "|---|---|"] + [f"| {t} | {n} |" for t, n in tech.most_common(20)]
    (ROOT / "prompt-library/INDEX.md").write_text("\n".join(out) + "\n")
    print(f"prompt INDEX.md: {len(vids)}")


if __name__ == "__main__":
    skills_index(); lemo_styles(); hyperframes_registry(); prompt_index()
