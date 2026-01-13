import re


def validate_label(label):
    if label is None:
        return "Label is required."

    label = str(label).strip()

    if len(label) < 3 or len(label) > 100:
        return "Label must be between 3 and 100 characters."

    if not re.search(r"[A-Za-z]", label):
        return "Label must contain at least one alphabet character."

    return None


def validate_amount(amount):
    if amount is None:
        return "Amount is required."

    if not isinstance(amount, (int, float)):
        return "Amount must be a valid number."

    if amount == 0:
        return "Amount cannot be zero."

    if abs(amount) > 10_000_000:
        return "Amount exceeds the maximum allowed limit."

    return None


def validate_note(note):
    if note is None:
        return None

    note = str(note)

    if len(note) > 255:
        return "Note must not exceed 255 characters."

    if re.search(r"<.*?>", note):
        return "Note contains invalid characters."

    return None
