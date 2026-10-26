#!/usr/bin/env bash
# Snapshot the live OpenCode provider/model list and the models.dev catalog.
# Usage: scripts/snapshot.sh [port]
set -euo pipefail
PORT="${1:-4097}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$DIR/data"

if ! curl -sf "http://127.0.0.1:$PORT/api/info" >/dev/null 2>&1; then
  echo "Starting a private OpenCode server on 127.0.0.1:$PORT ..."
  nohup opencode serve --hostname 127.0.0.1 --port "$PORT" >/tmp/opencode-serve.log 2>&1 &
  sleep 6
fi

# v2 prints "server password <pw>" on startup; a pre-existing server needs it passed in.
if [ -n "${OPENCODE_SERVER_PASSWORD:-}" ]; then
  PW="$OPENCODE_SERVER_PASSWORD"
else
  PW="$(sed -n 's/^server password //p' /tmp/opencode-serve.log 2>/dev/null | tail -n1 || true)"
fi
if [ -z "$PW" ]; then
  echo "No server password found. Re-run with OPENCODE_SERVER_PASSWORD=<pw>." >&2
  exit 1
fi

curl -sf -u "opencode:$PW" "http://127.0.0.1:$PORT/api/integration" > "$DIR/data/integration.json"
curl -sf -u "opencode:$PW" "http://127.0.0.1:$PORT/api/model"       > "$DIR/data/model.json"
curl -sf https://models.dev/api.json                                 > "$DIR/data/models.dev.json"
echo "Wrote data/integration.json, data/model.json, data/models.dev.json"
