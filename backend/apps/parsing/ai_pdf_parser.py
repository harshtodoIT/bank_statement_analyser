import os
import json
import requests


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def extract_transactions_with_ai(text: str):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not configured.")

    prompt = f"""
Extract bank transactions from the text below.

Return ONLY valid JSON array.

Each object must contain:
- date (DD-MM-YYYY)
- description
- debit (string, empty if none)
- credit (string, empty if none)
- balance (number)

Rules:
- If debit missing return empty string
- If credit missing return empty string
- Ignore headers and footers
- Ignore non-transaction lines
- Do not include explanation text
- Do not wrap response in markdown

Text:
{text}
"""

    response = requests.post(
        GROQ_URL,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0,
        },
        timeout=60,
    )

    if response.status_code != 200:
        raise ValueError(f"Groq API error: {response.text}")

    data = response.json()
    content = data["choices"][0]["message"]["content"].strip()

    # Remove markdown fences if present
    if content.startswith("```"):
        parts = content.split("```")
        if len(parts) >= 2:
            content = parts[1]
        content = content.replace("json", "").strip()

    try:
        transactions = json.loads(content)
    except Exception:
        raise ValueError(f"AI returned invalid JSON: {content}")

    if not isinstance(transactions, list):
        raise ValueError("AI response is not a JSON array.")

    normalized_rows = []

    for index, txn in enumerate(transactions, start=1):
        txn_lower = {k.lower(): v for k, v in txn.items()}

        date = str(txn_lower.get("date", "")).strip()
        description = str(txn_lower.get("description", "")).strip()
        debit = str(txn_lower.get("debit", "")).strip()
        credit = str(txn_lower.get("credit", "")).strip()
        balance = str(txn_lower.get("balance", "")).replace(",", "").strip()

        # Must have date and balance
        if not date or not balance:
            continue

        # Must have exactly one of debit or credit
        if not debit and not credit:
            continue

        normalized_rows.append({
            "row_index": index,
            "raw": [
                date,
                description,
                debit,
                credit,
                balance,
            ]
        })

    if not normalized_rows:
        raise ValueError("AI did not return valid transaction data.")

    # 🔥 Deterministic Balance Recalculation
    corrected_rows = []
    previous_balance = None

    for row in normalized_rows:
        date, desc, debit, credit, balance = row["raw"]

        debit_val = float(debit) if debit else 0.0
        credit_val = float(credit) if credit else 0.0
        balance_val = float(balance)

        if previous_balance is None:
            # First row → trust its balance
            previous_balance = balance_val
        else:
            # Recalculate balance deterministically
            expected_balance = previous_balance - debit_val + credit_val
            balance_val = round(expected_balance, 2)
            previous_balance = balance_val

        row["raw"][4] = str(balance_val)
        corrected_rows.append(row)

    return corrected_rows
