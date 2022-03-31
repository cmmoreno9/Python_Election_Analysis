# The data we need to retreive. 
# Add our dependencies.
# 1. The toal number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won 
# 4. The total number of votes each candidate won
# 5. The winner of the elction based on popular vote. 
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total votes and set it to 0
total_votes = 0 
#declare candidate_option list
candidate_options =[]
#create dictionary for candidate name and votes
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data :
#Read the file object with reader function. 
    file_reader = csv.reader(election_data) 
    #read the header row. 
    headers= next(file_reader)

    #print each row in the CSV file. 
    for row in file_reader: 
        #add increment total votes by 1 after for loop
        total_votes += 1 

        #print the candidate name from each row
        candidate_name =row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #3. Add a vote to candidate coutn in each row
        candidate_votes[candidate_name] += 1

    #print the candidate list
        print(candidate_votes)

#determine the percentage of votes for each candidate
#1 iterate through the candidate list
    for candidate_name in candidate_votes:
        #2 retrieve vote count of a candidate. 
        votes= candidate_votes[candidate_name] 
        #3 calcuate the percentage of votes
        vote_percentage = float(votes)/ float(total_votes)*100
        #4 print the candidate name and percentage of votes using f string in terminal
        

#winning candidate and winning count tracker
winning_canidate = "" 
winning_count = 0 
winning_percentage= 0 
#1 determine if the votes are greater than the winning count. 
if (votes> winning_count) and (vote_percentage > winning_percentage):
    #2 set winning count = votes and winning percentage = vote percentage 
    winning_count=votes
    winning_percentage = vote_percentage
    #3 set winning count = to candidate name 
    winning_candidate= candidate_name 

# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



