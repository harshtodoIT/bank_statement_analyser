from collections import defaultdict


def build_category_summary(transactions):
    categories = defaultdict(float)

    for txn in transactions:
        category = txn.get("category") or "Uncategorized"

        if txn["debit"]:
            categories[category] += float(txn["debit"])

    return dict(categories)
