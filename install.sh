#!/usr/bin/env bash
# Copies skill folders into an agent's skills directory. Runs no skill code.
# Usage: ./install.sh [--target DIR] [--force] [--list] <group|skill>...
# Groups: custom workflow firebase anthropic community all
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${SKILLS_DIR:-$HOME/.claude/skills}"
FORCE=0
LIST=0
ITEMS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --force) FORCE=1; shift ;;
    --list) LIST=1; shift ;;
    -h|--help) sed -n 2,4p "$0"; exit 0 ;;
    *) ITEMS+=("$1"); shift ;;
  esac
done
GROUPS_ALL="custom workflow firebase anthropic community"
skills_in() { find "$ROOT/skills/$1" -mindepth 2 -maxdepth 2 -name SKILL.md -exec dirname {} \; | sort; }
if [ "$LIST" = 1 ]; then
  for g in $GROUPS_ALL; do
    echo "[$g]"
    skills_in "$g" | xargs -n1 basename | sed 's/^/  /'
  done
  exit 0
fi
if [ ${#ITEMS[@]} -eq 0 ]; then
  echo "Name at least one group or skill. See --list." >&2
  exit 1
fi
mkdir -p "$TARGET"
copied=0
skipped=0
copy_one() {
  local src="$1" name
  name="$(basename "$src")"
  if [ -e "$TARGET/$name" ] && [ "$FORCE" = 0 ]; then
    echo "skip (exists): $name"
    skipped=$((skipped + 1))
    return
  fi
  rm -rf "${TARGET:?}/$name"
  cp -R "$src" "$TARGET/$name"
  copied=$((copied + 1))
}
for item in "${ITEMS[@]}"; do
  if [ "$item" = all ]; then
    for g in $GROUPS_ALL; do
      while IFS= read -r s; do copy_one "$s"; done < <(skills_in "$g")
    done
  elif [ -d "$ROOT/skills/$item" ]; then
    while IFS= read -r s; do copy_one "$s"; done < <(skills_in "$item")
  else
    found="$(find "$ROOT/skills" -mindepth 3 -maxdepth 3 -name SKILL.md -path "*/$item/SKILL.md" -exec dirname {} \; | head -1)"
    if [ -z "$found" ]; then
      echo "not found: $item" >&2
      exit 1
    fi
    copy_one "$found"
  fi
done
echo "Installed $copied, skipped $skipped, target $TARGET"
