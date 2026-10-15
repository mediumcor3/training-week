# Medium's Training Week

A read-only view of this week's training, built from Elvis's training log in Google Drive.

- `template.html` is the page; `build.py data/log.csv "<label>"` embeds a CSV export of the sheet and writes `index.html`.
- `data/log.csv` is refreshed from the Drive sheet twice a day by a scheduled Claude task that runs `refresh.sh`; GitHub Pages serves `index.html` from `main`.
