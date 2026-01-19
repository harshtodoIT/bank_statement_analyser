from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .models import ProcessingResult
from apps.manual_adjustments.models import ManualAdjustment
from apps.users.authentication import MockClerkAuthentication


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([MockClerkAuthentication])
def get_summary(request, job_id):
    result = get_object_or_404(
        ProcessingResult,
        job_id=job_id,
    )

    # 🔐 Ownership check
    if result.user and result.user != request.user:
        raise PermissionDenied("You do not have access to this result.")

    if result.status == "FAILED":
        return Response(
            {
                "status": "FAILED",
                "error": result.error,
            },
            status=status.HTTP_200_OK,
        )

    adjustments_qs = ManualAdjustment.objects.filter(
        user=request.user
    )

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

    net_with_manual = (result.net_cash_flow or 0) + total_manual

    return Response(
        {
            "status": "SUCCESS",
            "data": {
                "totals": result.totals,
                "monthly_summary": result.monthly_summary,
                "net_cash_flow": result.net_cash_flow,
                "manual_adjustments": adjustments,
                "net_cash_flow_with_manual": round(net_with_manual, 2),
                "category_summary": result.categorized_summary or {},
                "total_transactions": result.total_transactions,
                "bank_name": result.bank_name,
            },
        },
        status=status.HTTP_200_OK,
    )
