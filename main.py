import os
import csv

csvpath = os.path.join('election_data.csv')
#To read CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    voter_id = []
    canidates = []
    voter_count = 0

    for row in csvreader:
        voter_id.append(row[0])
        canidates.append(row[2])

total_votes = len(voter_id)
canidates = list(set(canidates))

for i in range (len(canidates)):
    if i == canidates
        count += 1
    voter_count.append(count)
    count = 0

