print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
counties
counties[0]
# alternate pull
print(counties[2])
print(counties[-1])
len(counties)
counties[0:2]
# counties.append() adds an item to the end of a list
counties.insert(2, "El Paso")
counties
counties.remove("El Paso")
counties
counties[2] = "El Paso"
counties

# quiz in module
counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1, "El Paso")
counties.remove("Arapahoe")
counties
counties.remove("Denver")
counties.append("Denver")
counties.append("Arapahoe")
counties


counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_tuple[1]
counties_tuple[:2]


counties_dict = {}
# adds Arapahoe to the dict as the key and number of registered voters as the values
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict["Arapahoe"]

# 3.2.7
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# el paso was supposed to be added by inserting but I didnt know how?
voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data                  
arap = {"county":"Arapahoe", "registered_voters": 422829}
voting_data.remove(arap)
denv = {"county":"Denver", "registered_voters": 463353}
voting_data.remove(denv)
voting_data.append(denv)
voting_data.append(arap)
voting_data

# 3.2.8
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

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

# f strings
# edit code to calculate percentage of votes using f string literals

# original code from 3.2.8
# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

# edited using f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
## in line 162 inside the curly braces the f string calculates..... 
## ...my_votes / total_votes * 100 and formats the value as string so there is...
## ...no need to convert percentage_votes as in line 157

# using f strings with Dictionaries
# original code from 3.2.10 skill drill
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
# the edited code using f strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# multiline F strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Format Floating-Point Decimals
# in the code above we can change the formatting to add a thousands separator....
#...and specify a decimal precision
# general format: f'{value:{width}.{precision}}'
# below is the edited code with formatting
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

# skill drill
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
    #print(county, "county has", voters, "registered voters")
for county, voters in counties_dict.items():
    f"{county:,}, county has , {voters:,} registered voters")

# skill drill
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]


