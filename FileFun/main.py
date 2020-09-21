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
