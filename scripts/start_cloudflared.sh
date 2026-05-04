#!/usr/bin/env bash

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

if ! lsof -iTCP:5001 -sTCP:LISTEN >/dev/null 2>&1; then
    echo "ERROR: Gunicorn nu asculta pe 5001. Porneste mai intai: ./start_gunicorn.sh 4"
    exit 1
fi

ORIGIN_URL="${ORIGIN_URL:-http://127.0.0.1:5001}"
PROTOCOL="${CF_PROTOCOL:-http2}"

echo "Pornesc cloudflared catre origin: $ORIGIN_URL (protocol: $PROTOCOL)"
exec cloudflared tunnel \
    --url "$ORIGIN_URL" \
    --protocol "$PROTOCOL" \
    --ha-connections 1 \
    --no-autoupdate
