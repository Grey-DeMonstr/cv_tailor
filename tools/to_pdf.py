#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
"""Render a cover letter (.txt) or a CV (.md) to PDF.

    python tools/to_pdf.py jobs/<company>/cover_letter.txt
    python tools/to_pdf.py jobs/<company>/cv.md [-o somewhere.pdf]

Windows only. Prints HTML with headless Chrome or Edge, so it needs no LaTeX, wkhtmltopdf
or weasyprint. Markdown goes through pandoc first, which must be installed for .md input.

Output defaults to the input path with a .pdf extension. One page for a normal letter.
"""
import argparse
import html
import io
import os
import subprocess
import sys
import tempfile

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page { size: A4; margin: %(margin)s; }
body { font-family: "Source Serif Pro", Georgia, "Times New Roman", serif;
       font-size: 11.5pt; line-height: 1.55; color: #111; margin: 0; }
p { margin: 0 0 11pt 0; }
h1 { font-size: 20pt; margin: 0 0 2pt 0; }
h2 { font-size: 12pt; margin: 16pt 0 6pt 0; border-bottom: 1px solid #bbb;
     padding-bottom: 2pt; text-transform: uppercase; letter-spacing: 0.5pt; }
h3 { font-size: 11.5pt; margin: 10pt 0 2pt 0; }
ul { margin: 0 0 8pt 0; padding-left: 16pt; }
li { margin: 0 0 3pt 0; }
a { color: #111; text-decoration: none; }
"""


def find_chrome():
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    sys.exit("No Chrome or Edge found. Add its path to CHROME_CANDIDATES in tools/to_pdf.py.")


def text_to_html(text):
    """Plain text: blank lines separate paragraphs, hard wraps inside one are joined."""
    paras = [" ".join(p.split()) for p in text.strip().split("\n\n") if p.strip()]
    return "\n".join("<p>%s</p>" % html.escape(p) for p in paras)


def markdown_to_html(path):
    try:
        return subprocess.run(
            ["pandoc", "-f", "gfm", "-t", "html5", path],
            check=True, capture_output=True, text=True, encoding="utf-8",
        ).stdout
    except FileNotFoundError:
        sys.exit("pandoc not found, and it is needed for markdown input.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    ap.add_argument("--margin", default="25mm 22mm", help='CSS @page margin, default "25mm 22mm"')
    args = ap.parse_args()

    src = os.path.abspath(args.input)
    out = os.path.abspath(args.output or os.path.splitext(src)[0] + ".pdf")

    if src.lower().endswith(".md"):
        body = markdown_to_html(src)
    else:
        body = text_to_html(io.open(src, encoding="utf-8").read())

    doc = ('<!doctype html><meta charset="utf-8"><title>%s</title><style>%s</style>\n%s\n'
           % (html.escape(os.path.basename(src)), CSS % {"margin": args.margin}, body))

    fd, tmp = tempfile.mkstemp(suffix=".html")
    os.close(fd)
    io.open(tmp, "w", encoding="utf-8").write(doc)
    try:
        subprocess.run(
            [find_chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             "--print-to-pdf=" + out, "file:///" + tmp.replace("\\", "/")],
            check=True, capture_output=True,
        )
    finally:
        os.remove(tmp)
    print(out)


if __name__ == "__main__":
    main()
