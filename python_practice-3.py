counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# membership and logical operators practice
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# 3.4.1 Python Dependencies, Modules, and Packages
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# to reduce confusion on importing a module with the same name as a class...
#...we can use an abbreviated alias dt for the datetime module
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# the csv module
import csv
# to see all the functions available in the csv module
dir(csv)
# can also be used on a variable like a dictionary
dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})
# another example with string
dir(str)
# skill drill
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)
# modules that may be useful later but need importing
# random
# numpy
# might already have with installation package

# 3.4.2
import csv
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: perform analysis.
print(election_data)

## alternate for indirect path
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# 3.4.3 write to files with python
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# add "Hello World" to the first line of election_analysis.txt
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# make the code cleaner and more concise
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
txt_file.write("Arapahoe")
txt_file.write("Denver")
txt_file.write("Jefferson")

skill drill
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write three counties to the file.
txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



# 3.5.1
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
    # Read and print the header row.
    #headers = next(file_reader)
    #print(headers)
