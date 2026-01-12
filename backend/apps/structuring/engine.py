from datetime import datetime
from .schema import validate_transaction_schema

def _parse_date(value: str) -> str:
    value = value.strip()

    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except Exception:
            continue

    raise ValueError("Invalid date format")


def _parse_amount(value):
    """Parse amount only if non-empty. Returns None for empty values."""
    if value is None:
        return None

    value = str(value).strip()

    # Return None for empty values (do not validate)
    if value == "":
        return None

    # Validate numeric value only if non-empty
    try:
        amount = float(value)
    except (ValueError, TypeError):
        raise ValueError("Invalid numeric value")

    if amount == 0:
        return None

    if amount < 0:
        raise ValueError("Negative amounts are not allowed")

    return amount


def structure_rows(raw_rows: list) -> list:
    structured = []

    for row in raw_rows:
        raw = row.get("raw")

        if not raw:
            continue

        # Skip header row
        if str(raw[0]).strip().lower() == "date":
            continue

        # Strict column count enforcement
        if len(raw) != 5:
            raise ValueError("Invalid column count in transaction row")

        # Strip all values before processing
        date_raw = str(raw[0]).strip() if raw[0] is not None else ""
        description_raw = str(raw[1]).strip() if raw[1] is not None else ""
        debit_raw = str(raw[2]).strip() if raw[2] is not None else ""
        credit_raw = str(raw[3]).strip() if raw[3] is not None else ""
        balance_raw = str(raw[4]).strip() if raw[4] is not None else ""

        # Skip header row deterministically (check after stripping)
        if date_raw.lower() == "date":
            continue

        # Parse amounts (only validates if non-empty)
        debit = _parse_amount(debit_raw)
        credit = _parse_amount(credit_raw)
        balance = _parse_amount(balance_raw)

        # Balance is mandatory
        if balance is None:
            raise ValueError("Balance is mandatory and missing")

        # Enforce rule: exactly one of debit or credit must be present
        if debit is None and credit is None:
            raise ValueError("Row must have exactly one of debit or credit")
        if debit is not None and credit is not None:
            raise ValueError("Row must have exactly one of debit or credit")

        txn = {
            "date": _parse_date(date_raw),
            "description": description_raw,
            "debit": debit,
            "credit": credit,
            "balance": balance,
        }

        validate_transaction_schema(txn)
        structured.append(txn)

    if not structured:
        raise ValueError("No valid transactions found")

    return structured
