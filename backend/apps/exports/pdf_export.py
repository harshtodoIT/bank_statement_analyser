from datetime import datetime
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def generate_pdf(report):
    filename = f"statement_export_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    elements = []

    # Custom styles
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        textColor=colors.HexColor("#1F3A5F"),
        alignment=1
    )

    section_style = ParagraphStyle(
        "SectionStyle",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#1F3A5F")
    )

    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        textColor=colors.HexColor("#333333")
    )

    # Title
    elements.append(Paragraph("Bank Statement Summary Report", title_style))
    elements.append(Spacer(1, 20))

    # Net Cash Flow highlight box
    net_cash_flow = report["yearly_summary"]["net_cash_flow"]

    net_cash_table = Table(
        [["Net Cash Flow", f"₹ {net_cash_flow:,.2f}"]],
        colWidths=[200, 200]
    )
    net_cash_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8F1FA")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1F3A5F")),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#1F3A5F")),
        ("PADDING", (0, 0), (-1, -1), 12),
    ]))

    elements.append(net_cash_table)
    elements.append(Spacer(1, 24))

    # Monthly Summary Section
    elements.append(Paragraph("Monthly Summary", section_style))
    elements.append(Spacer(1, 10))

    table_data = [["Month", "Credit", "Debit", "Net"]]
    for month, data in report["monthly_summary"].items():
        table_data.append([
            month,
            f"{data['credit']:,.2f}",
            f"{data['debit']:,.2f}",
            f"{data['net']:,.2f}"
        ])

    monthly_table = Table(table_data, colWidths=[90, 110, 110, 110])
    monthly_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F2F2")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#333333")),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
    ]))

    elements.append(monthly_table)
    elements.append(Spacer(1, 24))

        # Category Summary
    if report.get("category_summary"):
        elements.append(Paragraph("Category Summary", section_style))
        elements.append(Spacer(1, 10))

        category_table_data = [["Category", "Amount"]]

        for category, amount in report["category_summary"].items():
            category_table_data.append([
                category,
                f"₹ {amount:,.2f}"
            ])

        category_table = Table(category_table_data, colWidths=[200, 200])
        category_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F2F2")),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("TOPPADDING", (0, 0), (-1, 0), 10),
        ]))

        elements.append(category_table)
        elements.append(Spacer(1, 24))


    # Manual Adjustments
    if report["manual_adjustments"]:
        elements.append(Paragraph("Manual Adjustments", section_style))
        elements.append(Spacer(1, 10))

        for adj in report["manual_adjustments"]:
            elements.append(
                Paragraph(
                    f"{adj['label']} : ₹ {adj['amount']:,.2f}",
                    normal_style
                )
            )

        elements.append(Spacer(1, 20))

    # Footer
    footer_text = (
        f"Generated on {datetime.now().strftime('%d %b %Y, %I:%M %p')} "
        f"| Bank Statement Analyzer"
    )
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(footer_text, styles["Italic"]))

    doc.build(elements)
    return filename
