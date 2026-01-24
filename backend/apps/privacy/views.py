from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def privacy_status(request):
    """
    Returns whether the user has already chosen a privacy preference.
    """
    profile = request.user.profile

    return Response(
        {
            "has_chosen": profile.data_retention_preference is not None,
            "privacy_mode": profile.data_retention_preference,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def choose_privacy(request):
    """
    Allows user to choose privacy mode ONCE.
    """
    profile = request.user.profile

    # ❌ Already chosen → forbidden
    if profile.data_retention_preference is not None:
        return Response(
            {"error": "Privacy preference already set and cannot be changed."},
            status=status.HTTP_403_FORBIDDEN,
        )

    privacy_mode = request.data.get("privacy_mode")

    if privacy_mode not in ["TEMPORARY", "PERSIST"]:
        return Response(
            {"error": "Invalid privacy_mode. Allowed: TEMPORARY, PERSIST"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    profile.data_retention_preference = privacy_mode
    profile.save(update_fields=["data_retention_preference"])

    return Response(
        {
            "status": "SUCCESS",
            "privacy_mode": privacy_mode,
        },
        status=status.HTTP_200_OK,
    )
