class MockClerkError(Exception):
    pass


def verify_token(token: str) -> dict:
    """
    Mock Clerk token verification.

    Expected format:
    token = "mock_<user_id>"
    Example:
    mock_user_123
    """

    if not token:
        raise MockClerkError("Missing token")

    if not token.startswith("mock_"):
        raise MockClerkError("Invalid mock token")

    user_id = token.replace("mock_", "", 1).strip()

    if not user_id:
        raise MockClerkError("Invalid user id in token")

    return {
        "clerk_user_id": user_id,
        "email": f"{user_id}@mock.local",
        "name": f"Mock User {user_id}",
    }
