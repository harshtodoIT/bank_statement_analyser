from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import UserProfile
from apps.users.mock_clerk import verify_token, MockClerkError

User = get_user_model()


class MockClerkAuthentication(BaseAuthentication):
    """
    DRF authentication using mocked Clerk tokens.
    """

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None  # allow unauthenticated access (for now)

        if not auth_header.startswith("Bearer "):
            raise AuthenticationFailed("Invalid authorization header")

        token = auth_header.replace("Bearer ", "", 1).strip()

        try:
            payload = verify_token(token)
        except MockClerkError as e:
            raise AuthenticationFailed(str(e))

        clerk_user_id = payload["clerk_user_id"]
        email = payload["email"]
        name = payload.get("name", "")

        # Get or create Django user
        user, created = User.objects.get_or_create(
            username=clerk_user_id,
            defaults={
                "email": email,
                "first_name": name,
            },
        )

        # Ensure UserProfile exists
        UserProfile.objects.get_or_create(
            user=user,
            defaults={
                "clerk_user_id": clerk_user_id,
            },
        )

        return (user, None)
