from apps.manual_adjustments.models import ManualAdjustment


def generate_report(result):
    """
    result: ProcessingResult instance
    """

    adjustments_qs = ManualAdjustment.objects.filter(result=result)

    manual_adjustments = []
    manual_total = 0.0

    for adj in adjustments_qs:
        amount = float(adj.amount)
        manual_total += amount

        manual_adjustments.append({
            "label": adj.label,
            "amount": amount,
            "note": adj.note,
        })

    yearly_summary = {
        "total_credit": result.totals.get("credit", 0),
        "total_debit": result.totals.get("debit", 0),
        "net_cash_flow": result.net_cash_flow,
    }

    final_net_cash_flow = round(result.net_cash_flow + manual_total, 2)

    return {
        "totals": result.totals,
        "monthly_summary": result.monthly_summary,
        "yearly_summary": yearly_summary,
        "manual_adjustments": manual_adjustments,
        "manual_adjustments_total": round(manual_total, 2),
        "final_net_cash_flow": final_net_cash_flow,
        "category_summary": result.categorized_summary or {},
    }