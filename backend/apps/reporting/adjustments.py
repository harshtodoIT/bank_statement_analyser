def apply_manual_adjustments(computed_data, adjustments):
    """
    computed_data: output from computation module
    adjustments: list of manual adjustment dicts
    """

    total_manual = 0.0

    for adj in adjustments:
        total_manual += adj.get("amount", 0.0)


    computed_data["manual_adjustments"] = adjustments
    computed_data["manual_adjustment_total"] = round(total_manual, 2)

    computed_data["net_cashflow_with_manual"] = (
        computed_data.get("total_credit", 0)
        - computed_data.get("total_debit", 0)
        + total_manual
    )

    return computed_data
