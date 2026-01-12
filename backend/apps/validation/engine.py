from math import isfinite


TOLERANCE = 0.01


def validate_transactions(transactions: list) -> None:
    if not transactions:
        raise ValueError("No transactions to validate")

    previous_balance = None
    previous_signature = None
    previous_date = None

    for index, txn in enumerate(transactions):
        debit = txn["debit"] or 0
        credit = txn["credit"] or 0
        balance = txn["balance"]
        date = txn["date"]
        description = txn["description"]

        # Numeric sanity
        for value in [debit, credit, balance]:
            if not isfinite(value):
                raise ValueError("Invalid numeric value detected")

        # Defensive debit/credit check
        if (txn["debit"] is None and txn["credit"] is None) or (
            txn["debit"] is not None and txn["credit"] is not None
        ):
            raise ValueError("Invalid debit/credit state")

        # Date order check
        if previous_date and date < previous_date:
            raise ValueError("Transactions are not in chronological order")

        # Balance continuity (skip first row)
        if previous_balance is not None:
            expected = previous_balance + credit - debit
            if abs(expected - balance) > TOLERANCE:
                raise ValueError(f"Balance mismatch at transaction index {index}")

        # Duplicate consecutive transaction detection (soft)
        signature = (date, description, debit, credit)
        if signature == previous_signature:
            raise ValueError("Duplicate consecutive transactions detected")

        previous_balance = balance
        previous_signature = signature
        previous_date = date
