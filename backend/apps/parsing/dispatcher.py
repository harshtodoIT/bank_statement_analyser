from pathlib import Path
from .pdf_parser import PDFParser
from .csv_parser import CSVParser
from .excel_parser import ExcelParser


def parse_statement(file_path: str) -> list:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return PDFParser().parse(file_path)

    if suffix == ".csv":
        return CSVParser().parse(file_path)

    if suffix in [".xls", ".xlsx"]:
        return ExcelParser().parse(file_path)

    raise ValueError("Unsupported file format for parsing.")
