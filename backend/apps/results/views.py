from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import ProcessingResult


def get_summary(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)

    if result.status == "FAILED":
        return JsonResponse({
            "status": "FAILED",
            "error": result.error
        })

    return JsonResponse({
        "status": "SUCCESS",
        "data": {
            "totals": result.totals,
            "monthly_summary": result.monthly_summary,
            "net_cash_flow": result.net_cash_flow
        }
    })
