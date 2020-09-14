import math # by convention, all imports should be at
# the top of the file
import random

# a one line comment
# comments are ignored by Python

'''
this is 
a multi line
comment
'''

# variables
# a variable store a value
# they also have a data type 
# (what range of values can be stored)
x = 5 # "x is assigned 5" 
# the data type of x is integer
print(type(x))
x = 5.5 # floating point value (fractional)
print(type(x))
my_name = "gina" # string (sequence of characters)
print(my_name)

# operators
# * multiplication
# / floating point division
# // integer division
print(5 / 2)
print(5 // 2)
# remember PEMDAS
# also print a python operator precedence table
# ** power
print(2 ** 5)
# you can import math module
# sqrt() pow() tan()

print(math.pow(2, 5))

# # getting input from the user
# user_name = input("what is your name? ")
# print("hi, " + user_name)
# # for a numeric input, typecast to int() or float()
# user_number = int(input("what is your fav number? "))
# print(type(user_number))

# print formatting of decimal (floating) numbers
# c style
print("%.2f" %(math.pi))
# python style
print("{:.2f}".format(math.pi))
# how to round a decimal number
pi_rounded = round(math.pi, 2)
print(pi_rounded)

# conditionals (if statements)
# if a boolean condition (BC) is true, then execute some code
x = 7 
if x == 5: 
    print("x is 5")
    # 4 spaces denotes membership of a body (like { })
else: # executed when the if BC is false
    print("x is not 5")
# elif keyword (else if)
# you can nest if statememnt

# loops
# while loop in Python just like in C/C++/Java
# for in loop
for i in range(0, 5, 1):
    print(i)

# warm up task
#q = (k * A * (T1 - T2)) / L
# m = int(input("Enter an integer> "))
# n = int(input("Enter an integer> "))
# m = m + 5
# n = 3 * n
# print("m =", m, "\nn =", n)
# print("m = %d" %(m))

# 2 4 6 8 .... 40
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# use help() to view the documentation for an identifier (print)
#help(print) # press q to quit the help

# loops are used to repeat a sequence of statement
# while loop solution to the above
i = 2 
while i <= 38: 
    print(i, end=", ")
    # progress towards the boolean condition being false
    i += 2
print(i)

# more on for loops
# for item in sequence:
#   body (sequence of statement to be repeated)

# a list a sequence of items
animals = ["pig", "dragon"]
for animal in animals:
    print(animal)

# a string is a sequence of characters
my_str = "aardvark" # not a bird
for char in my_str:
    print(char)

# advanced loops...
# you can nest loops
# you can use break to get an early exit from a loop
# while True:
#     user_input = input("Please enter a word (stop to quit): ")
#     if user_input == "stop":
#         break

# random numbers
# lets throw a 6-side die
# import the random module
# random.randrange(start, stop) [start, stop)
roll = random.randrange(0, 6) + 1 # [1, 6]
print(roll)
# random.randint(start, stop) [start, stop]
roll = random.randint(1, 6) # [1, 6]
print(roll)

# functions
# a function a named sequence of statements
# mostly used for reusability (define a function one time and call multiple times)
# and for code organization
# def function_name(parameters list):
#   body of statements that belong to the function

# example 1: no parameters (e.g. no input arguments) and no return value
def sayHello():
    print("hello")
# need to call the function to execute its body
sayHello()

# example 2: one parameter (call the function pass in one input argument) and no return value
def say(message):
    print(message)
say("HELLO")
say("hola!!!")
say("goodbye")

# task: define/call a function that accepts the radius of a circle and prints the area of the circle
# relevant formula: pi * r^2
def computeCircleArea(radius):
    area = math.pi * pow(radius, 2)
    print(area)
computeCircleArea(5.0)

# example 3: one parameter, one return value (a return value is the output of a function)
def computeCircleArea2(radius):
    area = math.pi * pow(radius, 2)
    return area
result = computeCircleArea2(5.0)
print(result)

# example 4: one parameter, two return values (remember, you can return multiple values in python)
def computeCircleAreaANDCircumference(radius):
    area = math.pi * pow(radius, 2)
    circumference = 2 * math.pi * radius
    return area, circumference

result1, result2 = computeCircleAreaANDCircumference(5.0)
print(result1, result2)