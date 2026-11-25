#!/usr/bin/env bash
# Install every skill in this repo into Claude Code.
#   bash install.sh              -> ~/.claude/skills   (all your projects)
#   bash install.sh --project D  -> D/.claude/skills   (one project only)
#   bash install.sh --copy       -> copy instead of symlink (Windows / no symlinks)
# Claude Code finds skills one level deep (<dir>/<name>/SKILL.md), so nested skills are
# flattened here by their `name:`. Re-run after `python3 scripts/sync.py` to pick up updates.
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.claude/skills"; MODE=link
while [ $# -gt 0 ]; do
  case "$1" in
    --project) DEST="$(cd "$2" && pwd)/.claude/skills"; shift 2 ;;
    --copy) MODE=copy; shift ;;
    *) echo "unknown option $1" >&2; exit 1 ;;
  esac
done
mkdir -p "$DEST"
n=0
while IFS= read -r skill; do
  dir="$(dirname "$skill")"
  case "$dir" in */examples/*|*/fixtures/*|*/_archive/*) continue ;; esac
  name="$(awk '/^---/{c++; next} c==1 && /^name:/{sub(/^name:[ \t]*/,""); gsub(/["'\'']/,""); print; exit}' "$skill")"
  [ -n "$name" ] || continue
  target="$DEST/$name"
  rm -rf "$target"
  if [ "$MODE" = copy ]; then cp -R "$dir" "$target"; else ln -s "$dir" "$target"; fi
  n=$((n+1)); echo "  ✓ $name"
done < <(find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' | sort)
echo "Installed $n skills into $DEST ($MODE). Restart Claude Code to load them."
