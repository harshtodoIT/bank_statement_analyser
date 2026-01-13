from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.results.models import ProcessingResult
from .services import generate_report


def get_report(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)

    if result.status == "FAILED":
        return JsonResponse({
            "status": "FAILED",
            "error": result.error
        })

    report = generate_report(result)

    return JsonResponse({
        "status": "SUCCESS",
        "report": report
    })