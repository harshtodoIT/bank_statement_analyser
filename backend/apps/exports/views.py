from django.http import FileResponse
from django.shortcuts import get_object_or_404

from apps.results.models import ProcessingResult
from .services import get_export_data
from .csv_export import generate_csv
from .pdf_export import generate_pdf


def export_csv(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)
    report = get_export_data(result)

    file_path = generate_csv(report)
    return FileResponse(open(file_path, "rb"), as_attachment=True)


def export_pdf(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)
    report = get_export_data(result)

    file_path = generate_pdf(report)
    return FileResponse(open(file_path, "rb"), as_attachment=True)