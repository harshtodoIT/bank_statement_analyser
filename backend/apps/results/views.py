from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import ProcessingResult
from apps.manual_adjustments.models import ManualAdjustment


def get_summary(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)

    if result.status == "FAILED":
        return JsonResponse({
            "status": "FAILED",
            "error": result.error
        })

    adjustments_qs = ManualAdjustment.objects.filter(result=result)

    adjustments = []
    total_manual = 0.0

    for adj in adjustments_qs:
        amount = float(adj.amount)
        total_manual += amount

        adjustments.append({
            "label": adj.label,
            "amount": amount,
            "note": adj.note,
        })

    net_with_manual = result.net_cash_flow + total_manual

    return JsonResponse({
        "status": "SUCCESS",
        "data": {
            "totals": result.totals,
            "monthly_summary": result.monthly_summary,
            "net_cash_flow": result.net_cash_flow,
            "manual_adjustments": adjustments,
            "net_cash_flow_with_manual": round(net_with_manual, 2),
            "category_summary": result.categorized_summary or {},

            # ✅ Newly added (used by dashboard)
            "total_transactions": result.total_transactions,
            "bank_name": result.bank_name,
        }
    })
