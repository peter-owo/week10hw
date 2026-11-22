"""Lightweight, reproducible checks for the static assignment deliverables."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
PAGES = [ROOT / name for name in ("index.html", "wiki.html", "slides.html", "process.html")]


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.slides = 0
        self.scripts = []
        self.in_script = False
        self.script_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "section" and "slide" in attrs.get("class", "").split():
            self.slides += 1
        if tag == "script" and "src" not in attrs:
            self.in_script = True
            self.script_parts = []

    def handle_data(self, data):
        if self.in_script:
            self.script_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.in_script:
            self.scripts.append("".join(self.script_parts))
            self.in_script = False


def main():
    scans = {}
    failures = []
    for page in PAGES:
        if not page.exists():
            failures.append(f"missing {page.name}")
            continue
        scan = Scan()
        scan.feed(page.read_text(encoding="utf-8"))
        scans[page.name] = scan
        for link in scan.links:
            target = urlsplit(link)
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (ROOT / unquote(target.path)).resolve()
            if not resolved.is_file():
                failures.append(f"broken local link: {page.name} -> {link}")
        for idx, script in enumerate(scan.scripts, 1):
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".js", delete=False) as temp:
                temp.write(script)
                script_path = Path(temp.name)
            try:
                check = subprocess.run(["node", "--check", str(script_path)], capture_output=True, text=True)
                if check.returncode:
                    failures.append(f"JavaScript syntax: {page.name} script {idx}: {check.stderr.strip()}")
            finally:
                script_path.unlink(missing_ok=True)

    wiki = (ROOT / "wiki.md").read_text(encoding="utf-8")
    slide_html = (ROOT / "slides.html").read_text(encoding="utf-8")
    for number in range(1, 6):
        if f"## W{number}｜" not in wiki:
            failures.append(f"missing Wiki entry W{number}")
        if f"W{number}" not in slide_html:
            failures.append(f"slides do not reference W{number}")
    if scans.get("slides.html") and scans["slides.html"].slides != 10:
        failures.append(f"expected 10 slides, found {scans['slides.html'].slides}")
    source_count = wiki.count("| S1 |") + wiki.count("| S2 |") + wiki.count("| S3 |") + wiki.count("| S4 |") + wiki.count("| S5 |")
    if source_count != 5:
        failures.append(f"expected 5 source records, found {source_count}")

    if failures:
        print("FAIL")
        for failure in failures:
            print("-", failure)
        raise SystemExit(1)
    print("PASS: 4 HTML pages, 5 Wiki source records, 10 slides, local links and inline JavaScript syntax")


if __name__ == "__main__":
    main()
