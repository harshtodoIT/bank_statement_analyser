from collections import defaultdict
from datetime import datetime


def build_monthly_summary(transactions):
    monthly = defaultdict(lambda: {"credit": 0.0, "debit": 0.0})

    for txn in transactions:
        month_key = txn["date"].strftime("%Y-%m")

        if txn["credit"]:
            monthly[month_key]["credit"] += float(txn["credit"])

        if txn["debit"]:
            monthly[month_key]["debit"] += float(txn["debit"])

    # calculate net
    for month in monthly:
        monthly[month]["net"] = (
            monthly[month]["credit"] - monthly[month]["debit"]
        )

    return dict(monthly)
