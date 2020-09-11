import math # by convention, all imports should be at
# the top of the file

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

