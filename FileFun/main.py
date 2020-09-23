import random 

# we want to open data.csv and load its contents
# into a 2D list of strings (eventually, we will convert column2's data to int)

def load_lines_from_file(filename):
    # filename is a string represnting the name of the file to open
    infile = open(filename, "r") # r is for reading (not writing)
    lines = infile.readlines() # lines is a 1D list of strings
    # where each string is a line from the file
    infile.close() 
    # 3 steps of 3-part file processing template
    # 1. open the file (line 6)
    # 2. process the file (line 7)
    # 3. close the file (line 9)
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_data_into_table(lines):
    data = []
    for line in lines:
        values = line.split(",") # values is a 1D list of strings
        data.append(values)
    return data

def print_table(data):
    for row in data:
        for value in row:
            print(value, end=" ")
        print()
def remove_whitespaces(data):
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            value = data[i][j]
            data[i][j] = value.strip()

def convert_column_to_numeric(data, column_index):
    for row in data:
        row[column_index] = int(row[column_index])

# NOTE: use "data.csv" if you open FileFun up in VS Code
# or use FileFun/data.csv if you open up U2-Python in VS Code
file_lines = load_lines_from_file("FileFun/data.csv") # this is a relative path
# and this only works if data.csv is in the same folder as this main.py
# and if you are in VS Code, VS Code is open to this folder
print(file_lines)

# first, let's remove the newlines
clean_lines(file_lines)
print(file_lines)

# now, we want to restructure our 1D list of strings
# into a 2D list of strings
# where each string is a value from the CSV file (comma-separated value)
data = restructure_data_into_table(file_lines)
print(data)

# print out data in a nice tabular format
print_table(data)

# we may have spaces in our values that we want to remove
# use the strip() method... 
remove_whitespaces(data)
print(data)

# we want to convert column2's data to int (numeric)
# lets remove the header from data
header = data.pop(0) # remove row 0
print(header)
print(data)

convert_column_to_numeric(data, 2)
print(data)
print(type(data[0][2]))

# 2D LIST PRACTICE PROBLEM
# GENERATE THE RANDOM LIST
# make sure you import random
rand_nums = []
for i in range(10): # number of rows
    row = []
    for j in range(5): # columns
        row.append(random.randint(1, 10))
    rand_nums.append(row)

# PRINT THE LIST IN A TABLE FORMAT
for row in rand_nums:
    print(row)

print_table(rand_nums)

# PRINT LARGEST AND SMALLEST NUMBERS IN THE LIST
smallest = largest = rand_nums[0][0]
for row in rand_nums:
    if min(row) < smallest:
        smallest = min(row)
    if max(row) > largest:
        largest = max(row)
print("smallest:", smallest, "largest:", largest)

# DETERMINE NUMBER OF TIMES A USER-SPECIFIED NUMER IS IN LIST
user_val = int(input("Enter a number in [1, 10] to count: "))
count = 0
for row in rand_nums:
    for val in row:
        if val == user_val:
            count += 1
print(user_val, "is in the list", count, "times")

# REMOVE ALL INSTANCES OF A USER-SPECIFIED NUMBER
user_val = int(input("Enter a number in [1, 10] to remove: "))
for row in rand_nums:
    while user_val in row:
        row.remove(user_val)
print_table(rand_nums)