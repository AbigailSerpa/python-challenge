import os
import csv
import csv

# File path to the CSV file
file_path = r'C:\Users\abiga\OneDrive\Desktop\python-challenge\election_data.csv'

# Initialize variables and data structures
total_votes = 0
candidates_votes = {}  # Dictionary to store candidate votes

# Open the CSV file and analyze votes
with open(file_path, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    header = next(csvreader)
    print("Header:", header)
    
    # Count total votes, track candidates and their votes
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        # Count votes for each candidate
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] += 1
        else:
            candidates_votes[candidate_name] = 1

# Calculate percentage of votes for each candidate
candidates_percentages = {}
for candidate, votes in candidates_votes.items():
    candidates_percentages[candidate] = (votes / total_votes) * 100

# Determine the winner based on popular vote
winner = max(candidates_votes, key=candidates_votes.get)

# Create a string with the results
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in candidates_votes.items():
    percentage = candidates_percentages[candidate]
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print results to console
print(results)

# Write results to a text file
output_file_path = r'C:\Users\abiga\OneDrive\Desktop\python-challenge\election_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(results)











