from collections import defaultdict
from .rules import RULES


def categorize_transactions(transactions):
    """
    Mutates each transaction by adding:
      - category
      - confidence

    Returns:
      category_summary dict
    """

    category_totals = defaultdict(float)
    category_items = defaultdict(list)

    for txn in transactions:
        debit = txn.get("debit")
        credit = txn.get("credit")

        # -----------------
        # INCOME
        # -----------------
        if credit and credit > 0:
            txn["category"] = "Income"
            txn["confidence"] = 1.0

            category_totals["Income"] += credit
            category_items["Income"].append(txn)
            continue

        # -----------------
        # EXPENSE
        # -----------------
        if debit and debit > 0:
            desc = (txn.get("description") or "").lower()
            matched = False

            for category, keywords in RULES.items():
                if any(k in desc for k in keywords):
                    category_totals[category] += debit
                    category_items[category].append(txn)
                    matched = True
                    break


            if not matched:
                category_totals["Uncategorized"] += debit
                category_items["Uncategorized"].append(txn)

    return {
        "summary": dict(category_totals),
        "transactions": dict(category_items),
    }