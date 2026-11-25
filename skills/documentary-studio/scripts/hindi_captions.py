#!/usr/bin/env python3
"""Burn correctly shaped Hindi / Indic captions from an SRT into any video.

FFmpeg's `subtitles` filter uses libass, and many builds shape Devanagari wrongly (the ि matra
lands after the consonant, conjuncts split). Here every caption is shaped by Pillow + libraqm
(HarfBuzz) into a transparent PNG, then FFmpeg overlays each one in its time window with a short
fade. Works for English and mixed text too.

  python3 hindi_captions.py in.mp4 captions.srt out.mp4
  python3 hindi_captions.py in.mp4 captions.srt out.mp4 --style outline --size 0.05 --pos 0.9
  python3 hindi_captions.py in.mp4 captions.srt out.mp4 --highlight "पृथ्वी,बृहस्पति"   # colour key words
  python3 hindi_captions.py film.mp4 my-film/audio/timing.json out.mp4   # cinematic-film timing; also writes out.srt

Needs Pillow with raqm (`python3 -c "from PIL import features; print(features.check('raqm'))"`)
and ffmpeg. Font: ../fonts/NotoSansDevanagari.ttf or --font / INDIC_FONT.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont, features

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_FONT = os.environ.get("INDIC_FONT") or str(HERE.parent / "fonts" / "NotoSansDevanagari.ttf")


def parse_srt(text):
    cues = []
    for block in re.split(r"\n\s*\n", text.strip().replace("\r", "")):
        lines = block.strip().split("\n")
        tl = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if tl is None:
            continue
        a, b = [s.strip() for s in lines[tl].split("-->")]
        ts = lambda s: (lambda h, m, rest: int(h) * 3600 + int(m) * 60 + float(rest.replace(",", ".")))(*s.split(":"))
        body = "\n".join(lines[tl + 1:]).strip()
        if body:
            cues.append((ts(a), ts(b.split()[0]), body))
    return cues


def wrap(text, font, max_w):
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split():
            trial = (line + " " + w).strip()
            if line and font.getlength(trial) > max_w:
                out.append(line); line = w
            else:
                line = trial
        if line:
            out.append(line)
    return out


def render_cue(text, W, H, a):
    px = int(H * a.size)
    font = ImageFont.truetype(a.font, px, layout_engine=ImageFont.Layout.RAQM)
    try:
        font.set_variation_by_name(a.weight)
    except Exception:
        pass
    lines = wrap(text, font, W * a.max_width)
    lh = int(px * 1.45)
    widths = [font.getlength(l) for l in lines]
    pad_x, pad_y = int(px * 0.6), int(px * 0.32)
    bw, bh = int(max(widths) + 2 * pad_x), lh * len(lines) + 2 * pad_y
    im = Image.new("RGBA", (bw + 40, bh + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    ox, oy = 20, 20
    if a.style == "box":
        d.rounded_rectangle([ox, oy, ox + bw, oy + bh], radius=int(px * 0.3), fill=(6, 8, 14, int(255 * a.box_alpha)))
    hl = [h for h in a.highlight.split(",") if h]
    for i, (ln, lw) in enumerate(zip(lines, widths)):
        x = ox + (bw - lw) / 2
        y = oy + pad_y + i * lh + lh * 0.78
        if a.style == "outline":
            sh = Image.new("RGBA", im.size, (0, 0, 0, 0))
            ImageDraw.Draw(sh).text((x, y), ln, font=font, fill=(0, 0, 0, 230), anchor="ls", stroke_width=max(2, px // 10), stroke_fill=(0, 0, 0, 230))
            im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(px / 18)))
        # draw word by word so key words can take the accent colour (spaces keep shaping per word intact)
        cx = x
        for j, w in enumerate(ln.split(" ")):
            col = a.accent if any(h in w for h in hl) else a.color
            d.text((cx, y), w, font=font, fill=col, anchor="ls")
            cx += font.getlength(w + " ")
    return im


def hexrgb(s):
    s = s.lstrip("#")
    return tuple(int(s[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("srt"); ap.add_argument("out")
    ap.add_argument("--font", default=DEFAULT_FONT)
    ap.add_argument("--weight", default="Bold", help="variable-font instance: Regular, Medium, SemiBold, Bold…")
    ap.add_argument("--style", choices=["box", "outline"], default="box")
    ap.add_argument("--size", type=float, default=0.044, help="text height as a share of frame height")
    ap.add_argument("--pos", type=float, default=0.93, help="bottom of the caption as a share of frame height")
    ap.add_argument("--max-width", type=float, default=0.84)
    ap.add_argument("--box-alpha", type=float, default=0.6)
    ap.add_argument("--color", default="#ffffff"); ap.add_argument("--accent", default="#ffc56b")
    ap.add_argument("--highlight", default="", help="comma-separated words drawn in the accent colour")
    ap.add_argument("--fade", type=float, default=0.18)
    ap.add_argument("--crf", type=int, default=17)
    a = ap.parse_args()
    a.color, a.accent = hexrgb(a.color), hexrgb(a.accent)
    if not features.check("raqm"):
        sys.exit("Pillow has no raqm support: pip install --upgrade pillow")
    info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", a.video], capture_output=True, text=True, check=True).stdout)
    W, H = info["streams"][0]["width"], info["streams"][0]["height"]
    dur = float(info["format"]["duration"])
    src = pathlib.Path(a.srt)
    if src.suffix == ".json":  # cinematic-film audio/timing.json: one cue per narration line
        segs = json.loads(src.read_text(encoding="utf-8"))["segments"]
        cues = [(g["start"], g["end"], g["caption"]) for g in segs]
        srt = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round(t % 1 * 1000)) % 1000:03d}"
        pathlib.Path(a.out).with_suffix(".srt").write_text(
            "\n".join(f"{i + 1}\n{srt(t0)} --> {srt(t1)}\n{tx}\n" for i, (t0, t1, tx) in enumerate(cues)), encoding="utf-8")
    else:
        cues = parse_srt(src.read_text(encoding="utf-8"))
    if not cues:
        sys.exit("no cues in " + a.srt)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="hcap_"))
    inputs, chain, last = ["-i", a.video], [], "0:v"
    for i, (t0, t1, text) in enumerate(cues):
        im = render_cue(text, W, H, a)
        png = tmp / f"c{i:03d}.png"; im.save(png)
        x = (W - im.width) // 2
        y = int(H * a.pos) - im.height
        inputs += ["-loop", "1", "-t", f"{dur:.3f}", "-i", str(png)]
        f = min(a.fade, (t1 - t0) / 3)
        chain.append(f"[{i + 1}:v]format=rgba,fade=t=in:st={t0:.3f}:d={f:.3f}:alpha=1,fade=t=out:st={t1 - f:.3f}:d={f:.3f}:alpha=1[c{i}]")
        chain.append(f"[{last}][c{i}]overlay={x}:{y}:enable='between(t,{t0:.3f},{t1:.3f})'[v{i}]")
        last = f"v{i}"
    script = tmp / "graph.txt"; script.write_text(";\n".join(chain))
    cmd = ["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex_script", str(script), "-map", f"[{last}]", "-map", "0:a?",
           "-c:v", "libx264", "-crf", str(a.crf), "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", "-t", f"{dur:.3f}", a.out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-2000:])
    print(f"{a.out}: {len(cues)} captions burned ({W}x{H})")


if __name__ == "__main__":
    main()
