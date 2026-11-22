"""Lightweight, reproducible checks for the static assignment deliverables."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
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

    required = [
        "AGENTS.md", "wiki/index.md", "wiki/schema.md", "wiki/log.md",
        "wiki/syntheses/lesson-outline.md", "wiki/tasks/slide-query.md",
        "wiki/tasks/qa-plan.md", "wiki/tasks/qa-runs.md",
    ]
    for path in required:
        if not (ROOT / path).is_file():
            failures.append(f"missing Wiki architecture file: {path}")

    # Check every Markdown relative link, including links across raw, papers,
    # concepts, syntheses and tasks. External articles are checked manually.
    for page in ROOT.rglob("*.md"):
        if ".git" in page.parts:
            continue
        contents = page.read_text(encoding="utf-8")
        for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", contents):
            target = urlsplit(link)
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (page.parent / unquote(target.path)).resolve()
            if not resolved.exists():
                failures.append(f"broken Markdown link: {page.relative_to(ROOT)} -> {link}")

    concepts = (
        "christmas-date", "christmas-tree", "santa-claus",
        "las-posadas", "poinsettia",
    )
    raw_names = (
        "S1-christmas-date", "S2-christmas-tree", "S3-santa-claus",
        "S4-las-posadas", "S5-poinsettia",
    )
    for number, (raw_name, concept_name) in enumerate(zip(raw_names, concepts), 1):
        source_id = f"S{number}"
        for folder, name, expected_id in (
            ("raw/papers", raw_name, source_id),
            ("wiki/papers", raw_name, f"{source_id}-NOTE"),
            ("wiki/concepts", concept_name, f"W{number}"),
        ):
            path = ROOT / folder / f"{name}.md"
            if not path.is_file():
                failures.append(f"missing {folder} file: {name}.md")
                continue
            contents = path.read_text(encoding="utf-8")
            if not contents.startswith("---\n") or f"id: {expected_id}" not in contents.split("---", 2)[1]:
                failures.append(f"missing frontmatter ID {expected_id}: {path.relative_to(ROOT)}")
            for fact in range(1, 4):
                if f"{source_id}-F{fact}" not in contents:
                    failures.append(f"missing traceable claim {source_id}-F{fact}: {path.relative_to(ROOT)}")

    slide_html = (ROOT / "slides.html").read_text(encoding="utf-8")
    slide_sections = re.findall(r'<section class="slide[^\"]*"[^>]*>.*?</section>', slide_html, re.S)
    if scans.get("slides.html") and scans["slides.html"].slides != 10:
        failures.append(f"expected 10 slides, found {scans['slides.html'].slides}")
    if len(slide_sections) == 10:
        for slide_number, wiki_number in {2: 1, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5}.items():
            section = slide_sections[slide_number - 1]
            if f'wiki.html#w{wiki_number}' not in section or "https://" not in section:
                failures.append(f"slide {slide_number} lacks Wiki W{wiki_number} or original source link")
    if slide_html.count('data-correct="true"') != 1:
        failures.append("quiz must contain exactly one correct answer")

    if failures:
        print("FAIL")
        for failure in failures:
            print("-", failure)
        raise SystemExit(1)
    print("PASS: 5 raw sources, 5 reading notes, 5 concept pages, traceable claims, Wiki architecture, 10 slides, local links and JavaScript syntax")


if __name__ == "__main__":
    main()
