import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv') #file path to find files
#set variables for later use
totalmonths = 0 
total = 0
maxvalue = 0
minvalue = 0
pincome = None
incomechangelist = []
with open(csvpath) as csvfile: #reads csv file

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first and skips to next row 
    next(csvreader)
    #Read each row of data after the header
    for row in csvreader:
        totalmonths = totalmonths + 1 #stores the count of total months
        total = int(row[1]) + total #stores sum of all the income over the entire csvfile
        value = int(row[1])
        date = str(row[0])
        if pincome is not None:
            change = value-pincome
            incomechangelist.append(change)
            #finds the max and min value as it iterates through the csvreader and stores them along with the corresponding date for later use
            if change > maxvalue:
                maxvalue = change
                maxdate = date
            if change < minvalue:
                minvalue = change
                mindate = date
        pincome = value #stores the value as previous columns income to calculate change through the next iteration

    totalchange = sum(incomechangelist)
    numofchange = len(incomechangelist)
    incomechangeavg = round(totalchange / numofchange, 2) #finds average change from date to date over the entire dataset
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${total}")
    print(f"Average Change: $ {incomechangeavg}")      
    print(f"Greatest Increase in Profits: {maxdate} (${maxvalue})")      
    print(f"Greatest Decrease in Profits: {mindate} (${minvalue})")      

# the code below transcribes the terminal output into a txt file
output_path = os.path.join("Analysis", "PyBank_Results.txt")
#.write is the method used to actually write in the txt file once its been created and named
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: $ {incomechangeavg}\n")  
    txtfile.write(f"Greatest Increase in Profits: {maxdate} (${maxvalue})\n")
    txtfile.write(f"Greatest Decrease in Profits: {mindate} (${minvalue})\n") 