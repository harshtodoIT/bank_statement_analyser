import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from apps.results.models import ProcessingResult
from .models import ManualAdjustment
from .validators import validate_label, validate_amount, validate_note
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def create_manual_adjustment(request, job_id):
    result = get_object_or_404(ProcessingResult, job_id=job_id)

    try:
        payload = json.loads(request.body)
    except Exception:
        return JsonResponse({"success": False, "error": "Invalid JSON body"}, status=400)

    label = payload.get("label")
    amount = payload.get("amount")
    note = payload.get("note")

    error = validate_label(label)
    if error:
        return JsonResponse({"success": False, "error": error}, status=400)

    error = validate_amount(amount)
    if error:
        return JsonResponse({"success": False, "error": error}, status=400)

    error = validate_note(note)
    if error:
        return JsonResponse({"success": False, "error": error}, status=400)

    ManualAdjustment.objects.create(
        result=result,
        user=request.user if request.user.is_authenticated else None,
        label=label.strip(),
        amount=amount,
        note=note,
    )

    return JsonResponse({"success": True})
