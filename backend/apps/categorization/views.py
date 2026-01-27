from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from apps.processing.models import ProcessingJob
from apps.results.models import ProcessingResult
from apps.privacy.permissions import HasPrivacyPreference


@api_view(["GET"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def category_drill_down(request):
    job_id = request.query_params.get("job_id")
    category = request.query_params.get("category")

    if not job_id or not category:
        return Response(
            {"error": "job_id and category are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    job = ProcessingJob.objects.filter(
        id=job_id,
        user=request.user,
        status=ProcessingJob.Status.SUCCESS,
    ).first()

    if not job:
        raise PermissionDenied("Invalid or unauthorized job")

    result = ProcessingResult.objects.filter(
        job_id=job.id,
        user=request.user,
        status="SUCCESS",
    ).first()

    if not result:
        return Response(
            {"error": "Result not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    txs = (result.categorized_transactions or {}).get(category, [])

    return Response(
        {
            "status": "SUCCESS",
            "job_id": str(job.id),
            "category": category,
            "total_transactions": len(txs),
            "transactions": txs,
        },
        status=status.HTTP_200_OK,
    )
