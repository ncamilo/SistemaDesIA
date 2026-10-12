#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_PYTHON="$SCRIPT_DIR/../.venv/bin/python"
if [[ ! -x "$PROJECT_PYTHON" ]]; then
    PROJECT_PYTHON="${PYTHON:-python3.11}"
fi
exec "$PROJECT_PYTHON" "$SCRIPT_DIR/dev.py" "${1:-check}"
