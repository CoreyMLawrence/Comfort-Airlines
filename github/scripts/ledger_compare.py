# Ledger filenames
LEDGER_NO_AGGREATION_FILENAME = "reports/archive/ledger-no-aggregation.csv"
LEDGER_OPP_AGGREATION_FILENAME = "reports/archive/ledger-opportunistic-aggregation.csv"

# CSV Fields (item,net profit,time,location)
ITEM = 0
NET_PROFIT = 1
TIME = 2
LOCATION = 3

def sum_profits(rows) -> float:
    profit = 0
    
    for row in rows:
        amount = float(row[NET_PROFIT])
        if amount > 0:
            profit += amount 
        
    return profit

with open(LEDGER_NO_AGGREATION_FILENAME, "r") as ledger_no_aggregation_data, open(LEDGER_OPP_AGGREATION_FILENAME, "r") as ledger_opp_aggregation_data:
    profit_no_aggregation = sum_profits([row.strip().split(',') for row in ledger_no_aggregation_data][1:])
    profit_opp_aggregation = sum_profits([row.strip().split(',') for row in ledger_opp_aggregation_data][1:])
    
    print(f"[No aggregation] sum profits: {profit_no_aggregation}")
    print(f"[Opportunistic aggregation] sum profits: {profit_opp_aggregation}")
    print(f"\nDifference: {profit_opp_aggregation - profit_no_aggregation}")