# Modules:
import os
import csv

# Set path to the financial data budget_data.csv
csvpath = os.path.join("Resources", "budget_data.csv") # Setting a path to the file.
total_number_months = 0 # Initializing total number of months count.
profit_or_losses = 0.0 # Initializing total amount of Profit/Losses.

# Setup variables for the average total change:
prev_row = None #prev_row is None because we are not in the loop yet.
total_change = 0.0 # Initializing the total change.

# Setup variables for the greatest increase and decrease:
great_incr = 0 
great_dcr = 0
great_inc_date = 0
great_dcr_date=0

# Open the CSV:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # Skip the headers

    # Loop through the dataset :
    for row in csvreader:
        total_number_months = total_number_months + 1 #looking for the months.
        profit_or_losses = profit_or_losses+float(row[1]) #looking for net total amount of profit or losses.
        if prev_row: 
            change = float(row[1]) - float(prev_row[1]) #calculating the change in each row.
            total_change = total_change + change # here, we will obtain total change by adding to the initial value (0), the difference between the rows.
            if change > great_incr: 
                great_incr = change
                great_inc_date = row[0]
            if change < great_dcr:
                great_dcr = change
                great_dcr_date=row[0]

        prev_row=row
   
# Display the net total:
result_str = f"""
    Financial Analysis:
    ----------------------------------------
    Total Number of Months: {total_number_months}
    Total Profit/Losses: {profit_or_losses}
    Total Average Change: {total_change/(total_number_months-1)}
    The Greatest Increase in Profits: {great_inc_date}, {great_incr}
    The Greatest Decrease in Losses: {great_dcr_date}, {great_dcr}

"""
print(result_str)
output_file = os.path.join(".","Analysis", "AnalysisResults.txt") 
with open(output_file, "w") as text_file:
    text_file.write(result_str)

