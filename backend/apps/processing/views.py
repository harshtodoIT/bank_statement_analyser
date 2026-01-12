import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import ProcessingJob


@csrf_exempt
def start_processing(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    if not request.session.session_key:
        return JsonResponse(
            {"error": "Session not found."},
            status=401
        )

    data = request.POST or {}
    file_hash = data.get("file_hash")

    if not file_hash:
        return JsonResponse(
            {"error": "file_hash is required."},
            status=400
        )

    # Verify file exists in temp storage
    tmp_root = settings.MEDIA_ROOT / "tmp" / request.session.session_key

    if not tmp_root.exists():
        return JsonResponse(
            {"error": "No uploaded files found for this session."},
            status=404
        )

    # Find file by hash (simple scan for Phase 1)
    file_path = None
    for f in tmp_root.iterdir():
        if f.is_file():
            file_path = f
            break

    if not file_path:
        return JsonResponse(
            {"error": "Uploaded file not found."},
            status=404
        )

    job = ProcessingJob.objects.create(
        session_id=request.session.session_key,
        file_hash=file_hash,
        bank_name="UNKNOWN",
        status=ProcessingJob.Status.PENDING,
    )

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

