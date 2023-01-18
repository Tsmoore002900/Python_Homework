import os
import csv
# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'budget_data.csv')
#path to make txt.file
file_to_save = os.path.join('..', 'analysis', 'budget_analysis.txt')

# List to store data
months = []
monthly_changes = []
count_months = 0
net_profit_loss = 0
prvious_month = 0
current_month = 0
profit_loss_change = 0

#open data and set header
with open(graduation_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header =next(csv_reader)

    # collect and calculate data
    for row in csv_reader:
        count_months += 1
        current_month = int(row[1])
        net_profit_loss += current_month
        
        if (count_months == 1):
            prvious_month = current_month
            continue
        else:
            profit_loss_change = current_month - prvious_month
            months.append(row[0])
            monthly_changes.append(profit_loss_change)
            prvious_month = current_month
    
    # Calculate Changes
    sum_profit_loss = sum(monthly_changes)
    average_change = round(sum_profit_loss / (count_months - 1), 2)
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    greatest_increase_index = monthly_changes.index(greatest_increase)
    greatest_decrease_index = monthly_changes.index(greatest_decrease)
    best_month = months[greatest_increase_index]
    worst_month = months[greatest_decrease_index]

    #print
    with open(file_to_save, "w") as txt_file:
        bank_analysis = (
            f"\nFinacial Analysis\n"
            f"------------------------------\n"
            f"Total Months: {count_months}\n"
            f"Total: ${net_profit_loss}\n"
            f"Average Change: ${average_change}\n"
            f"Greatest Increase in Profits: {best_month} ${greatest_increase}\n"
            f"Greatest Decrease in Profits: {worst_month} ${greatest_decrease}\n")
        print(bank_analysis)
        
        #wirte
        txt_file.write(bank_analysis)

