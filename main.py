import os
import csv

csvpath = os.path.join('election_data.csv')
#To read CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    voter_id = []
    candiates = []
    voter_count = 0

    for row in csvreader:
        voter_id.append(row[0])
        candiates.append(row[2])

total_votes = len(voter_id)
candiates = list(set(candiates))

for i in range (len(candidates)):
    if i == candiates
        count += 1
    voter_count.append(count)
    count = 0

