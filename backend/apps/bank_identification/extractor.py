import csv
from pathlib import Path


def extract_first_part(file_path: str) -> str:
    from PyPDF2 import PdfReader
    import pandas as pd

    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return _extract_pdf_first_pages(path, PdfReader)

    if suffix == ".csv":
        return _extract_csv_head(path)

    if suffix in [".xls", ".xlsx"]:
        return _extract_excel_head(path, pd)

    raise ValueError("Unsupported file format for bank detection.")


def _extract_pdf_first_pages(path, PdfReader):
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages[:2]:
        text += page.extract_text() or ""
    return text


def _extract_csv_head(path: Path) -> str:
    lines = []
    with open(path, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 20:
                break
            lines.append(" ".join(row))
    return " ".join(lines)


def _extract_excel_head(path, pd):
    df = pd.read_excel(path, nrows=20)
    return df.to_string(index=False)