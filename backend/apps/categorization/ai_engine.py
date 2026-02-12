from collections import defaultdict
from transformers import pipeline  # type: ignore[import]

# Predefined categories
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Health",
    "Entertainment",
    "Investment",
    "Transfer",
    "Salary",
    "Other"
]

# Load model once (important)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


def categorize_transactions(transactions):
    category_totals = defaultdict(float)
    category_items = defaultdict(list)

    for txn in transactions:
        debit = txn.get("debit")
        credit = txn.get("credit")

        # Handle income directly
        if credit and credit > 0:
            txn["category"] = "Income"
            txn["confidence"] = 1.0

            category_totals["Income"] += credit
            category_items["Income"].append(txn)
            continue

        # Only classify expenses
        if debit and debit > 0:
            description = txn.get("description") or ""

            result = classifier(description, CATEGORIES)

            best_label = result["labels"][0]
            best_score = float(result["scores"][0])

            if best_score < 0.55:
                best_label = "Other"

            txn["category"] = best_label
            txn["confidence"] = round(best_score, 3)

            category_totals[best_label] += debit
            category_items[best_label].append(txn)

    return {
        "summary": dict(category_totals),
        "transactions": dict(category_items),
    }
