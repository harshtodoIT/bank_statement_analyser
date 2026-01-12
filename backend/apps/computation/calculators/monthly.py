from datetime import datetime
from collections import defaultdict


def group_by_month(transactions):
    monthly = defaultdict(lambda: {"credit": 0.0, "debit": 0.0})

    for txn in transactions:
        if "opening" in txn["description"].lower():
            continue

        date_obj = datetime.strptime(txn["date"], "%Y-%m-%d")
        key = date_obj.strftime("%Y-%m")

        if txn.get("credit") is not None:
            monthly[key]["credit"] += txn["credit"]

        if txn.get("debit") is not None:
            monthly[key]["debit"] += txn["debit"]

    return dict(monthly)
