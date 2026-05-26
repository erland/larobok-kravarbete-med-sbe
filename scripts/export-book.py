#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
EXPORTS = ROOT / "exports"


def load_metadata() -> dict:
    candidates = [ROOT / "book.yaml", ROOT / "docs" / "export-metadata.yaml"]
    for path in candidates:
        if path.exists():
            if yaml is None:
                raise SystemExit("PyYAML saknas. Installera med: pip install pyyaml")
            return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raise SystemExit("Saknar book.yaml eller docs/export-metadata.yaml.")


def validate_metadata(meta: dict) -> None:
    required = ["title", "author", "language", "identifier", "date", "version", "chapters"]
    missing = [key for key in required if not meta.get(key)]
    if missing:
        raise SystemExit(f"Metadata saknar obligatoriska fält: {', '.join(missing)}")
    if meta["language"] not in ("sv", "en"):
        raise SystemExit("Metadatafältet language måste vara 'sv' eller 'en'.")
    chapters = meta.get("chapters") or []
    if not chapters or chapters[0] != "chapters/00-inledning.md":
        raise SystemExit("Kapitelordningen måste börja med chapters/00-inledning.md.")


def table_cell_count(line: str) -> int:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return -1
    return len([part for part in stripped.strip("|").split("|")])


def strip_fenced_blocks(text: str) -> str:
    """Returnerar text där kodblock ersatts med tomma rader.

    Valideringen ska kontrollera bokens markdown, inte markdown- eller
    Gherkin-exempel som visas inuti kodblock. Antalet rader bevaras så att
    felmeddelanden fortfarande pekar ungefär rätt.
    """
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def validate_markdown(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    if text.count("```") % 2 != 0:
        errors.append("Har ojämnt antal kodblocksmarkörer.")
    check_text = strip_fenced_blocks(text)
    if re.search(r"^#{4,}\s", check_text, flags=re.MULTILINE):
        errors.append("Innehåller H4 eller djupare rubrik.")
    if len(re.findall(r"^#\s", check_text, flags=re.MULTILINE)) != 1:
        errors.append("Ska ha exakt en H1-rubrik utanför kodblock.")
    # Very simple table consistency check.
    lines = check_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and line.strip().endswith("|"):
            if i + 1 >= len(lines) or not re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", lines[i + 1]):
                errors.append(f"Tabell runt rad {i+1} saknar korrekt separatorrad.")
                i += 1
                continue
            expected = table_cell_count(line)
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|") and lines[j].strip().endswith("|"):
                if table_cell_count(lines[j]) != expected:
                    errors.append(f"Tabell runt rad {i+1} har olika antal celler.")
                    break
                j += 1
            i = j
        else:
            i += 1
    # Check image references.
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", check_text):
        target = match.group(1).split("#", 1)[0]
        if "://" in target:
            continue
        image_path = (path.parent / target).resolve()
        if not image_path.exists():
            errors.append(f"Bildreferens saknar fil: {target}")
    return errors


def collect_chapters(meta: dict) -> str:
    validate_metadata(meta)
    parts: list[str] = []
    all_errors: list[str] = []
    for chapter in meta["chapters"]:
        path = ROOT / chapter
        if not path.exists():
            all_errors.append(f"Saknar kapitel: {chapter}")
            continue
        text = path.read_text(encoding="utf-8")
        errs = validate_markdown(path, text)
        all_errors.extend([f"{chapter}: {err}" for err in errs])
        parts.append(text.strip() + "\n")
    if all_errors:
        raise SystemExit("Valideringen stoppade exporten:\n- " + "\n- ".join(all_errors))
    BUILD.mkdir(exist_ok=True)
    combined = "\n\n".join(parts)
    out = BUILD / "book.md"
    out.write_text(combined, encoding="utf-8")
    return str(out)


def ensure_pandoc() -> None:
    if shutil.which("pandoc") is None:
        raise SystemExit(
            "Pandoc hittades inte. Installera Pandoc och kör exporten igen. "
            "För PDF behövs även en PDF-engine, exempelvis xelatex från MacTeX eller TinyTeX."
        )


def run(cmd: list[str]) -> None:
    print("Kör:", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def export_epub(meta: dict, book_md: str) -> None:
    ensure_pandoc()
    EXPORTS.mkdir(exist_ok=True)
    cmd = [
        "pandoc", book_md,
        "--from=gfm",
        "--to=epub3",
        "--metadata", f"title={meta['title']}",
        "--metadata", f"author={meta['author']}",
        "--metadata", f"lang={'sv-SE' if meta['language'] == 'sv' else 'en'}",
        "--css=styles/epub.css",
        "--output=exports/book.epub",
    ]
    cover = meta.get("cover_image")
    if cover and (ROOT / cover).exists():
        cmd.insert(-1, f"--epub-cover-image={cover}")
    run(cmd)


def export_pdf(meta: dict, book_md: str) -> None:
    ensure_pandoc()
    EXPORTS.mkdir(exist_ok=True)
    if shutil.which("xelatex") is None:
        raise SystemExit(
            "xelatex hittades inte. Installera MacTeX/TinyTeX eller ändra PDF-engine i scripts/export-book.py."
        )
    cmd = [
        "pandoc", book_md,
        "--from=gfm",
        "--pdf-engine=xelatex",
        "--toc",
        "--toc-depth=3",
        "--metadata", f"title={meta['title']}",
        "--metadata", f"author={meta['author']}",
        "--metadata", f"lang={'sv-SE' if meta['language'] == 'sv' else 'en'}",
        "--output=exports/book.pdf",
    ]
    run(cmd)


def export_markdown(book_md: str) -> None:
    EXPORTS.mkdir(exist_ok=True)
    target = EXPORTS / "book.md"
    target.write_text(Path(book_md).read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Skrev {target}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exportera bokprojekt till EPUB/PDF/Markdown.")
    parser.add_argument("format", choices=["epub", "pdf", "markdown", "all"], nargs="?", default="all")
    args = parser.parse_args()

    meta = load_metadata()
    book_md = collect_chapters(meta)

    if args.format in ("markdown", "all"):
        export_markdown(book_md)
    if args.format in ("epub", "all"):
        export_epub(meta, book_md)
    if args.format in ("pdf", "all"):
        export_pdf(meta, book_md)

    print("Export klar.")


if __name__ == "__main__":
    main()
