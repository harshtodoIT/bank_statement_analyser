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
    "Other",
]


def _rule_based_category(description: str) -> tuple[str, float]:
    """
    Lightweight fallback categorizer used when the HF pipeline
    (which depends on PyTorch) is not available.
    """
    text = (description or "").lower()

    rules: list[tuple[list[str], str]] = [
        (["uber", "ola", "bus", "train", "flight", "airbnb", "hotel", "taxi"], "Travel"),
        (["netflix", "spotify", "prime video", "cinema", "movie"], "Entertainment"),
        (["rent", "electricity", "water bill", "gas bill", "internet", "wifi"], "Bills"),
        (["pharmacy", "hospital", "clinic", "doctor", "medicine"], "Health"),
        (["salary", "payroll", "wage"], "Salary"),
        (["transfer", "neft", "rtgs", "imps", "upi"], "Transfer"),
        (["mutual fund", "stock", "share", "equity", "sip"], "Investment"),
        (["amazon", "flipkart", "myntra", "zara", "h&m"], "Shopping"),
        (["restaurant", "cafe", "starbucks", "kfc", "mcdonald", "swiggy", "zomato"], "Food"),
    ]

    for keywords, label in rules:
        if any(word in text for word in keywords):
            return label, 0.75

    return "Other", 0.5


# Try to load the zero-shot model once.
# If it fails (e.g. PyTorch not installed), fall back to rule-based logic.
try:
    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
    )
except Exception:
    classifier = None


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

            if classifier is not None:
                result = classifier(description, CATEGORIES)
                best_label = result["labels"][0]
                best_score = float(result["scores"][0])
            else:
                best_label, best_score = _rule_based_category(description)

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
