# Modules 
import os
import csv

# Set path to the financial data budget_data.csv
csvpath = os.path.join(".","Resources", "election_data.csv") 

# Setup variables
candidates={} # Initializing candidates as a dictionary so we can use key and value to capture the data.
total_num_votes = 0 # Initializng the variable to be able to count the rows.

def calc_perc(val,total): #Defining a function to calculate the percentage of the total votes
    return f"{round(val/total*100, 3)} %"

with open(csvpath) as csvfile: # Open the CSV file
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) #skipping the header

    # Loop through the dataset looking for the total number of votes :
    for row in csvreader:
        candidates[row[2]] = candidates.get(row[2],0) + 1 #Using .get method to return the value of the item with the speciffied key. 
        total_num_votes = total_num_votes+1

winner=["No Name",0] #setting up a winner variable to track who got the most votes.
all_candidates="" #setting up a variable for all candidates as a string.

for name, votes in candidates.items(): #iterating using .items method to find the winner.
    all_candidates +=f"{name} : {calc_perc(votes,total_num_votes)} ({votes})\n"
    if votes > winner[1]: #using if statement to check if current item has more votes than previous item with most votes
        winner=[name, votes] #then spit out the winner name and the amount of votes.

# Printing results
election_results = f""" 
Election Results
------------------------------------
Total Votes: {total_num_votes}
-----------------------------------
{all_candidates}-----------------------------------
Winner: {winner[0]} is the WINNER!
-----------------------------------
"""
print(election_results) #display election results
textfile_path = os.path.join(".","Analysis", "elections_results.txt")  #path to a folder where it will be saved
with open(textfile_path, "w") as text_file:
    text_file.write(election_results) 