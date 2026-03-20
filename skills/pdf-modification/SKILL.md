---
name: pdf-modification
description: Comprehensive PDF modification skill. Use when the user wants to modify a PDF file in any way: edit text, add/remove pages, merge, split, rotate, add watermarks, add images, compress, encrypt/decrypt, fill forms, add annotations, reorder pages, edit metadata, add headers/footers, extract content, or run OCR on scanned PDFs.
---

# PDF Modification Skill

Complete toolkit for every possible modification on a PDF file using Python.

## Supported Operations

| Operation | Description |
|-----------|-------------|
| Text replacement | Replace or edit text in a PDF |
| Page management | Add, remove, reorder, rotate pages |
| Merge | Combine multiple PDFs into one |
| Split | Extract pages or split into multiple files |
| Watermark | Add text or image watermarks |
| Images | Insert, replace, or remove images |
| Compression | Reduce file size |
| Encryption | Password-protect or unlock a PDF |
| Forms | Fill, read, or flatten form fields |
| Annotations | Add, edit, or remove comments/highlights |
| Metadata | Edit title, author, subject, keywords |
| Headers/Footers | Add page numbers, text bands |
| Bookmarks | Add or edit the table of contents |
| Content extraction | Extract text, images, or tables |
| OCR | Make scanned/image PDFs searchable |
| Conversion | PDF → images, HTML; images → PDF |

## Dependencies

```bash
pip install pymupdf pypdf pdfplumber reportlab pytesseract pillow pandas openpyxl
# For OCR: also install tesseract-ocr system package
# sudo apt-get install tesseract-ocr   (Debian/Ubuntu)
# brew install tesseract               (macOS)
```

**Library roles:**
- `pymupdf` (import `fitz`) — core engine: text, images, annotations, watermarks, compression, rendering
- `pypdf` — merge, split, encrypt/decrypt, metadata, page rotation
- `pdfplumber` — structured text and table extraction
- `reportlab` — generate overlay content (headers, footers, stamps)
- `pytesseract` + `Pillow` — OCR on scanned PDFs
- `pandas` / `openpyxl` — export extracted tables to CSV/Excel

## Workflow

Make a todo list for all tasks in this workflow and work through them one at a time.

### 1. Identify the Operation

Ask the user (or infer from context) which modification they want:
- What is the input PDF path?
- What exact change is needed?
- What should the output file be named/where should it be saved?
- Any additional options (password, page range, replacement text, etc.)?

### 2. Check Dependencies

```bash
python3 -c "import fitz, pypdf, pdfplumber, reportlab, PIL; print('OK')"
```

If any import fails, install the missing packages before continuing.

### 3. Implement the Modification

Use the code templates below for the requested operation. Adapt as needed.

---

#### TEXT REPLACEMENT

```python
import fitz  # pymupdf

def replace_text(input_path: str, output_path: str, old_text: str, new_text: str):
    doc = fitz.open(input_path)
    for page in doc:
        # Search all instances
        instances = page.search_for(old_text)
        for rect in instances:
            # Redact the old text
            page.add_redact_annot(rect, fill=(1, 1, 1))
        page.apply_redactions()
        # Insert new text at each position
        for rect in instances:
            page.insert_text(rect.tl, new_text, fontsize=11)
    doc.save(output_path)
    doc.close()
    print(f"Replaced '{old_text}' → '{new_text}' in {output_path}")
```

> **Note:** For rich text replacement (preserving font/size), use `page.insert_htmlbox()` or overlay with reportlab.

---

#### ADD / REMOVE / REORDER PAGES

```python
from pypdf import PdfWriter, PdfReader

# --- Remove pages (0-indexed) ---
def remove_pages(input_path: str, output_path: str, pages_to_remove: list[int]):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i not in pages_to_remove:
            writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)

# --- Reorder pages ---
def reorder_pages(input_path: str, output_path: str, new_order: list[int]):
    """new_order: list of 0-based page indices in desired order"""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i in new_order:
        writer.add_page(reader.pages[i])
    with open(output_path, "wb") as f:
        writer.write(f)
```

---

#### MERGE PDFs

```python
from pypdf import PdfMerger

def merge_pdfs(input_paths: list[str], output_path: str):
    merger = PdfMerger()
    for path in input_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()
    print(f"Merged {len(input_paths)} PDFs → {output_path}")
```

---

#### SPLIT PDF

