import csv
from datetime import datetime


def generate_csv(report):
    filename = f"statement_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Type", "Label", "Amount", "Month", "Credit", "Debit", "Net"])

        # Totals
        writer.writerow([
            "SUMMARY", "Total Credit", report["totals"]["credit"], "", "", "", ""
        ])
        writer.writerow([
            "SUMMARY", "Total Debit", report["totals"]["debit"], "", "", "", ""
        ])
        writer.writerow([
            "SUMMARY", "Net Cash Flow", report["yearly_summary"]["net_cash_flow"], "", "", "", ""
        ])

        # Monthly summary
        for month, data in report["monthly_summary"].items():
            writer.writerow([
                "MONTH", month, "", "", data["credit"], data["debit"], data["net"]
            ])

        # Category summary
        if report.get("category_summary"):
            for category, amount in report["category_summary"].items():
                writer.writerow([
                    "CATEGORY", category, amount, "", "", "", ""
                ])


        # Manual adjustments
        for adj in report["manual_adjustments"]:
            writer.writerow([
                "MANUAL", adj["label"], adj["amount"], "", "", "", ""
            ])

    return filename