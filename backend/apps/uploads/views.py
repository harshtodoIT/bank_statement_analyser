from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .validators import validate_file
from .storage import save_temp_file


@csrf_exempt
def upload_statement(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

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

    return JsonResponse({
        "message": "File uploaded successfully.",
        "session_id": session_id,
        "file_hash": storage_info["file_hash"]
    })
