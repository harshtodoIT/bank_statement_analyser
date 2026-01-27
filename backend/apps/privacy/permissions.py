from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class HasPrivacyPreference(BasePermission):
    """
    Allows access only if the user has chosen a privacy preference.
    """

    message = "Privacy preference not selected."

    def has_permission(self, request, view):
        profile = getattr(request.user, "profile", None)

        if not profile or profile.data_retention_preference is None:
            raise PermissionDenied(self.message)

        return True
