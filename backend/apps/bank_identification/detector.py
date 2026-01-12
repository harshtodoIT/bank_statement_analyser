from .patterns import BANK_PATTERNS
from .extractor import extract_first_part
from pathlib import Path

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
    text = extract_first_part(file_path).lower()

    # 1️⃣ Try content-based detection
    bank = _detect_from_text(text)
    if bank:
        return bank

    # 2️⃣ Fallback to filename-based detection (CSV / Excel only)
    filename = Path(file_path).name.lower()
    bank = _detect_from_text(filename)
    if bank:
        return bank

    raise ValueError("Unsupported or unknown bank statement.")


def _detect_from_text(text: str):
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

    return None
