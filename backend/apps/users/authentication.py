import jwt
import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


CLERK_AUDIENCE = "bank-statement-analyser-api"


class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        if not auth_header.startswith("Bearer "):
            raise AuthenticationFailed("Invalid authorization header")

        token = auth_header.split(" ", 1)[1]

        try:
            # Decode without verification to get issuer
            unverified_payload = jwt.decode(
                token,
                options={"verify_signature": False},
            )

            issuer = unverified_payload.get("iss")
            if not issuer:
                raise AuthenticationFailed("Invalid Clerk token")

            if not issuer.startswith("https://"):
                raise AuthenticationFailed("Invalid issuer")

            jwks_url = f"{issuer}/.well-known/jwks.json"
            jwks = requests.get(jwks_url, timeout=5).json()

            unverified_header = jwt.get_unverified_header(token)
            kid = unverified_header.get("kid")

            key = None
            for jwk in jwks["keys"]:
                if jwk["kid"] == kid:
                    key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk)
                    break

            if not key:
                raise AuthenticationFailed("Invalid token key")
                
            payload = jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=CLERK_AUDIENCE,
                issuer=issuer,
            )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")

        except Exception as e:
            raise AuthenticationFailed(str(e))

        # except Exception:
        #     raise AuthenticationFailed("Invalid or expired token")

        clerk_user_id = payload.get("sub")
        email = payload.get("email")

        if not clerk_user_id:
            raise AuthenticationFailed("Invalid Clerk token")

        user, _ = User.objects.get_or_create(
            username=clerk_user_id,
            defaults={"email": email or ""},
        )

        return (user, None)
