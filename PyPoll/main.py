import csv
import os
import sys

election_csv = os.path.join("PyPoll/Resources/election_data.csv")

with open(election_csv, newline="") as csvfile:
    electionreader=csv.reader(csvfile, delimiter = ",")

    csv_header = next(electionreader)
    #print(csv_header)

    votes = []
    candidates = []

    for row in electionreader:
        votes.append(row[0])
        candidates.append(row[2])
       

total_votes = (len(votes))
#print(total_votes)

#votes
khan_total = (int(candidates.count("Khan")))
khan = (khan_total/total_votes) * 100
khanrounded = round(khan, 3)

correy_total = (int(candidates.count("Correy")))
correy = (correy_total/total_votes) * 100
correyrounded = round(correy, 3)

li_total = (int(candidates.count("Li")))
li = (li_total/total_votes) * 100
lirounded = round(li, 3)

otooley_total = (int(candidates.count("O'Tooley")))
otooley = (otooley_total/total_votes) * 100
otooleyrounded = round(otooley, 3)


if khan_total > correy_total > li_total > otooley_total:
    winner = "Khan"
elif correy_total > khan_total > li_total > otooley_total:
    winner = "Correy"
elif li_total > khan_total > correy_total > otooley_total:
    winner = "Li"
elif otooley_total > khan_total > correy_total > li_total:
    winner = "O'Tooley"

#terminal
print("ELECTION RESULTS")
print("-------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------------")
print(f"Khan: {khanrounded}% ({khan_total})")
print(f"Correy: {correyrounded}% ({correy_total})")
print(f"Li: {lirounded}% ({li_total})")
print(f"O'Tooley: {otooleyrounded}% ({otooley_total})")
print("-------------------------------------------")
print(f"WINNER: {winner}!")

# .txt file
sys.stdout = open("PyPoll/Analysis/Result.txt", "w")
print("ELECTION RESULTS")
print("-------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------------")
print(f"Khan: {khanrounded}% ({khan_total})")
print(f"Correy: {correyrounded}% ({correy_total})")
print(f"Li: {lirounded}% ({li_total})")
print(f"O'Tooley: {otooleyrounded}% ({otooley_total})")
print("-------------------------------------------")
print(f"WINNER: {winner}!")

sys.stdout.close()
