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
    sum_rental = Decimal("0.0")

    for row in reader:
        amount = Decimal(row[NET_PROFIT])

        if amount >= Decimal("0.0"):
            sum_profits += amount
        elif row[ITEM] == "PLANE_RENTAL":
            sum_rental += amount
        else:
            sum_expenses += amount


    print(f"Sum profits: {2 * sum_profits:,.2f} per month  (post- flight expenses, pre-rental)")
    print(f"Sum rental: {sum_rental:,.2f} = per month ")
    print(f"Sum profits: {2 * sum_profits + sum_rental:,.2f} per month (post- flight expenses, post-rental)")
    print(f"Sum expenses: {sum_expenses:,.2f} per month")