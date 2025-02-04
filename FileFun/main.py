# FILES
# a file stores data on a file system
# "on disk"

# goal: is to load the contents of data.csv
# into our python program memory
# stored as a 2D list

# 3-step file processing template
# 1. open file
# 2. process file (e.g., read or write)
# 3. close the file

def load_lines_from_file(filename):
    # filename is a string with a relative
    # path to the file to process
    # 1. 
    infile = open(filename, "r")
    # 2.
    lines = infile.readlines()
    # 3.
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

def restructure_lines_into_table(lines):
    table = []
    for line in lines:
        row = line.split(",")
        # print("row:", row)
        table.append(row)

    return table

def convert_column_to_numeric(table, column_index):
    for row in table:
        # NOTE: float() will throw an exception if it cannot
        # convert the string to a float
        # look into try except statements to handle this
        row[column_index] = float(row[column_index])

# GS adding after class
def pretty_print(header, table):
    # this doesn't perfectly align, but it is 
    # a quick and dirty way that works for 
    # this small table
    for col_name in header:
        print(col_name, end="\t")
    print()
    for row in table:
        for val in row:
            print(val, end="\t")
        print()
    print()

lines = load_lines_from_file("data.csv")
print("lines:", lines)
# TASK: clean the newlines 
clean_lines(lines)
print("lines:", lines)
# restructure into 2D list of rows with column values
table = restructure_lines_into_table(lines)
header = table.pop(0)
print(header)
print(table)
convert_column_to_numeric(table, 1) # 1 corresponds to Calories Burned
convert_column_to_numeric(table, 2) # 2 corresponds to Steps
print("after conversion")
print(header)
print(table)
# TODO: write a pretty_print() function to print out the table in a 
# nice grid like function
# GS adding after class
pretty_print(header, table)