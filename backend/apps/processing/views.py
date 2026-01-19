import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from .worker import start_async_job
from .models import ProcessingJob
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.authentication import MockClerkAuthentication

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([MockClerkAuthentication])
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

    media_root = settings.MEDIA_ROOT
    tmp_root = media_root / "tmp" / session_id

    if not media_root.exists():
        return Response(
            {"error": "Media directory not initialized"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if not tmp_root.exists():
        return Response(
            {"error": "Upload session not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    files = [f for f in tmp_root.iterdir() if f.is_file()]
    if not files:
        return Response(
            {"error": "Uploaded file not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    job = ProcessingJob.objects.create(
        user=request.user,
        session_id=session_id,
        file_hash=file_hash,
        bank_name="UNKNOWN",
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
@permission_classes([IsAuthenticated])
@authentication_classes([MockClerkAuthentication])
def process_status(request, job_id):
    job = get_object_or_404(ProcessingJob, id=job_id)

    # 🔐 Ownership check
    if job.user and job.user != request.user:
        raise PermissionDenied("You do not have access to this job.")

    response = {
        "status": job.status
    }

    if job.status == ProcessingJob.Status.FAILED:
        response["error"] = job.error_message

    return Response(response)
