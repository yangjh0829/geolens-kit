#!/usr/bin/env bash
# GeoLens installer — macOS / Linux
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HOME}/.workbuddy/skills/geolens"

if [ -d "$DEST" ]; then
  echo "目标已存在：$DEST（请先备份或删除，本脚本不会覆盖）" >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
cp -R "$SRC" "$DEST"
rm -rf "$DEST/.git" "$DEST/__pycache__"

echo "已安装：$DEST"
echo "自检：python \"$DEST/scripts/check.py\""
echo '调用：对 agent 说「用 geolens 判这张图：<图片路径>」'
