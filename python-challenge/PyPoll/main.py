import os
import csv

csvpath = os.path.join('election_data.csv')
file_to_output = os.path.join("analysis", "election_analysis.txt")


#To read CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0

    
    candidates = []
    voter_count = []
    candidate_percentage = []
    winning_candidate = ""
    winning_count = 0

    for row in csvreader:
        total_votes=total_votes+1
        if candidates in candidates:
            candidates_index = candidates.index(candidates)
            voter_count[candidates_index] = voter_count[candidates_index] + 1
            # Else create new spot in list for candidate
        else:
            candidates.append(candidates)
            voter_count.append(1)

    max_votes = voter_count[0]
    max_index = 0

        # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        candidate_percentage = voter_count[count]/total_votes*100

        if voter_count[count] > max_votes:
            max_votes = voter_count[count]
            max_index = count
            winning_candidate = candidates[max_index]

    # Round decimal


    # Print results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    
    print("---------------------------")
    print(f"Winner: {winning_candidate}")
    print("---------------------------")

    