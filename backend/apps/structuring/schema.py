REQUIRED_KEYS = {"date", "description", "debit", "credit", "balance"}


def validate_transaction_schema(txn: dict):
    # Exact keys check
    if set(txn.keys()) != REQUIRED_KEYS:
        raise ValueError("Invalid transaction schema keys")

    # Date
    if not isinstance(txn["date"], str):
        raise ValueError("Date must be a string")

    # Description
    if not isinstance(txn["description"], str):
        raise ValueError("Description must be a string")

    # Debit / Credit / Balance
    for field in ["debit", "credit", "balance"]:
        value = txn[field]
        if value is not None and not isinstance(value, (int, float)):
            raise ValueError(f"{field} must be a number or null")
