#!/usr/bin/env bash
# ./run.sh — build the web UI if it is missing, start the server, open the browser.
set -euo pipefail
cd "$(dirname "$0")"

PORT="${SCOUT_PORT:-8780}"
URL="http://127.0.0.1:${PORT}"

if [ ! -f web/dist/index.html ] && [ -f web/package.json ] && command -v npm >/dev/null 2>&1; then
  echo "run.sh: web/dist missing — building web/ …"
  (cd web && { [ -d node_modules ] || npm install; } && npm run build) || \
    echo "run.sh: web build failed; serving the API-only page instead"
fi

if [ ! -x .venv/bin/python ]; then
  PYTHON_FOR_VENV="$(command -v python3.12 || command -v python3)"
  "$PYTHON_FOR_VENV" -m venv .venv
fi
if ! .venv/bin/python -c 'import openai_codex' >/dev/null 2>&1; then
  echo "run.sh: installing the local Codex SDK …"
  .venv/bin/python -m pip install -r requirements-codex.txt
fi

.venv/bin/python -m scout --port "$PORT" &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT INT TERM

for _ in $(seq 1 40); do
  if curl -s --max-time 1 "$URL/api/health" >/dev/null 2>&1; then break; fi
  sleep 0.25
done

case "$(uname -s)" in
  Darwin) open "$URL" ;;
  Linux)  command -v xdg-open >/dev/null 2>&1 && xdg-open "$URL" || true ;;
esac

echo "run.sh: Workspace at $URL (Ctrl-C to stop)"
wait "$SERVER_PID"
