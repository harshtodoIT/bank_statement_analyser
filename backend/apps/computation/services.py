from .calculators.totals import calculate_total_credit, calculate_total_debit
from .calculators.monthly import group_by_month
from .calculators.cashflow import calculate_net_cashflow
from .calculators.balance_check import check_balance_continuity


def compute_all(transactions):
    balance_status = check_balance_continuity(transactions)

    if not balance_status["status"]:
        return {"error": "Balance mismatch", "details": balance_status}

    total_credit = calculate_total_credit(transactions)
    total_debit = calculate_total_debit(transactions)
    monthly = group_by_month(transactions)
    cashflow = calculate_net_cashflow(monthly)

    return {
        "total_credit": total_credit,
        "total_debit": total_debit,
        "monthly_summary": monthly,
        "net_cashflow": cashflow,
    }
