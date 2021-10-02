# 3.2.10
# while loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

# for loop
# see python practice main
counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)   

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)    
#same as above but uses range()
for num in range(5):
    print(num)
#iterate through
for i in range(len(counties)):
    print(counties[i])

# iterate throught dictionaries
# having trouble
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# get keys in a dictionary
for county in counties_dict.keys():
    print(county)
# skill drill
# get values in a dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
# get key, value in dictionary template
# for key, value in dictionary_name.items():
    # print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)
# skill drill 3.2.10
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")
# iterate through a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
## use the range function to iterate over the list
for i in range(len(voting_data)):
    print(voting_data[i])
# get the values from a list of dictionaries
## need a nested loop
### retrieve each dictionary in the first loop
### use values() on county_dict to reference data in second forloop to get each value.
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# Module question, retrieve the number of voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
# if we want counties
for county_dict in voting_data:
    print(county_dict['county'])
# 3.2.11
# the print() function
print("Hello World")
print("Your interest for the year is $" + str(interest))     



#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total numer of votes each candidate won
#5. The winner of the election based on popular vote



# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

#print(winning_candidate_summary)

# Print the candidate vote dictionary.
#print(candidate_votes)

# Print the candidate list.
#print(candidate_options)

# Print the total votes.
#print(total_votes)




