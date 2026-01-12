import re


def _validate_label(label):
    if label is None:
        return "Label is required."

    label = label.strip()

    if len(label) < 3 or len(label) > 100:
        return "Label must be between 3 and 100 characters."

    # Reject labels with only numbers or symbols
    if not re.search(r"[A-Za-z]", label):
        return "Label must contain at least one alphabet character."

    return None


def _validate_amount(amount):
    if amount is None:
        return "Amount is required."

    if not isinstance(amount, (int, float)):
        return "Amount must be a valid number."

    if amount == 0:
        return "Amount cannot be zero."

    if abs(amount) > 10_000_000:
        return "Amount exceeds the maximum allowed limit."

    return None


def _validate_note(note):
    if note is None:
        return None

    note = str(note)

    if len(note) > 255:
        return "Note must not exceed 255 characters."

  
    if re.search(r"<.*?>", note):
        return "Note contains invalid characters."

    return None


def apply_manual_adjustments(computed_data, adjustments):
    """
    Applies validated manual adjustments on top of deterministic computation output.
    """

    validated_adjustments = []
    total_manual_amount = 0.0

    for adj in adjustments:
        label_error = _validate_label(adj.get("label"))
        if label_error:
            return {"success": False, "error": label_error}

        amount_error = _validate_amount(adj.get("amount"))
        if amount_error:
            return {"success": False, "error": amount_error}

        note_error = _validate_note(adj.get("note"))
        if note_error:
            return {"success": False, "error": note_error}

        adj["is_manual"] = True
        validated_adjustments.append(adj)
        total_manual_amount += adj["amount"]

    computed_data["manual_adjustments"] = validated_adjustments
    computed_data["manual_adjustment_total"] = round(total_manual_amount, 2)

    computed_data["net_cashflow_with_manual"] = (
        computed_data.get("total_credit", 0)
        - computed_data.get("total_debit", 0)
        + total_manual_amount
    )

    return {
        "success": True,
        "data": computed_data
    }
