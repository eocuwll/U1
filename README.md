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
