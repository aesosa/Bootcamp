#PyBank challenge: create a python script that
#analyzes records to calculate the following:
#total number of months included in dataset
#net total of profit/losses over entire period
#greatest increase in profit(Data and amount) over  period
#greatest decrease in profit(data and amount) over period
import csv
import os
budget_data = "Resources/budget_data.csv"
analysis_data = "Analysis/PyBankAnalysis.txt"
# print("Financial Analysis")
# print("------------------------------------------")
# # print("Total Months: ", blank)
totalmonths = 0
# print("Total: ", Total)
# print("Average Change: ", blank)
previousrevenue = 0
monthofchange = []
revenue_change = []
# print("Greatest Increase in Profits: ", blank)
greatestincrease = ["", 0]
# print("Greatest Decrease in Profits: ", blank)
greatestdecrease = ["", 0]
# print("------------------------------------------")
totalrevenue = 0

with open(budget_data) as pybank:
    Dictreader = csv.DictReader(pybank)
    for row in Dictreader:
        #tracking the totalmonths
        totalmonths += 1
        totalrevenue = totalrevenue + int(row["Profit/Losses"])

        revenue_change = int(row["Profit/Losses"]) - previousrevenue
        previousrevenue = int(row["Profit/Losses"])
        revenue_change = revenue_change + [revenue_change]
        monthofchange = monthofchange + [row["Date"]]

        if (revenue_change < greatestdecrease[1]):
            greatestdecrease[0] = row["Date"]
            greatestdecrease[1] = revenue_change
        if (revenue_change > greatest_increase[1]):
            greatestincrease[0] = row["Date"]
            greatestincrease[1] = revenue_change

revenue = sum(revenue_change) / len(revenue_changes)

output = (
    f"\nFinancial Analsysis\n"
    f"--------------\n"
    f"\Total Months: {totalmonths}\n"
    f"Total Revenue: ${totalrevenue}\n"
    f"Average Revenue Change: ${revenue }\n"
    f"Greatest Increase in Revenue: {greatestincrease[0]} (${greatestincrease[1]})\n"
    f"Greatest Decrease in Revenue: {greatestdecrease[0]} (${greatestdecrease[1]})\n"
            )
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
