# Local patches

`scripts/patches/cinematic-film.py` (in this repo) makes letter counting work for Hindi and other
non-Latin scripts in `split_takes.py`, `captions.py` and `make_beats.py`, and adds the danda `।` as a sentence end.
It is re-applied after every `python3 scripts/sync.py cinematic-film`.
