import csv
import os
import pandas as pd

inputFile = os.path.join("election_data.csv")

outputFile = os.path.join("election_analysis.txt")
#variable
totalVotes = 0


with open(inputFile) as pollData:
    csvreader = csv.reader(pollData, delimiter = ",")

    #read the header
    header = next(csvreader)
    electionData_DF = pd.read_csv(inputFile)
    candidateVotes = electionData_DF["Candidate"].unique()
#variables
    candidate1= 0
    candidate2= 0 
    candidate3= 0

    for row in csvreader:
        totalVotes +=1

        if row[2] == candidateVotes[0]:
            candidate1 += 1
           
        elif row[2] == candidateVotes[1]:          
            candidate2 +=1                
        else:
            candidate3 +=1                    
        totalVotes= candidate1 + candidate2 + candidate3
        #candidate percentages
    candidate1pct = (candidate1/totalVotes) * 100
    candidate2pct = (candidate2/totalVotes) * 100
    candidate3pct = (candidate3/totalVotes) * 100
        
    completeVotes = [candidate1, candidate2, candidate3]
    mostVotes = max(completeVotes)
    index = completeVotes.index(mostVotes)
    winningCandidate= candidateVotes[index]

print(f"\n\nElection Rsults \n ---------------------\nTotal Votes: {totalVotes} \n ----------------")
print(f"{candidateVotes [0]}: {candidate1pct:.3f}% ({candidate1})")
print(f"{candidateVotes [1]}: {candidate2pct:.3f}% ({candidate2})")
print(f"{candidateVotes [2]}: {candidate3pct:.3f}% ({candidate3})")
print(f"-----------------------\nWinner: {winningCandidate}\n")



output = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"-----------------------------\n"
    f"{candidateVotes[0]}: {candidate1pct:.3f}% ({candidate1})\n"
    f"{candidateVotes[1]}: {candidate2pct:.3f}% ({candidate2})\n"
    f"{candidateVotes[2]}: {candidate3pct:.3f}% ({candidate3})\n"
    f"------------------------------\n"
    f"Winner: {winningCandidate}"
)


with open(outputFile, "w") as textFile:
    textFile.write(output)