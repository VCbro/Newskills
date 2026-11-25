"""Hindi (and other Indic) text for cinematic-film boards.

cinematic-film's engine draws text one character at a time with Skia, which has no complex-script
shaping here, so Hindi matras and conjuncts (क्ष, ज्ञ, त्र, श्र, ि) come out broken. This module
replaces `engine.draw_text` / `engine.text_width` for any string that contains Indic script: the
string is shaped by Pillow + libraqm (HarfBuzz), rasterised at the on-screen resolution of the
current camera zoom, and drawn by Skia as an image. Latin text still goes through the original code.

Use it in a project's scene.py (first lines, before build_film):

    import sys; sys.path.insert(0, "<path to>/skills/documentary-studio/scripts")
    import hindi_text; hindi_text.install()

Font: skills/documentary-studio/fonts/NotoSansDevanagari.ttf (SIL OFL), or set INDIC_FONT to any
.ttf. Needs Pillow built with raqm (the PyPI wheels are): `python3 -c "from PIL import features;
print(features.check('raqm'))"` must print True.
"""
from __future__ import annotations

import functools
import math
import os
import pathlib
import re
import sys

import numpy as np
import skia
from PIL import Image, ImageDraw, ImageFont, features

INDIC = re.compile(r"[ऀ-෿꣠-ꣿ᳐-᳿]")  # Devanagari … Sinhala, Vedic marks
HERE = pathlib.Path(__file__).resolve().parent
FONT = os.environ.get("INDIC_FONT") or str(HERE.parent / "fonts" / "NotoSansDevanagari.ttf")
# engine font role -> weight of the variable font
WEIGHT = {"cond": "Bold", "label": "Bold", "mono": "SemiBold", "serif": "Medium", "labelm": "Medium", "hand": "Regular"}
PAD = 4
SAMPLING = skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)

_orig = {}


def has_indic(text: str) -> bool:
    return bool(text) and bool(INDIC.search(text))


@functools.lru_cache(maxsize=128)
def pil_font(px: int, weight: str):
    f = ImageFont.truetype(FONT, px, layout_engine=ImageFont.Layout.RAQM)
    try:
        f.set_variation_by_name(weight)
    except Exception:  # static font file: weight is whatever the file is
        pass
    return f


def _weight(role):
    return WEIGHT.get(role, "Medium")


@functools.lru_cache(maxsize=1024)
def _raster(text: str, px: int, weight: str, rgb: tuple):
    """Shaped text as a Skia image; returns (image, left, top) in raster px relative to the baseline origin."""
    f = pil_font(px, weight)
    l, t, r, b = f.getbbox(text, anchor="ls")
    w, h = max(1, r - l + 2 * PAD), max(1, b - t + 2 * PAD)
    im = Image.new("RGBA", (w, h), rgb + (0,))
    ImageDraw.Draw(im).text((PAD - l, PAD - t), text, font=f, fill=rgb + (255,), anchor="ls")
    arr = np.ascontiguousarray(np.asarray(im))
    img = skia.Image.fromarray(arr, colorType=skia.ColorType.kRGBA_8888_ColorType, alphaType=skia.AlphaType.kUnpremul_AlphaType)
    return img, l - PAD, t - PAD


def _zoom(c) -> float:
    m = c.getTotalMatrix()
    s = math.hypot(m.getScaleX(), m.getSkewY())
    return 2 ** (round(math.log2(max(s, 1e-4)) * 4) / 4)  # quarter-octave steps keep the cache small


def indic_width(text, size, role="serif"):
    px = max(8, int(round(size)))
    return pil_font(px, _weight(role)).getlength(text) * size / px


def text_width(res, text, size, font="serif", track=0.0):
    if not has_indic(text):
        return _orig["text_width"](res, text, size, font, track)
    return indic_width(text, size, font)  # letter tracking would split conjuncts, so it is ignored


def draw_text(c, res, text, x, y, size, font="serif", rgb=(240, 232, 214), a=1.0, track=0.0, align="left", reveal=None):
    if not has_indic(text):
        return _orig["draw_text"](c, res, text, x, y, size, font, rgb, a, track, align, reveal)
    if a <= 0.002:
        return indic_width(text, size, font)
    px = max(8, min(1200, int(round(size * _zoom(c)))))
    img, l, t = _raster(text, px, _weight(font), tuple(int(v) for v in rgb[:3]))
    k = size / px
    total = pil_font(px, _weight(font)).getlength(text) * k
    x0 = x - total / 2 if align == "center" else x - total if align == "right" else x
    dst = skia.Rect.MakeXYWH(x0 + l * k, y + t * k, img.width() * k, img.height() * k)
    p = skia.Paint(AntiAlias=True)
    p.setAlphaf(max(0.0, min(1.0, a)))
    c.save()
    if reveal is not None and reveal < len(text):  # type-on: wipe left to right by the share of characters shown
        frac = max(0.0, reveal) / max(1, len(text))
        c.clipRect(skia.Rect.MakeLTRB(x0 - size, y - size * 3, x0 + total * frac, y + size * 2))
    c.drawImageRect(img, skia.Rect.MakeWH(img.width(), img.height()), dst, SAMPLING, p)
    c.restore()
    return total


def install(*extra_modules):
    """Patch cinematic-film's engine (and captions, if loaded) so Indic strings are shaped correctly."""
    if not features.check("raqm"):
        raise SystemExit("hindi_text: Pillow has no raqm support; `pip install --upgrade pillow` (PyPI wheels include it)")
    if not pathlib.Path(FONT).exists():
        raise SystemExit(f"hindi_text: font not found: {FONT} (set INDIC_FONT)")
    import engine  # cinematic-film/scripts is on sys.path when render.py runs a scene
    if "draw_text" not in _orig:
        _orig["draw_text"], _orig["text_width"] = engine.draw_text, engine.text_width
    mods = [engine] + [sys.modules[m] for m in ("captions",) if m in sys.modules] + list(extra_modules)
    for m in mods:
        m.draw_text, m.text_width = draw_text, text_width
    return True
