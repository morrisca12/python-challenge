#import the os module, to allow creating file paths across operating systems
import os
#import module for reading csv files   
import csv

#import csv file
csvpath=os.path.join('budget_data.csv')

#open the csv file using the CSV module; csvreader here is a function
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #csvfile manipulates the object csv.reader to extract the lines
    print(csvreader)
    
    # skip the header row (first row) by using next
    next(csvreader) 

    #lists to store data in
    date = []
    cashflow = []
    cf_change = []

    # writing a For loop for each row in column1 (cashflow column) 
    for row in csvreader:
        #append the data to lists created above
        date.append(row[0])
        cashflow.append(float(row[1]))
        #print(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    #print length of date columns = number of months
    print("Total Months:", len(date))
    #print cumulative cashflow
    print("Total: $", sum(cashflow))


    #calculating the difference between subsequent rows in Cashdlow column 
    for i in range(1,len(cashflow)):
        cf_change.append((cashflow[i]) - (cashflow[i-1]))   
        #calculate the average of MoM changes
        avg_cf_change = round((sum(cf_change)/len(cf_change)),2)
        #calculate max of MoM cashflow changes
        max_cf_change = max(cf_change)
        #calculate min of MoM cashflow changes
        min_cf_change = min(cf_change)
        #calculate the max and min date and output as a string
        max_cf_change_date = str(date[cf_change.index(max(cf_change))])
        min_cf_change_date = str(date[cf_change.index(min(cf_change))])


    print("Average Change: $", (avg_cf_change))
    print("Greatest Increase in Profits:", max_cf_change_date,"($", max_cf_change,")")
    print("Greatest Decrease in Profits:", min_cf_change_date,"($", min_cf_change,")")
