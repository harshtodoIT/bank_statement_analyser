import csv
from datetime import datetime


def generate_csv(report_data, transactions, manual_adjustments):
    filename = f"statement_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Date", "Description", "Debit", "Credit",
            "Balance", "Category", "Is Manual"
        ])

        # Bank transactions
        for txn in transactions:
            writer.writerow([
                txn.get("date"),
                txn.get("description"),
                txn.get("debit"),
                txn.get("credit"),
                txn.get("balance"),
                txn.get("category", "Uncategorized"),
                "No"
            ])

        # Manual adjustments
        for adj in manual_adjustments:
            writer.writerow([
                "",
                adj.get("label"),
                adj.get("amount") if adj.get("amount", 0) < 0 else "",
                adj.get("amount") if adj.get("amount", 0) > 0 else "",
                "",
                "Manual",
                "Yes"
            ])

    return {
        "success": True,
        "file": filename
    }
