from collections import defaultdict
from .rules import RULES


def categorize_transactions(transactions):
    """
    transactions: list of structured transactions (dicts)
    Returns: category_summary dict
    """

    category_totals = defaultdict(float)

    for txn in transactions:
        debit = txn.get("debit")
        credit = txn.get("credit")

        # Income
        if credit and credit > 0:
            category_totals["Income"] += credit
            continue

        # Expense
        if debit and debit > 0:
            desc = (txn.get("description") or "").lower()
            matched = False

            for category, keywords in RULES.items():
                if any(k in desc for k in keywords):
                    category_totals[category] += debit
                    matched = True
                    break

            if not matched:
                category_totals["Uncategorized"] += debit

    return dict(category_totals)
