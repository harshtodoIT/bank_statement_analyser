import pandas as pd


class ExcelParser:
    def parse(self, file_path: str) -> list:
        rows = []

        try:
            df = pd.read_excel(file_path, header=None)
        except Exception:
            raise ValueError("Failed to read Excel file.")

        if df.empty:
            raise ValueError("Excel file is empty.")

        for index, row in df.iterrows():
            cleaned_row = [
                "" if pd.isna(cell) else str(cell).strip()
                for cell in row.tolist()
            ]

            rows.append({
                "row_index": index + 1,
                "raw": cleaned_row
            })

        return rows
