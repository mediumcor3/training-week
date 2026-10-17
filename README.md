# Medium's Training Week

A read-only view of this week's training, built from Elvis's training log in Google Drive.

- `template.html` is the page; `build.py data/log.csv "<label>"` embeds a CSV export of the sheet and writes `index.html`.
- `data/log.csv` is refreshed from the Drive sheet twice a day by a scheduled Claude task that runs `refresh.sh`; GitHub Pages serves `index.html` from `main`.

## New blocks
When a block finishes and the sheet's leftmost tab moves to a new block (with "Block N" in column A above the Week 1 header), copy the old block's CSV into `data/archive/blockN.csv`. The page shows archived blocks alongside the live tab, with a block switch above the week buttons.
