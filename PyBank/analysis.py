import os
import csv
# Path to collect data from the Resources folder
graduation_csv = os.path.join('..', 'Resources', 'budget_data.csv')
#path to save
file_to_save = os.path.join('budget_analysis.txt')

# List to store data
months = []
profit_loss_changes = []
count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

with open(graduation_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header =next(csv_reader)

    for row in csv_reader:
        count_months += 1
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        
        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            previous_month_profit_loss = current_month_profit_loss
    
    # Calculate Changes
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss / (count_months - 1), 2)
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    greatest_increase_index = profit_loss_changes.index(greatest_increase)
    greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
    best_month = months[greatest_increase_index]
    worst_month = months[greatest_decrease_index]

    #print
    with open(file_to_save, "w") as txt_file:
        bank_analysis = (
            f"\nFinacial Analysis\n"
            f"------------------------------\n"
            f"Total Months: {count_months}\n"
            f"Total: ${net_profit_loss}\n"
            f"Average Change: ${average_profit_loss}\n"
            f"Greatest Increase in Profits: {best_month} ${greatest_increase}\n"
            f"Greatest Decrease in Profits: {worst_month} ${greatest_decrease}\n")
        print(bank_analysis)
        txt_file.write(bank_analysis)

