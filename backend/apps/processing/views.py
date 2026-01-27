from django.shortcuts import get_object_or_404
from .worker import start_async_job
from .models import ProcessingJob
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.privacy.permissions import HasPrivacyPreference


@api_view(["POST"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def start_processing(request):
    file_hash = request.data.get("file_hash")
    session_id = request.data.get("session_id")

    if not file_hash:
        return Response(
            {"error": "file_hash is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not session_id:
        return Response(
            {"error": "session_id is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # ✅ COPY PRIVACY MODE FROM USER PROFILE (CRITICAL FIX)
    privacy_mode = request.user.profile.data_retention_preference

    job = ProcessingJob.objects.create(
        user=request.user,
        session_id=session_id,
        file_hash=file_hash,
        bank_name="UNKNOWN",
        privacy_mode=privacy_mode,
        status=ProcessingJob.Status.PENDING,
    )

    start_async_job(job.id)

    return Response(
        {
            "job_id": str(job.id),
            "status": job.status,
        },
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def process_status(request, job_id):
    job = get_object_or_404(ProcessingJob, id=job_id)

    if job.user and job.user != request.user:
        raise PermissionDenied("You do not have access to this job.")

    response = {"status": job.status}

    if job.status == ProcessingJob.Status.FAILED:
        response["error"] = job.error_message

    return Response(response)
