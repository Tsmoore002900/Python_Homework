import os
import csv
# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# List to store data
Date = []
Profit_Losses = []
with open(graduation_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header =next(csv_reader)
    #print(csv_reader)
    #print(f"CSV Header: {csv_header}")
    for row in csv_reader:
        Date.append(str(row[0]))
        Profit_Losses.append(int(row[1]))
        # Total Months Calculation
        Total_Months = len(Profit_Losses)
        # Total Calculation
        Total = sum(Profit_Losses)
        #Average Change Calculation
        Average_Change = round((Total / Total_Months), 2)
        #Greatest Increase in Profits Calculation
        Increase = max(Profit_Losses)
        #Greatest Decrease in Profits Calculation
        Decrease = max(Profit_Losses)
        
    #Insert Finacial Analysis as text
    print("Financial Analysis")
    print("-----------------------------------")    
    print(f"Total Months: {str(Total_Months)}")
    print(f"Total: {str(Total)}")
    print(f"Average Change: {str(Average_Change)}")
    print(f"Greatest Increase in Profits: {str(Increase)}")
    print(f"Greatest Decrease in Profits: {str(Decrease)}")

