def check_balance_continuity(transactions):
    for i in range(1, len(transactions)):
        prev = transactions[i - 1]
        curr = transactions[i]

        expected = prev["balance"]

        if curr.get("credit") is not None:
            expected += curr["credit"]

        if curr.get("debit") is not None:
            expected -= curr["debit"]

        if round(expected, 2) != round(curr["balance"], 2):
            return {
                "status": False,
                "error_at": curr["date"],
                "expected": expected,
                "actual": curr["balance"],
            }

    return {"status": True}


