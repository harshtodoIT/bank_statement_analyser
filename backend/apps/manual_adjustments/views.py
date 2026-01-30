import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from apps.results.models import ProcessingResult
from .models import ManualAdjustment
from .validators import validate_label, validate_amount, validate_note
from apps.privacy.permissions import HasPrivacyPreference


@api_view(["POST"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def create_manual_adjustment(request, job_id):
    """
    Create a manual adjustment for a processed bank statement.
    - User must be authenticated (Clerk)
    - Job must belong to user
    - Job must be SUCCESS
    """

    # 🔒 Validate job ownership + status
    result = get_object_or_404(
        ProcessingResult,
        job_id=job_id,
        user=request.user,
        status="SUCCESS"
    )

    # 🔹 Parse JSON body
    try:
        payload = json.loads(request.body)
    except Exception:
        return Response(
            {"success": False, "error": "Invalid JSON body"},
            status=status.HTTP_400_BAD_REQUEST
        )

    label = payload.get("label")
    amount = payload.get("amount")
    note = payload.get("note")

    # 🔹 Validate fields
    error = validate_label(label)
    if error:
        return Response(
            {"success": False, "error": error},
            status=status.HTTP_400_BAD_REQUEST
        )

    error = validate_amount(amount)
    if error:
        return Response(
            {"success": False, "error": error},
            status=status.HTTP_400_BAD_REQUEST
        )

    error = validate_note(note)
    if error:
        return Response(
            {"success": False, "error": error},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 🔹 Create adjustment
    ManualAdjustment.objects.create(
        result=result,
        user=request.user,
        label=label.strip(),
        amount=amount,
        note=note,
    )

    return Response(
        {"success": True},
        status=status.HTTP_200_OK
    )
