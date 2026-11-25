"""Hindi / non-Latin fixes for cinematic-film, re-applied by scripts/sync.py after every update.

Upstream counts only A-Z letters to time lines and words, so a Hindi line has 0 letters and
split_takes.py divides by zero; sentence ends only know '.!?', not the Devanagari danda '।'.
Each fix is a literal replacement; if upstream changes the line, sync stops and says which one,
so the fix can be checked (or dropped if upstream fixed it).
"""
LATIN = 're.sub(r"[^A-Za-z]", "",'
UNI = 're.sub(r"[\\W\\d_]", "",'   # letters in any script (keeps Devanagari consonants and vowels)

FIXES = [
    ("scripts/split_takes.py", LATIN, UNI, 2),
    ("scripts/split_takes.py", 're.findall(r"[.!?](?=\\s+\\S)"', 're.findall(r"[.!?।](?=\\s+\\S)"', 1),
    ("scripts/captions.py", LATIN, UNI, 1),
    ("scripts/make_beats.py", LATIN, UNI, 1),
]


def apply(dest):
    for rel, old, new, count in FIXES:
        p = dest / rel
        s = p.read_text(encoding="utf-8")
        if s.count(old) != count:
            if s.count(new) == count:
                continue  # already applied
            raise SystemExit(f"patch cinematic-film: expected {count}x {old!r} in {rel}, found {s.count(old)} — upstream changed, review the fix")
        p.write_text(s.replace(old, new), encoding="utf-8")
    (dest / "PATCHES.md").write_text(
        "# Local patches\n\n`scripts/patches/cinematic-film.py` (in this repo) makes letter counting work for Hindi and other\n"
        "non-Latin scripts in `split_takes.py`, `captions.py` and `make_beats.py`, and adds the danda `।` as a sentence end.\n"
        "It is re-applied after every `python3 scripts/sync.py cinematic-film`.\n", encoding="utf-8")
