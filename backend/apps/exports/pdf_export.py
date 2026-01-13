from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report):
    filename = f"statement_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Bank Statement Summary Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Totals
    elements.append(Paragraph(
        f"Net Cash Flow: {report['yearly_summary']['net_cash_flow']}",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 12))

    # Monthly table
    table_data = [["Month", "Credit", "Debit", "Net"]]
    for month, data in report["monthly_summary"].items():
        table_data.append([
            month, data["credit"], data["debit"], data["net"]
        ])

    elements.append(Table(table_data))
    elements.append(Spacer(1, 12))

    # Manual adjustments
    if report["manual_adjustments"]:
        elements.append(Paragraph("Manual Adjustments", styles["Heading2"]))
        for adj in report["manual_adjustments"]:
            elements.append(Paragraph(
                f"{adj['label']} : {adj['amount']}",
                styles["Normal"]
            ))

    doc.build(elements)
    return filename