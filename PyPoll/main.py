import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') #file path to find files
#set variables for later use
candidateandvotes = {}
winner = 0 
winnername = ""
with open(csvpath) as csvfile:  #reads csv file
    csvreader = csv.reader(csvfile, delimiter=',') #CSV reader specifies delimiter and variable that holds contents
    next(csvreader) #Read the header row first and skips to next row 

    for row in csvreader: #Read each row of data after the header
        candidate = str(row[2]) #makes the 3 column (index[2]) = to candidate for later use

        if candidate in candidateandvotes: #iterates through the empty dictionary created above
            candidateandvotes[candidate] += 1 #if the candidate(key) has appeared in the dict it adds 1 to the votes(value) of each candidate  
        else:
            candidateandvotes[candidate] = 1 #adds the candidate to the dict if they havent appeared yet as a key 

totalvotes = sum(candidateandvotes.values()) #adds all the candidates votes (values) together 
#makes a new dict with the same key(candidate) as the first dict only this time the value will be = to the percentage of votes
canpercentages = {candidate: (votes / totalvotes * 100) for candidate, votes in candidateandvotes.items()} 
for key in candidateandvotes:
    if candidateandvotes[key] > winner:  #references the candidate but checks the value to see if it is greater than the winner
        winner = candidateandvotes[key]  #sets a counter to check each candidates values(votes)
        winnername = key #makes the winner name the key(candidate) for later use

print("Election Results")
print("----------------------------------")
print(f"Total Votes: {totalvotes}")
print("----------------------------------")
for candidate, votes in candidateandvotes.items(): #iterates through the dictionary checking the key and value at the same time 
    print(f"{candidate}: {canpercentages[candidate]: .3f}% ({votes})") #prints each key(candidate), votesperct(value from second dictionary), value (votes)
print("----------------------------------")
print(f"Winner: {winnername}") #displays the winner from the for loop in line 24
print("----------------------------------")
# the code below transcribes the terminal output into a txt file
output_path = os.path.join("Analysis", "PyPoll_Results.txt")
#.write is the method used to actually write in the txt file once its been created and named
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write("----------------------------------\n")
    for candidate, votes in candidateandvotes.items():
        txtfile.write(f"{candidate}: {canpercentages[candidate]: .3f}% ({votes})\n")
    txtfile.write("----------------------------------\n")
    txtfile.write(f"Winner: {winnername}\n")
    txtfile.write("----------------------------------\n")