```python
from pypdf import PdfReader, PdfWriter

def split_pdf(input_path: str, output_dir: str):
    """Split each page into a separate file."""
    import os
    reader = PdfReader(input_path)
    os.makedirs(output_dir, exist_ok=True)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        out = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(out, "wb") as f:
            writer.write(f)
    print(f"Split into {len(reader.pages)} files in {output_dir}/")

def extract_page_range(input_path: str, output_path: str, start: int, end: int):
    """Extract pages start..end (1-based, inclusive)."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages[start-1:end]:
        writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)
```

---

#### ROTATE PAGES

```python
from pypdf import PdfReader, PdfWriter

def rotate_pages(input_path: str, output_path: str, angle: int, page_indices: list[int] | None = None):
    """angle: 90, 180, or 270. page_indices: None = all pages."""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if page_indices is None or i in page_indices:
            page.rotate(angle)
        writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)
```

---

#### ADD TEXT WATERMARK

```python
import fitz

def add_text_watermark(input_path: str, output_path: str, text: str,
                        opacity: float = 0.3, angle: float = 45, fontsize: int = 60):
    doc = fitz.open(input_path)
    for page in doc:
        # Center of page
        rect = page.rect
        page.insert_text(
            point=fitz.Point(rect.width / 4, rect.height / 2),
            text=text,
            fontsize=fontsize,
            rotate=angle,
            color=(0.7, 0.7, 0.7),
            overlay=True,
        )
    doc.save(output_path)
    doc.close()
```

#### ADD IMAGE WATERMARK / STAMP

```python
import fitz

def add_image_stamp(input_path: str, output_path: str, image_path: str,
                    opacity: float = 0.4, position: str = "center"):
    doc = fitz.open(input_path)
    for page in doc:
        img_rect = page.rect  # full page; adjust as needed
        page.insert_image(img_rect, filename=image_path, overlay=True)
    doc.save(output_path)
    doc.close()
```

---

#### INSERT IMAGE INTO PAGE

```python
import fitz

def insert_image(input_path: str, output_path: str, image_path: str,
                 page_num: int = 0, x: float = 50, y: float = 50,
                 width: float = 200, height: float = 150):
    doc = fitz.open(input_path)
    page = doc[page_num]
    rect = fitz.Rect(x, y, x + width, y + height)
    page.insert_image(rect, filename=image_path)
    doc.save(output_path)
    doc.close()
```

---

#### COMPRESS / REDUCE FILE SIZE

```python
import fitz

def compress_pdf(input_path: str, output_path: str, image_quality: int = 60):
    doc = fitz.open(input_path)
    # Rewrite with compression; also downscale embedded images
    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]
            base = doc.extract_image(xref)
            from PIL import Image
            import io
            pil = Image.open(io.BytesIO(base["image"]))
            buf = io.BytesIO()
            pil.save(buf, format="JPEG", quality=image_quality)
            doc.update_stream(xref, buf.getvalue())
    doc.save(output_path, garbage=4, deflate=True, clean=True)
    doc.close()
    import os
    orig = os.path.getsize(input_path)
    new = os.path.getsize(output_path)
    print(f"Compressed: {orig//1024}KB → {new//1024}KB ({100*(orig-new)//orig}% reduction)")
```

---

#### ENCRYPT (PASSWORD PROTECT)

```python
from pypdf import PdfReader, PdfWriter

def encrypt_pdf(input_path: str, output_path: str,
                user_password: str, owner_password: str | None = None):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(user_password, owner_password or user_password, use_128bit=True)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Encrypted → {output_path}")

def decrypt_pdf(input_path: str, output_path: str, password: str):
    reader = PdfReader(input_path)
    if reader.is_encrypted:
        reader.decrypt(password)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"Decrypted → {output_path}")
```

---

#### FILL PDF FORMS

```python
import fitz

def fill_form(input_path: str, output_path: str, field_data: dict):
    """field_data: {field_name: value}"""
    doc = fitz.open(input_path)
    for page in doc:
        for widget in page.widgets():
            if widget.field_name in field_data:
                widget.field_value = field_data[widget.field_name]
                widget.update()
    doc.save(output_path)
    doc.close()

def list_form_fields(input_path: str) -> list[dict]:
    doc = fitz.open(input_path)
    fields = []
    for page_num, page in enumerate(doc):
        for widget in page.widgets():
            fields.append({
                "page": page_num + 1,
                "name": widget.field_name,
                "type": widget.field_type_string,
                "value": widget.field_value,
            })
    doc.close()
    return fields

def flatten_form(input_path: str, output_path: str):
    """Make form fields non-editable (flatten)."""
    doc = fitz.open(input_path)
    for page in doc:
        for widget in page.widgets():
            widget.update()
    doc.save(output_path, incremental=False)
    doc.close()
```

---

