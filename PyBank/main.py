import os
import csv

budget_csv = os.path.join("PyBank/Resources/budget_data.csv")

with open(budget_csv, newline = "") as csvfile:
    budgetreader=csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(budgetreader)
    #print(csv_header)

    total_months = []
    net_total = []
    change = []
    
    for row in budgetreader:
        total_months.append(row[0])
        net_total.append(int(row[1]))
    for i in range(len(net_total)-1):
        change.append(net_total[i+1]-net_total[i])

print("FINANCIAL ANAYLSIS")
print("---------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Grand Total: ${sum(net_total)}")
print(f"Average Change: ${round(sum(change)/len(change), 2)}")
#------------------------------------------------------------------------
# < & > profits

greatestincrease = max(change)
greatestdecrease = min(change)
print(f"Greatest Increase in Profits: (${greatestincrease})")
print(f"Greatest Decrease in Profits: (${greatestdecrease})")
