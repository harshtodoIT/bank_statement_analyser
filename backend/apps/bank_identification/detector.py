from .patterns import BANK_PATTERNS
from .extractor import extract_first_part


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


def detect_bank_from_file(file_path: str) -> str:
    """
    Detect bank name directly from file path.
    """
    text = extract_first_part(file_path)
    return detect_bank_from_text(text)