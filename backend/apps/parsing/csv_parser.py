import csv


class CSVParser:
    def parse(self, file_path: str) -> list:
        rows = []

        with open(file_path, newline="", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader, start=1):
                cleaned_row = [cell.strip() for cell in row]

                rows.append({
                    "row_index": index,
                    "raw": cleaned_row
                })

        if not rows:
            raise ValueError("CSV file is empty.")

        return rows
