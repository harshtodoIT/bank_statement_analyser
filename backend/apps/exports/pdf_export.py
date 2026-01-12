from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_data, transactions, manual_adjustments):
    filename = f"statement_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Bank Statement Summary Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Summary section
    elements.append(Paragraph(
        f"Net Cashflow: {report_data.get('net_cashflow')}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 12))

    # Monthly summary table
    monthly = report_data.get("monthly_summary", {})
    table_data = [["Month", "Credit", "Debit", "Net"]]

    for month, data in monthly.items():
        table_data.append([
            month,
            data.get("credit"),
            data.get("debit"),
            data.get("net")
        ])

    elements.append(Table(table_data))
    elements.append(Spacer(1, 12))

    # Manual adjustments section
    elements.append(Paragraph("Manual Adjustments", styles["Heading2"]))

    for adj in manual_adjustments:
        elements.append(Paragraph(
            f"{adj.get('label')} : {adj.get('amount')}",
            styles["Normal"]
        ))

    doc.build(elements)

    return {
        "success": True,
        "file": filename
    }
