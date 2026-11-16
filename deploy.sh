#!/bin/bash
# Build, QA, and the legal gate. Does not push. Usage: ./deploy.sh [--launch]
# --launch fails while GA4_ID in _build/build.py is empty.
set -e
cd "$(dirname "$0")"
MODE=""
if [ "$1" = "--launch" ]; then MODE="--launch"; fi
python3 _build/build.py $MODE
python3 _build/check.py $MODE
python3 _build/legal_gate.py check
echo "build ok ($MODE)"
