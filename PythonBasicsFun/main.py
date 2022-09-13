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
# print("Enter your favorite number: ")
# fav_num = input()
# print(type(fav_num))
# print("Your favorite number doubled is:", 2 * int(fav_num))
# # we often need to convert between types
# # type conversion
# fav_num_int = int(fav_num)
# print("Your favorite number doubled is:", 2 * fav_num_int)

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

# we also have an else keyword
# else executes when preceding if conditions is false
if x == 5:
    print("x is 5")
else:
    print("x is not 5")

# we also have an elif (else if) keyword
# use elif when you want to test multiple conditions in a row
x = -2
if x < 0:
    print("x is negative")
elif x > 0:
    print("x is positive")
else:
    print("x is 0")

# you can nest if statements (put an if inside another if)
# be aware of indentation

# LOOPS
# use a loop when you want to repeat code
# we have for loops and while loops
# for loop structure
# for item in sequence:
#    body of for loop (code you want repeated)
for item in [3, 5, 7, "hello"]:
    print(item)
for letter in "slalom":
    print(letter)
# we can also make our own sequences using range()
# range(stop) # [0, stop)
for i in range(9):
    print(i, end=" ")
print()

# range(start, stop) # [start, stop)
for i in range(4, 9):
    print(i, end=" ")
print()

# range(start, stop, step) # [start, stop) up by step
for i in range(4, 9, 2):
    print(i, end=" ")
print()
print("hello")

# task: write a for loop to print 8 6 4
for i in range(8, 2, -2):
    print(i, end=" ")
print()

# task: write a for loop to print the first 20 even numbers
# 2, 4, ..., 38, 40
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# ADVANCED LOOPS
# like if statements you can nest loops
# we can get an early exit from a loop with the break keyword
# while loops
# while loop structure
# while *condition* is true:
#    body of loop (code to repeated)
#    progress towards the *condition* being false
# while True:
#     user_input = input("Enter a word (stop to exit): ")
#     if user_input == "stop":
#         break # early exit

# task: rewrite the first 20 even # code to use a while loop instead of a for loop
k = 2
while k <= 38:
    print(k, end=", ")
    k += 2 # progress towards k > 38
print(k)

# FUNCTIONS
# a named sequence of statements
# we have been using functions: math.pow(), print(), sorted(), len()
# int(), range(), input()
# now it is time to write our own
# functions accept input (arguments when you "call" the function,
# parameters when you "define" the function)
# functions produce output (return values AKA results)
# function definition structure
# def function_name(parameter list):
#    function body (statements to be executed when this function
#    is "called")

# example 1: a function with no inputs (no arguments when you call it)
# and no outputs
# definition
def say_hello():
    print("hello")
# body of function only executes when you call the function
say_hello() # function call
for i in range(10):
    say_hello()

# example 2: a function with one inputs (one argument when you call it)
# and no outputs
def say(message):
    print("message:", message)
say("yo yo") # function call
# "yo yo" is the argument
# message is the parameter

# task: define/call function that accepts a radius of a circle
# and prints the circle's area
def print_circle_area(radius):
    area = math.pi * radius ** 2
    print("area:", area)
print_circle_area(5)

# example 3 (a function with one input and one output)
def compute_circle_area(radius):
    area = math.pi * radius ** 2
    return area # send back this value to the calling code!!

result = compute_circle_area(5)
print("result:", result)



# why use functions??