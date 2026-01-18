from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .validators import validate_file
from .storage import save_temp_file
from apps.bank_identification.detector import detect_bank_from_file
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

from apps.users.authentication import MockClerkAuthentication


@api_view(["POST"])
@authentication_classes([MockClerkAuthentication])
def upload_statement(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    # ✅ Ensure session exists
    if not request.session.session_key:
        request.session.create()

    session_id = request.session.session_key
    uploaded_file = request.FILES.get("file")

    try:
        validate_file(uploaded_file)
        storage_info = save_temp_file(uploaded_file, session_id)
    except ValueError as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )

    try:
        bank_name = detect_bank_from_file(storage_info["file_path"])
    except ValueError as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )

    return JsonResponse({
        "status": "accepted",
        "session_id": session_id,
        "file_hash": storage_info["file_hash"],
        "file_name": uploaded_file.name,
        "bank_name": bank_name
    })
