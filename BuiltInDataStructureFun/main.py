# three commonly used "built in" data structures
# 1. list
# 2. tuple
# 3. dictionary

# a list a sequence of items
# 0-based for indexing
# lists are mutable (they can be changed)
# lists have an order to their items
#     -len    ...   -2   -1
#       0  1   2  3  4  5
nums = [3, 6, -1, 7, 9, 7]
print(nums)
print(nums[0], nums[-6], nums[0:2])

# append an item
nums.append(100)
print(nums)
# remove an item
nums.remove(7)
print(nums)

# lists have an order
# means we can sort...
print(nums)
nums.sort() # inplace sort low to high
print(nums)

# 1D lists (line-like)
# 2D lists (grid-like)
# 3D lists (cube-like)
# 4D-ND lists....

# 2D lists
# there are two main ways to think about 2D lists
# 1. like a table (it has rows and cols, or it has x axis and y axis)
matrix = [  [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(matrix[0][0])
print(matrix[1][2])
# 2. a 1D list where each item is a 1D list (nested lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix[0]))
print(type(matrix[0][0]))

# 3D lists
cube = [[[0, 0], [1, 1]], [[2, 2], [3, 3]]]
print(cube[0][0][0])

# tuples
# a tuple is an immutable list (cannot be changed)
my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))
#my_tuple[0] = "X"

# when declaring a single item tuple, you have to have a comma after it
my_single_item_tuple = (1, )
print(my_single_item_tuple)
# to create an empty tuple
my_empty_tuple = tuple()
print(my_empty_tuple)

# tuple indexing and slicing is the same as for lists
# tuples are used for returning multiple values

# dictionaries
# a dictionary is a list with keys and indexes and values mapped from those keys
# a key value pair
# use a key to look up a value
# keys in a dictionary must be unique
# example of a key: student ID
# example of a value: student name
# loop up ID 12345 -> "Jane Doe"
my_dict = {} # empty dictionary
my_empty_dict = dict()
print(my_dict)
my_dict["12345"] = "Jane Doe"
print(my_dict)

state_capitals = {"washington": "olympia", "idaho": "boise", "oregon": "portland"}
print(state_capitals)
# dictionaries are mutable
#state_capitals["washington"] = "spokane"
#print(state_capitals)
# add another state capitals
state_capitals["california"] = "sacremento"
print(state_capitals)
# the key value pairs in a dictionary are not ordered!!!

# initialize a dict using a list of tuples
roman_numerals = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50)])
print(roman_numerals)
roman_numerals_as_list = list(roman_numerals.items())
print(roman_numerals_as_list)

# types for keys: integers, strings, files, tuples, etc. 
# lists cannot be as keys
# types for values: any type

# len()
print(len(state_capitals))
# check for the existence of a key
print("washington" in state_capitals)
print("olympia" in state_capitals.values())
# loop through the key value pairs in a dictionary
for state in state_capitals:
    print(state, state_capitals[state])
for (state, capital) in state_capitals.items():
    print(state, "*", capital)