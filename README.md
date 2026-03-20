# Claude Code Skills

## Installed Skills

### document-processing/pdf-processing-pro

Production-ready PDF processing toolkit installed at `~/.claude/skills/document-processing/pdf-processing-pro/`.

**Features:**
- PDF form analysis, filling, and validation
- Table extraction (CSV/Excel export)
- OCR processing for scanned PDFs
- Batch PDF operations
- Comprehensive error handling and logging

**Included scripts:**
- `analyze_form.py` - Extract form field information
- `fill_form.py` - Fill PDF forms with data
- `validate_form.py` - Validate form data before filling
- `extract_tables.py` - Extract tables to CSV/Excel
- `extract_text.py` - Extract text with formatting preservation
- `merge_pdfs.py` - Merge multiple PDFs
- `split_pdf.py` - Split PDF into individual pages
- `validate_pdf.py` - Validate PDF integrity

**Reference docs:**
- `FORMS.md` - Complete form processing guide
- `TABLES.md` - Advanced table extraction
- `OCR.md` - Scanned PDF processing

**Quick start:**
```bash
pip install pdfplumber pypdf pillow pytesseract pandas
python scripts/analyze_form.py input.pdf --output fields.json
```

---

### pdf-modification

Comprehensive PDF modification skill installed at `~/.claude/skills/pdf-modification/SKILL.md`.

**Supported operations:**

| Operation | Description |
|-----------|-------------|
| Text replacement | Replace or edit text anywhere in the PDF |
| Page management | Add, remove, reorder, rotate pages |
| Merge | Combine multiple PDFs into one |
| Split | Extract pages or split into individual files |
| Watermark | Add text or image watermarks/stamps |
| Images | Insert, replace, or remove images |
| Compression | Reduce file size, recompress embedded images |
| Encryption | Password-protect or decrypt a PDF |
| Forms | Fill, list, or flatten interactive form fields |
| Annotations | Add/remove highlights, comments, markups |
| Metadata | Edit title, author, subject, keywords |
| Headers/Footers | Add page numbers and text bands |
| Bookmarks | Add or edit the table of contents |
| Content extraction | Extract text, images, or tables to file |
| OCR | Make scanned/image PDFs searchable |
| Conversion | PDF ↔ images |

**Dependencies:**
```bash
pip install pymupdf pypdf pdfplumber reportlab pytesseract pillow pandas openpyxl
# System: sudo apt-get install tesseract-ocr  (for OCR)
```

**Trigger examples:**
- "Add a watermark to my PDF"
- "Merge these 3 PDFs into one"
- "Extract all tables from report.pdf"
- "Password-protect invoice.pdf"
- "Run OCR on this scanned document"
- "Add page numbers to presentation.pdf"
