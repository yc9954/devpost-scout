#!/bin/zsh
# One command, four steps: speak the script, shoot it flat, put the camera and
# the pointer on afterwards, lay the voice over it.
#
# The camera and the cursor are not in the capture. Chrome only hands over a
# frame when the picture changes, so anything continuous — a zoom, a pointer —
# used to be pinned to whatever rate the encoder could manage, which is where
# the stutter came from. Shot flat, the only thing bound to that rate is the
# page's own state changing, which is genuinely discontinuous. The motion is
# drawn here, at sixty.
set -e
cd "$(dirname "$0")/.."
ENGINE=${ENGINE:-say}
OUT=${1:-demo.mp4}
FLAT=${FLAT:-film/.flat}

python3 film/narrate.py --engine "$ENGINE"
python3 film/record.py --flat --flat-dir "$FLAT" --width 1920 --height 1440 \
  --scale 1.0 --out /tmp/warrant-flat.mp4
python3 film/compose.py --frames "$FLAT" --track "$FLAT/track.json" \
  --cursor "$FLAT/cursor.json" --fps 60 --max-upscale 1.25 --max-zoom 1.35 \
  --out /tmp/warrant-silent.mp4
python3 film/mux.py --video /tmp/warrant-silent.mp4 --no-subs --out "$OUT"
echo "\n$OUT is ready. Subtitles: film/narration.srt"
echo "If it runs long, film/brisk.py plays a window faster rather than cutting it:"
echo "  python3 film/brisk.py --in $OUT --out short.mp4 --window 78:95 --rate 1.25 \\"
echo "      --srt film/narration.srt" 
