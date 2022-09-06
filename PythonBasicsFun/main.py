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