"""Rebuild index.html from a training-log CSV snapshot.
Usage: python3 build.py <log.csv> "<snapshot label>" [--standalone]
(--standalone adds the doctype/viewport head a plain web host needs, e.g. GitHub Pages.)
(Make the CSV from an .xlsx with xlsx_to_csv.py.)"""
import base64, json, pathlib, sys
here = pathlib.Path(__file__).parent
csv_bytes = pathlib.Path(sys.argv[1]).read_bytes()
html = (here / "template.html").read_text()
html = (html.replace("__SNAPSHOT_B64__", base64.b64encode(csv_bytes).decode())
            .replace("__SNAPSHOT_LABEL__", sys.argv[2])
            .replace("__ARCHIVES__", json.dumps([base64.b64encode(f.read_bytes()).decode() for f in sorted((here / "data" / "archive").glob("*.csv"))]))
            .replace("__FILE_ID__", "1tT1WizCta1JozTiN355NR8nby2ZPMN8SDJn-22gV4kw"))
if "--standalone" in sys.argv[3:]:
    html = '<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n' + html
(here / "index.html").write_text(html)
print("wrote", here / "index.html", len(html), "bytes")
