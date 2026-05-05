#!/usr/bin/env bash
# Scale video to App Store Connect preview 886x1920 (e.g. from 1290x2796).
# Trims to 30s by default (ASC often reports longer clips as "too large").
# Requires: ffmpeg (brew install ffmpeg)
#
# Usage:
#   ./scale-app-store-preview-video.sh input.mp4
#   ./scale-app-store-preview-video.sh input.mov output.mp4
#   MODE=crop ./scale-app-store-preview-video.sh input.mp4
#   MAX_SEC=0 ./scale-app-store-preview-video.sh input.mp4   # no trim
#   AVG_BR=3M ./scale-app-store-preview-video.sh input.mp4   # smaller file

set -euo pipefail

MODE="${MODE:-pad}" # pad | crop
MAX_SEC="${MAX_SEC:-30}" # 0 = no -t (full length; may fail ASC if >30s)
AVG_BR="${AVG_BR:-4M}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg not found. Install: brew install ffmpeg" >&2
  exit 1
fi

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <input-video> [output-video]" >&2
  exit 1
fi

INPUT="$1"
if [[ ! -f "$INPUT" ]]; then
  echo "Input not found: $INPUT" >&2
  exit 1
fi

if [[ $# -ge 2 ]]; then
  OUTPUT="$2"
else
  base="$(basename "$INPUT")"
  name="${base%.*}"
  dir="$(dirname "$INPUT")"
  OUTPUT="$dir/${name}_886x1920.mp4"
fi

if [[ "$MODE" == "crop" ]]; then
  VF="scale=886:1920:force_original_aspect_ratio=increase,crop=886:1920,setsar=1,fps=30"
else
  VF="scale=886:1920:force_original_aspect_ratio=decrease,pad=886:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30"
fi

FF_IN=(-y -i "$INPUT")
if [[ "$MAX_SEC" != "0" ]]; then
  FF_IN+=(-t "$MAX_SEC")
fi

MAX_BR="5.5M"
BUF_BR="11M"
if [[ "$AVG_BR" =~ ^([0-9.]+)M$ ]]; then
  max="$(awk -v a="${BASH_REMATCH[1]}" 'BEGIN { m=a*1.375; if (m>12) m=12; printf "%.2f", m }')"
  buf="$(awk -v m="$max" 'BEGIN { printf "%.2f", m*2 }')"
  MAX_BR="${max}M"
  BUF_BR="${buf}M"
fi

echo "MODE=$MODE MAX_SEC=$MAX_SEC AVG_BR=$AVG_BR maxrate=$MAX_BR"
echo "OUTPUT=$OUTPUT"

ffmpeg "${FF_IN[@]}" \
  -vf "$VF" \
  -fps_mode cfr \
  -c:v libx264 -preset medium \
  -b:v "$AVG_BR" -maxrate "$MAX_BR" -bufsize "$BUF_BR" \
  -profile:v high \
  -pix_fmt yuv420p \
  -movflags +faststart \
  -c:a aac -b:a 96k -ar 44100 -ac 2 \
  "$OUTPUT"

echo "Done."
