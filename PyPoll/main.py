import os
import csv

filetoload=os.path.join("Resources","election_data.csv")

totalvotes=0
candidates={}
percentwon=[]
totalvoteswon=[]
 


with open(filetoload) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    for c1,c2,c3 in csvreader:
        totalvotes += 1
        if c3 in candidates:
            candidates[c3] += 1
        else:
            candidates[c3] = 1

print("\ncleElection Results")
print("-------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------")
winner= list(candidates.keys())[0]
for name, votes in candidates.items() :
    if votes> candidates[winner]:
        winner=name
    print(f"{name}: {votes/totalvotes:.3%} ({votes})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

with open('./analysis/pypollresults.txt','w') as f:
    print("Election Results",file=f)
    print("-------------------",file=f)
    print(f"Total Votes: {totalvotes}",file=f)
    print("-------------------",file=f)
    winner= list(candidates.keys())[0]
    for name, votes in candidates.items() :
        if votes> candidates[winner]:
            winner=name
        print(f"{name}: {votes/totalvotes:.3%} ({votes})",file=f)
    print("-------------------",file=f)
    print(f"Winner: {winner}",file=f)
    print("-------------------",file=f)