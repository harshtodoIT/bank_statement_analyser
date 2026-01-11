from .patterns import BANK_PATTERNS


def detect_bank_from_text(text: str) -> str:
    """
    Detect bank name from given text.
    Returns bank name or raises ValueError on failure.
    """

    text = text.lower()
    matches = []

    for bank, patterns in BANK_PATTERNS.items():
        for pattern in patterns:
            if pattern in text:
                matches.append(bank)
                break

    if len(matches) == 1:
        return matches[0]

    if len(matches) > 1:
        raise ValueError("Ambiguous bank detection.")

    raise ValueError("Unsupported or unknown bank statement.")
