"""Rebuild index.html from a training-log CSV snapshot.
Usage: python3 build.py <log.csv> "<snapshot label>"
(Make the CSV from an .xlsx with xlsx_to_csv.py.)"""
import base64, pathlib, sys
here = pathlib.Path(__file__).parent
csv_bytes = pathlib.Path(sys.argv[1]).read_bytes()
html = (here / "template.html").read_text()
html = (html.replace("__SNAPSHOT_B64__", base64.b64encode(csv_bytes).decode())
            .replace("__SNAPSHOT_LABEL__", sys.argv[2])
            .replace("__FILE_ID__", "1tT1WizCta1JozTiN355NR8nby2ZPMN8SDJn-22gV4kw"))
(here / "index.html").write_text(html)
print("wrote", here / "index.html", len(html), "bytes")