#### ANNOTATIONS (COMMENTS, HIGHLIGHTS)

```python
import fitz

def add_highlight(input_path: str, output_path: str, page_num: int, text_to_highlight: str,
                  color: tuple = (1, 1, 0)):
    doc = fitz.open(input_path)
    page = doc[page_num]
    instances = page.search_for(text_to_highlight)
    for rect in instances:
        annot = page.add_highlight_annot(rect)
        annot.set_colors(stroke=color)
        annot.update()
    doc.save(output_path)
    doc.close()

def add_comment(input_path: str, output_path: str, page_num: int,
                x: float, y: float, comment: str, author: str = "Claude"):
    doc = fitz.open(input_path)
    page = doc[page_num]
    point = fitz.Point(x, y)
    annot = page.add_text_annot(point, comment)
    annot.set_info(title=author)
    annot.update()
    doc.save(output_path)
    doc.close()

def remove_all_annotations(input_path: str, output_path: str):
    doc = fitz.open(input_path)
    for page in doc:
        for annot in page.annots():
            page.delete_annot(annot)
    doc.save(output_path)
    doc.close()
```

---

#### EDIT METADATA

```python
from pypdf import PdfReader, PdfWriter

def edit_metadata(input_path: str, output_path: str, metadata: dict):
    """metadata keys: /Title, /Author, /Subject, /Keywords, /Creator, /Producer"""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    existing = dict(reader.metadata or {})
    existing.update(metadata)
    writer.add_metadata(existing)
    with open(output_path, "wb") as f:
        writer.write(f)

def read_metadata(input_path: str) -> dict:
    reader = PdfReader(input_path)
    return dict(reader.metadata or {})
```

---

#### ADD HEADERS / FOOTERS / PAGE NUMBERS

```python
import fitz

def add_page_numbers(input_path: str, output_path: str,
                     position: str = "bottom-center", fontsize: int = 10,
                     template: str = "Page {n} of {total}"):
    doc = fitz.open(input_path)
    total = len(doc)
    for i, page in enumerate(doc):
        text = template.format(n=i+1, total=total)
        rect = page.rect
        if position == "bottom-center":
            pt = fitz.Point(rect.width / 2 - 40, rect.height - 20)
        elif position == "top-center":
            pt = fitz.Point(rect.width / 2 - 40, 20)
        elif position == "bottom-right":
            pt = fitz.Point(rect.width - 80, rect.height - 20)
        else:
            pt = fitz.Point(20, rect.height - 20)
        page.insert_text(pt, text, fontsize=fontsize, color=(0, 0, 0))
    doc.save(output_path)
    doc.close()

def add_header_footer_text(input_path: str, output_path: str,
                            header: str | None = None, footer: str | None = None,
                            fontsize: int = 9, color: tuple = (0.4, 0.4, 0.4)):
    doc = fitz.open(input_path)
    for page in doc:
        rect = page.rect
        if header:
            page.insert_text(fitz.Point(40, 18), header, fontsize=fontsize, color=color)
        if footer:
            page.insert_text(fitz.Point(40, rect.height - 15), footer, fontsize=fontsize, color=color)
    doc.save(output_path)
    doc.close()
```

---

#### ADD / EDIT BOOKMARKS (TABLE OF CONTENTS)

```python
import fitz

def set_bookmarks(input_path: str, output_path: str, toc: list[list]):
    """
    toc format: [[level, title, page_number], ...]
    Example: [[1, "Chapter 1", 1], [2, "Section 1.1", 3]]
    """
    doc = fitz.open(input_path)
    doc.set_toc(toc)
    doc.save(output_path)
    doc.close()

def get_bookmarks(input_path: str) -> list:
    doc = fitz.open(input_path)
    toc = doc.get_toc()
    doc.close()
    return toc
```

---

#### EXTRACT TEXT

```python
import pdfplumber

def extract_text(input_path: str, output_path: str | None = None,
                 page_range: tuple | None = None) -> str:
    all_text = []
    with pdfplumber.open(input_path) as pdf:
        pages = pdf.pages
        if page_range:
            pages = pdf.pages[page_range[0]-1:page_range[1]]
        for page in pages:
            all_text.append(page.extract_text() or "")
    result = "\n\n".join(all_text)
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)
    return result
```

---

#### EXTRACT TABLES

