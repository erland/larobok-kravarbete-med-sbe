#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

PANDOC_VERSION = "3.1.11.1"


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True, check=True)
    match = re.search(r"pandoc\s+([^\s]+)", result.stdout.splitlines()[0])
    return match.group(1) if match else "unknown"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def postprocess_epub(epub: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="sbe-epub-") as tmp_name:
        tmp = Path(tmp_name)
        with zipfile.ZipFile(epub, "r") as zf:
            zf.extractall(tmp)

        container = tmp / "META-INF" / "container.xml"
        if not container.exists():
            return
        match = re.search(r'full-path="([^"]+)"', container.read_text(encoding="utf-8"))
        if not match:
            return
        opf = tmp / match.group(1)
        opf_text = opf.read_text(encoding="utf-8")
        nav_match = re.search(r'<item\b[^>]*properties="[^"]*nav[^"]*"[^>]*id="([^"]+)"|<item\b[^>]*id="([^"]+)"[^>]*properties="[^"]*nav[^"]*"', opf_text)
        if nav_match:
            nav_id = nav_match.group(1) or nav_match.group(2)
            opf_text = re.sub(
                rf'(<itemref\b[^>]*idref="{re.escape(nav_id)}"[^>]*)(/?>)',
                lambda m: m.group(1) if 'linear=' in m.group(1) else m.group(1) + ' linear="no"' + m.group(2),
                opf_text,
            )
            opf.write_text(opf_text, encoding="utf-8")

        temp_epub = epub.with_suffix(".tmp.epub")
        with zipfile.ZipFile(temp_epub, "w") as zf:
            mimetype = tmp / "mimetype"
            if mimetype.exists():
                zf.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
            for path in sorted(tmp.rglob("*")):
                if not path.is_file() or path == mimetype:
                    continue
                zf.write(path, path.relative_to(tmp).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
        temp_epub.replace(epub)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Reuse the repository's existing validation without changing its local export path.
    run([sys.executable, "scripts/export-book.py", "markdown"], root)

    version = pandoc_version()
    if version != PANDOC_VERSION:
        raise SystemExit(f"Pandoc {PANDOC_VERSION} krävs; hittade {version}.")

    metadata_path = root / "book.yaml"
    metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8")) or {}
    chapters = [root / rel for rel in metadata["chapters"]]
    base_name = metadata.get("project_slug", "book")
    resource_path = f"{root}:{root / 'chapters'}"
    chapter_filter = root / "publishing" / "chapter-headings.lua"

    epub = output_dir / f"{base_name}.epub"
    epub_cmd = [
        "pandoc", *map(str, chapters),
        "--from=markdown", "--to=epub3",
        "--output", str(epub),
        "--metadata-file", str(metadata_path),
        "--resource-path", resource_path,
        "--lua-filter", str(chapter_filter),
        "--toc", "--toc-depth=1",
        "--css", str(root / "publishing" / "epub.css"),
    ]
    cover = metadata.get("cover_image")
    if cover:
        epub_cmd.extend(["--epub-cover-image", str(root / cover)])
    run(epub_cmd, root)
    postprocess_epub(epub)

    if shutil.which("xelatex") is None:
        raise SystemExit("xelatex krävs för PDF-bygget.")

    pdf = output_dir / f"{base_name}.pdf"
    with tempfile.TemporaryDirectory(prefix="sbe-pdf-") as tmp_name:
        tmp = Path(tmp_name)
        front = tmp / "frontmatter.md"
        title = latex_escape(str(metadata.get("title", "")))
        subtitle = latex_escape(str(metadata.get("subtitle", "")))
        author = latex_escape(str(metadata.get("author", "")))
        cover_path = (root / metadata["cover_image"]).as_posix()
        front.write_text(
            "```{=latex}\n"
            "\\pagenumbering{gobble}\n"
            "\\thispagestyle{empty}\n"
            f"\\AddToShipoutPictureBG*{{\\AtPageLowerLeft{{\\includegraphics[width=\\paperwidth,height=\\paperheight]{{{cover_path}}}}}}}\n"
            "\\null\\clearpage\n"
            "\\thispagestyle{empty}\n"
            "\\vspace*{0.22\\textheight}\n"
            "\\begin{center}\n"
            f"{{\\Huge\\bfseries {title}}}\\par\n"
            f"\\vspace{{1em}}{{\\Large {subtitle}}}\\par\n"
            "\\vfill\n"
            f"{{\\Large {author}}}\\par\n"
            "\\end{center}\\clearpage\n"
            "\\pagenumbering{roman}\n"
            "\\phantomsection\n"
            "\\pdfbookmark[1]{Innehåll}{toc}\n"
            "\\tableofcontents\n"
            "\\clearpage\n"
            "\\pagenumbering{arabic}\n"
            "```\n",
            encoding="utf-8",
        )

        pdf_cmd = [
            "pandoc", str(front), *map(str, chapters),
            "--from=markdown+raw_tex+pipe_tables", "--to=pdf",
            "--pdf-engine=xelatex", "--output", str(pdf),
            "--resource-path", resource_path,
            "--lua-filter", str(chapter_filter),
            "--include-in-header", str(root / "publishing" / "pdf-header.tex"),
            "--metadata", "title=",
        ]
        run(pdf_cmd, root)

    print(f"OK: {epub}")
    print(f"OK: {pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
