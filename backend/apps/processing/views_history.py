from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.results.models import ProcessingResult
from apps.privacy.permissions import HasPrivacyPreference


@api_view(["GET"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def processing_history(request):
    """
    List all SUCCESS processing runs for the user.
    Used for History page.
    """

    results = (
        ProcessingResult.objects
        .filter(
            user=request.user,
            status="SUCCESS",
        )
        .order_by("-created_at")
    )

    data = []

    for r in results:
        data.append({
            "job_id": str(r.job_id),
            "bank_name": r.bank_name,
            "total_transactions": r.total_transactions,
            "net_cash_flow": r.net_cash_flow,
            "created_at": r.created_at,
        })

    return Response(
        {
            "status": "SUCCESS",
            "data": data,
        },
        status=status.HTTP_200_OK,
    )
