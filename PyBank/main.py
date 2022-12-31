import os 
import csv
import sys

filetoload=os.path.join("Resources","budget_data.csv")
totalmonths=0
changesum=0
nettotal=[]
greatestincrease=0
greatestdecrease=0


with open(filetoload) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for date,value in csvreader:
        totalmonths=totalmonths+1
        nettotal.append(int(value))
        if totalmonths != 1:
            change = int(value) - lastvalue
            changesum = changesum + change
            if change > greatestincrease:
                greatestincrease = change
                increasedate= date
            if change < greatestdecrease:
                greatestdecrease= change
                decreasedate=date
        lastvalue = int(value)

    print("\nFinancial Analysis\n-------------------------")
    print("Total Months: %2d" % totalmonths)
    print("Total: $%2d"% sum(nettotal))
    print("Average Change: $%.2f"%float(changesum/(totalmonths-1)))
    print(f"Greatest Increase in Profits: {increasedate} ({greatestincrease})")
    print(f"Greatest decrease in Profits: {decreasedate} ({greatestdecrease})")

original_stdout= sys.stdout
with open('./analysis/pybankresults.txt','w') as f:
    sys.stdout= f
    print("Financial Analysis\n-------------------------")
    print("Total Months: %2d" % totalmonths)
    print("Total: $%2d"% sum(nettotal))
    print("Average Change: $%.2f"%float(changesum/(totalmonths-1)))
    print(f"Greatest Increase in Profits: {increasedate} ({greatestincrease})")
    print(f"Greatest decrease in Profits: {decreasedate} ({greatestdecrease})")
    sys.stdout= original_stdout
