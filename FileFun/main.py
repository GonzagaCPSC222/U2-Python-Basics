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

lines = load_lines_from_file("data.csv")
print("lines:", lines)
# TASK: 
# clean the newlines 
# restructure into 2D list of rows with column values