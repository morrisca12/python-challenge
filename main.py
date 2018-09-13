import os
import csv

csvpath = os.path.join('budget_data.csv')
#To read CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #variables
    date = []
    revenue = []
    avg_revenue = []
    rev_increase = 0
    rev_decrease = 0
    rev_increase_date = ""
    rev_decrease_date = ""
    #To find months and revenue total
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))
    #To calculate avg change, min and max
    for i in range(1,len(revenue)):
        revenue.append((revenue[i]) - (revenue[i-1]))   
        #calculate the average rev change per month
        avg_revenue = round((sum(revenue)/len(revenue)), 2)

        rev_increase = max(revenue)
        rev_decrease = min(revenue)
    #to find date for rev increase and decrease
    for j in range(0,len(date)):
        if j == rev_increase:
            rev_increase_date.append(row[0])
        if j == rev_decrease:
            rev_decrease_date.append(row[0])
#to print the totals
print("Financial Analysis")
print("-------------------")
print("Total Months:", len(date))
print("Total Revenue $:", sum(revenue))
print("Average Revenue $:", round(avg_revenue))
print("Greatest Increase in Profits:", str(rev_increase_date), "$:", rev_increase)
print("Greatest Decrease in Profits:", str(rev_decrease_date), "$:", rev_decrease)
#to creat text file
f = open("Output_analysis.txt" , "w")
f.write("Financial Analysis"+ "\n")
f.write("----------------------------"+ "\n")
f.write("Total Months: " + str(date) + "\n")
f.write("Total Revenue: $" + str(revenue)+ "\n")
f.write("Average Revenue: $" + str(avg_revenue)+ "\n")
f.write("Greatest Increase in Revenue: " + rev_increase_date + " ($" + str(rev_increase) + ")" + "\n")
f.write("Greatest Decrease in Revenue: " + rev_decrease_date + " ($" + str(rev_decrease) + ")" + "\n")
f.close()

