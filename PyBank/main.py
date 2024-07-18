# create a Python script that analyzes the records to calculate each of the following values:
import os
import csv

total_months = 0
net_total = 0
previous_profit_losses = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Join directory
budget_data = os.path.join(r'C:\Users\abiga\OneDrive\Desktop\python-challenge\PyBank\Resources\budget_data.csv')

# Open and read CSV
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Compute each row
    for row in csvreader:
        date = row[0]
        profit_losses = int(row[1])

        # Calculate the total number of months and net total amount
        total_months += 1
        net_total += profit_losses

        if previous_profit_losses is not None:
            # Calculate changes
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)

            # Find greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

            # Find the greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        # Save the current profit/losses for the next iteration
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write the analysis to a text file
output_file = r'C:\Users\abiga\OneDrive\Desktop\python-challenge\PyBank\analysis\PyBank.txt'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")


				   







          
          





