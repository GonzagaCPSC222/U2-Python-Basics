import math

# this is a one line commentgjfakhdfklghadkfjhg
# a comment is used to document your code
# comments are ignored by python

"""
this is
a multi
line comment
AKA block comment
"""

# game plan:
# 1. variables
# 2. operators
# 3. getting input from the user
# 4. formatting decimal numbers

# VARIABLES
# a variable stores a value
x = 5 # read as "x is assigned 5", "x holds 5", etc.
# NOT "x equals 5"
# the value 5 is an integer (int for short)
print(x)
# we can check the type of x
# the data type represents the range of
# values
print(type(x))
# we can reassign x
x = 5.5
# this is a float data type
# a number with a fractional part
print(x)
print(type(x))
x = "hello"
# this is a string data type
# a sequence of characters
print(x)
print(type(x))

# OPERATORS
# +, -
# * is multiplication
print(4 * 5)
# / is floating point division (like "normal" division)
print(5 / 2)
# // is integer division (is the whole number 
# result of floating point division)
print(5 // 2)
# % is the modulus operator (it is the remainder
# of integer division)
print(5 % 2)
# ** is the exponentiation operator (power)
print(5 ** 2)

# warm up
# print(3.0 % 1)
# print(3 / 0)
# print(2 ** 4 ** (2 / 4))

# we can also do exponentiation with the pow() function
# we need to import the math module
# a module is a python file
print(math.pow(5, 2))

# GETTING INPUT FROM THE USER
print("Enter your favorite number: ")
fav_num = input()
print(type(fav_num))
print("Your favorite number doubled is:", 2 * int(fav_num))
# we often need to convert between types
# type conversion
fav_num_int = int(fav_num)
print("Your favorite number doubled is:", 2 * fav_num_int)

# DECIMAL FORMATTING
# there are LOTS of ways to do this!!
print(math.pi)
print("%.2f" %(math.pi))
print("{:.2f}".format(math.pi))
print(f"{math.pi:.2f}")
print(round(math.pi, 2))

# CONDITIONALS (AKA if statements)
# if some condition (boolean condition) is true
# then execute some code
x = 7
if x == 5: # == is the equality operator
    print("hello")
    # python uses indentation (1 tab = 4 spaces)
    # to group code together into "blocks"
    # like { } C/C++