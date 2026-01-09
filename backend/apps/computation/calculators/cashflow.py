def calculate_net_cashflow(monthly_data):
    cashflow = {}

    for month, values in monthly_data.items():
        cashflow[month] = round(
            values["credit"] - values["debit"], 2
        )

    return cashflow
