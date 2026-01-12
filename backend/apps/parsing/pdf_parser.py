from PyPDF2 import PdfReader


class PDFParser:
    def parse(self, file_path: str) -> list:
        rows = []

        try:
            reader = PdfReader(file_path)
        except Exception:
            raise ValueError("Failed to read PDF file.")

        row_index = 1

        for page in reader.pages:
            text = page.extract_text()

            if not text:
                continue

            lines = text.splitlines()

            for line in lines:
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                rows.append({
                    "row_index": row_index,
                    "raw": [cleaned_line]
                })

                row_index += 1

        if not rows:
            raise ValueError("PDF file contains no readable text.")

        return rows