```python
import pdfplumber
import pandas as pd

def extract_tables(input_path: str, output_path: str, fmt: str = "csv"):
    """fmt: 'csv' or 'xlsx'"""
    with pdfplumber.open(input_path) as pdf:
        all_tables = []
        for page_num, page in enumerate(pdf.pages):
            for table in page.extract_tables():
                df = pd.DataFrame(table[1:], columns=table[0])
                df.insert(0, "_page", page_num + 1)
                all_tables.append(df)
    if not all_tables:
        print("No tables found.")
        return
    combined = pd.concat(all_tables, ignore_index=True)
    if fmt == "xlsx":
        combined.to_excel(output_path, index=False)
    else:
        combined.to_csv(output_path, index=False)
    print(f"Extracted {len(all_tables)} table(s) → {output_path}")
```

---

#### EXTRACT IMAGES

```python
import fitz, os

def extract_images(input_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(input_path)
    count = 0
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base = doc.extract_image(xref)
            ext = base["ext"]
            out = os.path.join(output_dir, f"page{page_num+1}_img{img_index+1}.{ext}")
            with open(out, "wb") as f:
                f.write(base["image"])
            count += 1
    doc.close()
    print(f"Extracted {count} image(s) to {output_dir}/")
```

---

#### OCR (SCANNED PDFs → SEARCHABLE PDF)

```python
import fitz
from PIL import Image
import pytesseract
import io

def ocr_pdf(input_path: str, output_path: str, lang: str = "fra+eng", dpi: int = 300):
    """
    Render each page as image, run OCR, and embed a text layer.
    lang: tesseract language codes, e.g. 'fra', 'eng', 'fra+eng'
    """
    doc = fitz.open(input_path)
    out_doc = fitz.open()
    for page_num, page in enumerate(doc):
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Run OCR
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, lang=lang, extension="pdf")
        # Insert OCR result as page
        tmp = fitz.open("pdf", pdf_bytes)
        out_doc.insert_pdf(tmp)
        tmp.close()
        print(f"OCR page {page_num + 1}/{len(doc)}")
    out_doc.save(output_path)
    out_doc.close()
    doc.close()
    print(f"OCR complete → {output_path}")
```

---

#### CONVERT PDF → IMAGES

```python
import fitz, os

def pdf_to_images(input_path: str, output_dir: str, fmt: str = "png", dpi: int = 150):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(input_path)
    for i, page in enumerate(doc):
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        out = os.path.join(output_dir, f"page_{i+1:04d}.{fmt}")
        pix.save(out)
    doc.close()
    print(f"Saved {len(doc)} image(s) to {output_dir}/")
```

#### CONVERT IMAGES → PDF

```python
import fitz
from PIL import Image

def images_to_pdf(image_paths: list[str], output_path: str):
    doc = fitz.open()
    for path in image_paths:
        img = Image.open(path)
        w, h = img.size
        page = doc.new_page(width=w, height=h)
        page.insert_image(page.rect, filename=path)
    doc.save(output_path)
    doc.close()
    print(f"Created PDF with {len(image_paths)} pages → {output_path}")
```

---

### 4. Run the Script

Execute the script with the user's input file:

```bash
python3 pdf_modify.py
```

Verify:
- Output file exists and is not empty
- Open with a PDF viewer if possible, or use `fitz` to inspect:
  ```python
  import fitz
  doc = fitz.open("output.pdf")
  print(f"Pages: {len(doc)}, Encrypted: {doc.is_encrypted}")
  ```

### 5. Error Handling

Common issues:

| Error | Cause | Fix |
|-------|-------|-----|
| `PdfReadError: EOF marker not found` | Corrupt input PDF | Use `pypdf` with `strict=False` |
| `fitz.FileDataError` | Unsupported PDF version | Try repair: `fitz.open(input, filetype="pdf")` |
| `PermissionError` / encrypted | Password-protected | Decrypt first with `reader.decrypt(password)` |
| `tesseract not found` | Tesseract not installed | `sudo apt-get install tesseract-ocr` |
| `No module named 'fitz'` | pymupdf missing | `pip install pymupdf` |

For corrupt PDFs, attempt repair:
```python
import fitz
doc = fitz.open(input_path)
doc.save(output_path, garbage=4, clean=True, deflate=True)
```

### 6. Validate & Report

After the operation, report to the user:
- Input file: path + original size
- Output file: path + new size
- Operation performed + parameters used
- Number of pages affected
- Any warnings encountered

## Wrap up

In your final message, provide:

* **Operation performed** — what was modified and how
* **Files:**
  - Input: `path/to/input.pdf` (X KB, N pages)
  - Output: `path/to/output.pdf` (X KB, N pages)
* **Result summary** — pages changed, fields filled, text replaced, etc.
* **Validation:** ✅ Output file readable / ‼️ issue encountered
* **Next steps** — suggest related operations if relevant (e.g., "You can now encrypt the file with `/pdf-modification`")
