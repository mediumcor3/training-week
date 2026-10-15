#!/usr/bin/env bash
# Usage: ./refresh.sh <file holding the sheet's CSV as base64>
# Rebuilds index.html when the sheet changed, then commits and pushes.
set -euo pipefail
cd "$(dirname "$0")"
base64 -d "$1" > data/log.csv.new
if cmp -s data/log.csv.new data/log.csv; then rm data/log.csv.new; echo "Sheet unchanged; nothing to publish."; exit 0; fi
mv data/log.csv.new data/log.csv
python3 -I build.py data/log.csv "$(TZ=America/New_York date '+%b %-d, %-I:%M %p ET')"
git add data/log.csv index.html
git commit -qm "Refresh from training sheet"
git push origin main
