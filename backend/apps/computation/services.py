from .calculators.totals import calculate_total_credit, calculate_total_debit
from .calculators.monthly import group_by_month
from .calculators.cashflow import calculate_net_cashflow


def compute_all(transactions):
    total_credit = calculate_total_credit(transactions)
    total_debit = calculate_total_debit(transactions)

    monthly = group_by_month(transactions)
    monthly_cashflow = calculate_net_cashflow(monthly)

   
    monthly_summary = {}
    for month, values in monthly.items():
        monthly_summary[month] = {
            "credit": round(values["credit"], 2),
            "debit": round(values["debit"], 2),
            "net": round(values["credit"] - values["debit"], 2),
        }

    return {
        "totals": {
            "credit": total_credit,
            "debit": total_debit,
        },
        "net_cash_flow": round(total_credit - total_debit, 2),
        "monthly_summary": monthly_summary,
    }
