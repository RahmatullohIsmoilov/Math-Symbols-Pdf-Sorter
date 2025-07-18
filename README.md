# Math Symbols PDF Sorter

A Python tool to **analyze, extract, and sort PDFs based on mathematical symbols** (like ∑, ∫, π, and others).  
Designed for students, educators, and researchers who work with math-heavy PDFs and need to automatically organize or process them.

---

## Features

- **Symbol Extraction** – Scans PDFs to detect mathematical symbols.
- **Automatic Sorting** – Groups PDFs into folders (e.g., `integrals/`, `summations/`, `greek_letters/`).
- **Batch Processing** – Process multiple PDFs at once.
- **Customizable** – Easy to tweak for specific symbol sets or workflows.
- **Lightweight** – Runs locally without complex dependencies.

---

## Dependencies

Make sure you have **Python 3.8+** installed, then install these:

```bash
pip install PyPDF2
pip install pdfminer.six
pip install reportlab
pip install tqdm
pip install pillow
