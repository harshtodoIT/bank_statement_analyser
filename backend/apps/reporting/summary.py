from .monthly import build_monthly_summary
from .category import build_category_summary
from .yearly import build_yearly_summary


def generate_report(transactions, manual_adjustments):
    """
    transactions: list of dicts from transactions table
    manual_adjustments: list of dicts from manual_adjustments table
    """

    monthly_summary = build_monthly_summary(transactions)
    category_summary = build_category_summary(transactions)
    yearly_summary = build_yearly_summary(transactions)

    manual_total = sum(
        float(adj["amount"]) for adj in manual_adjustments
    )

    final_net_cashflow = yearly_summary["net_cashflow"] + manual_total

    return {
        "monthly_summary": monthly_summary,
        "yearly_summary": yearly_summary,
        "category_summary": category_summary,
        "manual_adjustments_total": manual_total,
        "net_cashflow": final_net_cashflow
    }
