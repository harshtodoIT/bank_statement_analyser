from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .validators import validate_file


@csrf_exempt
def upload_statement(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method is allowed."},
            status=405
        )

    uploaded_file = request.FILES.get("file")

    try:
        validate_file(uploaded_file)
    except ValueError as e:
        return JsonResponse(
            {"error": str(e)},
            status=400
        )

    return JsonResponse({
        "message": "File validation passed."
    })
