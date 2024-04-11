import csv
from decimal import Decimal

# Ledger filename
LEDGER = "reports/ledger.csv"
# LEDGER = "./reports/archive/ledger-opportunistic-aggregation.csv"

# CSV Fields (item,net profit,time,location)
ITEM = 0
NET_PROFIT = 1
TIME = 2
LOCATION = 3

with open(LEDGER, "r") as ledger_data:
    reader = csv.reader(ledger_data, delimiter=",")
    header = next(reader)

    sum_profits = Decimal("0.0")
    sum_expenses = Decimal("0.0")

    for row in reader:
        amount = Decimal(row[NET_PROFIT])

        if amount >= Decimal("0.0"):
            sum_profits += amount
        else:
            sum_expenses += amount


    print(f"Sum profits: {sum_profits:,.2f} (post-expenses)")
    print(f"Sum expenses: {sum_expenses:,.2f}")