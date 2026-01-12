from datetime import datetime
from .schema import validate_transaction_schema


def _parse_date(value: str) -> str:
    try:
        return datetime.strptime(value.strip(), "%d-%m-%Y").date().isoformat()
    except Exception:
        raise ValueError("Invalid date format")


def _parse_amount(value):
    if value is None:
        return None

    value = str(value).strip()
    if value == "":
        return None

    try:
        return float(value)
    except Exception:
        raise ValueError("Invalid numeric value")


def structure_rows(raw_rows: list) -> list:
    structured = []

    for row in raw_rows:
        raw = row.get("raw")

        if not raw or len(raw) < 5:
            raise ValueError("Row has insufficient columns")

        date_raw = raw[0]
        description = raw[1]
        debit_raw = raw[2]
        credit_raw = raw[3]
        balance_raw = raw[4]

        debit = _parse_amount(debit_raw)
        credit = _parse_amount(credit_raw)
        balance = _parse_amount(balance_raw)

        # Exactly one of debit or credit
        if (debit is None and credit is None) or (debit is not None and credit is not None):
            raise ValueError("Row must have exactly one of debit or credit")

        txn = {
            "date": _parse_date(date_raw),
            "description": str(description).strip(),
            "debit": debit,
            "credit": credit,
            "balance": balance,
        }

        validate_transaction_schema(txn)
        structured.append(txn)

    if not structured:
        raise ValueError("No valid transactions found")

    return structured
