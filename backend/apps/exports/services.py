from .csv_export import generate_csv
from .pdf_export import generate_pdf


def export_statement(report_data, transactions, manual_adjustments, export_type):
    """
    export_type: 'csv' or 'pdf'
    """

    if export_type == "csv":
        return generate_csv(report_data, transactions, manual_adjustments)

    if export_type == "pdf":
        return generate_pdf(report_data, transactions, manual_adjustments)

    raise ValueError("Unsupported export type")
