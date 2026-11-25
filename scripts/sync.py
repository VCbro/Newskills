#!/usr/bin/env python3
"""Install / update every upstream skill listed in scripts/sources.json.

Usage:
    python3 scripts/sync.py              # sab sources update karo
    python3 scripts/sync.py onetake      # sirf ek source update karo
    python3 scripts/sync.py --cache DIR  # clones yahan rakho (default: .cache/upstream)

Kya karta hai:
  1. Har repo ko shallow clone / pull karta hai (.cache/upstream, git-ignored).
  2. `copy` me diye paths ko is repo me copy karta hai — badi demo videos/GIFs
     aur 20 MB se badi files chhod deta hai taaki repo halka rahe.
  3. Har destination me UPSTREAM.md (author, repo, commit, license) aur
     upstream LICENSE files likhta hai — credit hamesha saath rahe.
  4. CREDITS.md ko dobara banata hai.
Hamari apni likhi files (README.md har group folder me, apne SKILL.md) ko
yeh script kabhi nahi chhooti, kyunki upstream files hamesha ek sub-folder me jaati hain.
"""
import json, os, shutil, subprocess, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = json.loads((ROOT / "scripts" / "sources.json").read_text())["sources"]
SKIP_DIRS = {".git", "node_modules", ".github", ".turbo", "dist", ".next"}
SKIP_EXT = {".mp4", ".mov", ".webm", ".mkv", ".avi", ".gif", ".m4v"}
MAX_BYTES = 20 * 1024 * 1024


def run(*cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=True, text=True, capture_output=True).stdout.strip()


def fetch(repo, cache):
    d = cache / repo.replace("/", "__")
    if (d / ".git").exists():
        run("git", "fetch", "-q", "--depth", "1", "origin", "HEAD", cwd=d)
        run("git", "reset", "-q", "--hard", "FETCH_HEAD", cwd=d)
    else:
        d.parent.mkdir(parents=True, exist_ok=True)
        run("git", "clone", "-q", "--depth", "1", "--filter=blob:limit=25m",
            f"https://github.com/{repo}.git", str(d))
    return d, run("git", "rev-parse", "HEAD", cwd=d)


def keep(path: pathlib.Path):
    if path.suffix.lower() in SKIP_EXT:
        return False
    try:
        return path.stat().st_size <= MAX_BYTES
    except OSError:
        return False


def copy_tree(src: pathlib.Path, dst: pathlib.Path):
    skipped = 0
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return 0
    if dst.exists():
        shutil.rmtree(dst)
    for dirpath, dirnames, filenames in os.walk(src):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel = pathlib.Path(dirpath).relative_to(src)
        for f in filenames:
            p = pathlib.Path(dirpath) / f
            if p.is_symlink() or not keep(p):
                skipped += 1
                continue
            out = dst / rel / f
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, out)
    return skipped


def main():
    args = sys.argv[1:]
    cache = ROOT / ".cache" / "upstream"
    if "--cache" in args:
        i = args.index("--cache"); cache = pathlib.Path(args[i + 1]).resolve(); del args[i:i + 2]
    only = set(args)
    clones = {}
    today = datetime.date.today().isoformat()
    for s in SOURCES:
        if only and s["id"] not in only:
            continue
        print(f"→ {s['id']} ({s['repo']})")
        d, sha = fetch(s["repo"], cache)
        clones[s["repo"]] = (d, sha)
        s["_commit"] = sha
        if s.get("mode") == "reference":
            continue
        first_dst = None
        for src_rel, dst_rel in s["copy"]:
            src = d / src_rel if src_rel else d
            dst = ROOT / dst_rel
            skipped = copy_tree(src, dst)
            first_dst = first_dst or (dst if dst.is_dir() else dst.parent)
            print(f"   copied {src_rel or '.'} → {dst_rel}  (skipped {skipped} media/huge files)")
            meta_dir = dst if dst.is_dir() else dst.parent
            (meta_dir / "UPSTREAM.md").write_text(
                f"# Upstream source\n\n"
                f"- **Original repo:** https://github.com/{s['repo']}\n"
                f"- **Path:** `{src_rel or '/'}`\n"
                f"- **Author / credit:** {s['author']}\n"
                f"- **License:** {s['license']}\n"
                f"- **Synced commit:** `{sha}` on {today}\n\n"
                f"Yeh files original author ki hain; sirf demo videos/GIFs aur 20 MB se badi files hata di gayi hain.\n"
                f"Update karne ke liye: `python3 scripts/sync.py {s['id']}`\n")
        for lf_src, lf_dst in s.get("license_files", []):
            if lf_src.startswith("@"):
                other, path = lf_src[1:].split(":", 1)
                od, _ = clones.get(other) or fetch(other, cache)
                p = od / path
            else:
                p = d / lf_src
            copy_tree(p, first_dst / lf_dst)
    write_credits()


def write_credits():
    lines = ["# Credits\n",
             "Is repo ki saari upstream skills unke original authors ki hain. Hamne sirf unhe ek jagah",
             "organize kiya, README/guide likhe aur kuch apni skills jodi. Commercial use se pehle har",
             "project ka license zaroor padhein.\n",
             "| Skill / folder | Original repo | Author | License |", "|---|---|---|---|"]
    for s in SOURCES:
        where = ", ".join(f"`{c[1]}`" for c in s.get("copy", [])) or s.get("note", "")
        lines.append(f"| {where} | [{s['repo']}](https://github.com/{s['repo']}) | {s['author']} | {s['license']} |")
    lines += ["", "Apni likhi skills (`skills/3d-video-studio/SKILL.md`, `threejs-3d`, `ffmpeg-video`,",
              "`3d-portfolio-website`) aur saare README/guide files: is repo ke maintainer (VCbro) ki, MIT license (`LICENSE`).", ""]
    (ROOT / "CREDITS.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
