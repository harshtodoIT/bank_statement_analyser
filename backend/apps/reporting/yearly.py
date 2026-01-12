def build_yearly_summary(transactions):
    total_credit = 0.0
    total_debit = 0.0

    for txn in transactions:
        if txn["credit"]:
            total_credit += float(txn["credit"])
        if txn["debit"]:
            total_debit += float(txn["debit"])

    return {
        "total_credit": total_credit,
        "total_debit": total_debit,
        "net_cashflow": total_credit - total_debit
    }
