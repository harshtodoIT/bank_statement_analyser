import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import get_object_or_404
from .worker import start_async_job
from .models import ProcessingJob
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from apps.users.authentication import MockClerkAuthentication

@api_view(["POST"])
@authentication_classes([MockClerkAuthentication])
def start_processing(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    file_hash = request.POST.get("file_hash")
    session_id = request.POST.get("session_id")

    if not file_hash:
        return JsonResponse(
            {"error": "file_hash is required."},
            status=400
        )

    if not session_id:
        return JsonResponse(
            {"error": "session_id is required."},
            status=400
        )

    tmp_root = settings.MEDIA_ROOT / "tmp" / session_id

    if not tmp_root.exists():
        return JsonResponse(
            {"error": "Upload session not found."},
            status=404
        )

    files = [f for f in tmp_root.iterdir() if f.is_file()]
    if not files:
        return JsonResponse(
            {"error": "Uploaded file not found."},
            status=404
        )

    job = ProcessingJob.objects.create(
        session_id=session_id,
        file_hash=file_hash,
        bank_name="UNKNOWN",
        status=ProcessingJob.Status.PENDING,
        user=request.user,
    )

    start_async_job(job.id)

    return JsonResponse({
        "job_id": str(job.id),
        "status": job.status
    })

def process_status(request, job_id):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Only GET method is allowed."},
            status=405
        )

    job = get_object_or_404(ProcessingJob, id=job_id)

    response = {
        "status": job.status
    }

    if job.status == ProcessingJob.Status.FAILED:
        response["error"] = job.error_message

    return JsonResponse(response)

