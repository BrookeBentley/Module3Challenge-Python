import csv
import os

fileLoad = os.path.join("budget_data.csv")

#file for the output
outputFile = os.path.join("budgetAnalysis.txt")

# variable for total number of months
totalMonths = 0
totalProfitLoss = 0 # total profit/loss
changeProfitLoss = []
months = [] # list of months

with open(fileLoad) as budgetData:
   csvreader = csv.reader(budgetData)
   header = next(csvreader)
   firstRow = next(csvreader)
   totalMonths += 1
   
   totalProfitLoss += float(firstRow[1])

   previousProfitLoss = float(firstRow[1])

   for row in csvreader:
      totalMonths += 1


      #total profit/loss
      totalProfitLoss += float(row[1])

      #calculate net change
      netChange = float(row[1]) - previousProfitLoss
      changeProfitLoss.append(netChange)

      #add first month change occurred
      months.append(row[0])

      #update previous profit/loss
      previousProfitLoss = float(row[1])

#calculate average net change per month
averageChangePerMonth = sum(changeProfitLoss) / len(changeProfitLoss)

greatestIncrease = [months[0], changeProfitLoss[0]]
greatestDecrease =[months[0], changeProfitLoss[0]]

 #loop used to calculate the greatest monthly change
for m in range(len(changeProfitLoss)):
   #calculate greatest increase and decrease
    if (changeProfitLoss[m] > greatestIncrease[1]):
        greatestIncrease[1] = changeProfitLoss[m]
        greatestIncrease[0] = months[m]

    if (changeProfitLoss[m] < greatestDecrease[1]):
        greatestDecrease[1] = changeProfitLoss[m]
        greatestDecrease[0] = months[m]

output = (
   f"Budget Data Analysis \n"
   f"------------------------\n"
   f"Total Months = {totalMonths} \n"
   f"Total Profit/Losses = ${totalProfitLoss: ,.2f} \n"
   f"Average Change = ${averageChangePerMonth:,.2f}\n"
   f"Greatest Increase in Profits = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}\n"
   f"Greatest Decrease in Profits = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}\n"
   )
print(output)

#save output as text file
with open (outputFile, "w") as textFile:
    textFile.write(output)

