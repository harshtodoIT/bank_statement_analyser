def calculate_total_credit(transactions):
    total = 0.0

    for txn in transactions:
        if txn.get("credit") is not None:
            total += txn["credit"]

    return round(total, 2)


def calculate_total_debit(transactions):
    total = 0.0

    for txn in transactions:
        if txn.get("debit") is not None:
            total += txn["debit"]

    return round(total, 2)
