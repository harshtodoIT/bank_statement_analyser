from django.http import JsonResponse

def ensure_session(request):
    """
    Ensures an anonymous session exists and returns the session key.
    """
    if not request.session.session_key:
        request.session.create()

    return JsonResponse({
        "session_id": request.session.session_key
    })
