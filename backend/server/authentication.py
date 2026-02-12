import jwt
import requests
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Bearer "):
            return None

        token = auth.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                options={"verify_signature": False}
            )
        except Exception:
            raise AuthenticationFailed("Invalid Clerk token")

        return (payload, None)
