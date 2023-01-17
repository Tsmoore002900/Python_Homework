#add dependencies
import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('..', 'Resources', 'election_data.csv')
# path to save
file_to_save = os.path.join('..', 'analysis','election_analysis.txt')

#List to store Data
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open and read the file. 
with open(election_data) as election_data:
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name) 
            candidate_votes[candidate_name] = 0 
        candidate_votes[candidate_name] += 1

#Save the results to text file. 
with open(file_to_save, "w") as txt_file: 
    election_data = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_data, end="")
    txt_file.write(election_data)

    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
     

        #Determine winning vote count & candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    