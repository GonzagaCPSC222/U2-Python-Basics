import math # use code from another python module (AKA file)
import random # GS adding after class
from datetime import datetime

# best practice: put your import statements at top of file
print("hello")

# this is a one line comment
"""
this is a multi
line
comment
"""

# VARIABLES
x = 5.0
print(x)
# use the built in type() function to determine the type of
# a variable or value
print(x, type(x))
# we can reassign variables
x = "hello"
print(x, type(x))

# OPERATORS
# pretty much the same as C++, with a few exceptions
# / floating point division // integer division % mod
print(5 / 2, 5 // 2, 5 % 2)
# exponentiation ** 
print(5 ** 2)
# another way: import the math module
# and call math.pow()
print(math.pow(5, 2))
# && || ! boolean operators in C++
# and or not

# DECIMAL FORMATTING
# lots of diff ways, choose the one you prefer
print("%.2f" %(math.pi))
print("{:.2f}".format(math.pi))
print(f"{math.pi:.2f}")
print(round(math.pi, 2))

# USER INPUT
# print("enter your favorite number: ", end="")
# fav_num = input()
# print(type(fav_num))
# # type conversion
# fav_num = int(fav_num)
# print("your fav number doubled:", 2 * fav_num)

# CONDITIONALS (AKA if statements)
# we have if elif (else if) else
temp = 45
if temp < 32:
    # python uses indentation to group statements together (like { })
    print("it is cold out")
elif temp < 60:
    print("it is not too bad out")
else:
    print("it is warm out")

# you can nest if statements inside if statements
# watch your indentation

# LOOPS
# we have for loops and while loops
# for item in sequence:
#     body of statements to be repeated
for char in "hello":
    print(char)
for item in [1, 2, 3, 4]: # list
    print(item)
# we can make our own numeric sequences with range()
# range(stop) [0, stop)
# range(start, stop) [start, stop)
# range(start, stop, step) step to specify a inc/dec other than 1
for i in range(-2, 5, 2):
    print(i)

# task: print the first 20 even numbers all on one line
# separated by a comma and a space
# 2, 4, ...., 40
for i in range(2, 40, 2):
    print(i, end=", ")
print(i + 2)

# while loop structure
# while boolean condition is true:
#    body (code we want repeated)
#    progress towards boolean condition being false
# task: rewrite the even number loop using a while loop
i = 2
while i <= 38:
    print(i, end=", ")
    i += 2
print(i)

# you can get an early exit from a loop with the break keyword
# while True:
#     user_input = input("enter a word (\"stop\" to exit): ")
#     if user_input == "stop":
#         break
# print("outside the loop")

# FUNCTIONS
# a function is a named sequence of statements
# functions can accept inputs (arguments when you call; 
# parameters when you define the function)
# they can return 0 or more values
# def function_name(parameter list):
#     body (only executes once you call the function)
def my_print(msg_str): # header
    """docstring
    prepends a timestamp to the msg_str before printing
    """
    print(f"{datetime.now()}: {msg_str}")

my_print("testing123")

# task: define/call a function that accepts a radius
# and returns the area and circumference of a circle with that radius

# GS adding after class
# no return
def compute_circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print("area:", area, "circumference:", circumference)

compute_circle_stats(5)

# with return
def compute_circle_stats2(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference # send back values to the calling code!!

# unpacks return values
area_result, circum_result = compute_circle_stats2(5)
print("area result:", area_result, "circumference result:", circum_result)
# doesn't unpack return values (leaves them in tuple)
result = compute_circle_stats2(5)
print("type(result):", type(result))
print("result:", result, result[0], result[1])

# RANDOM NUMBERS
# often we need random numbers for simulating random events
# or initializing the state of an algorithm

# if you want the same random numbers each time you run
# your program, "seed" the random number generator
random.seed(0)

# lets roll a 6 sided die
# import the random module
roll = random.randrange(1, 7) # [1, 7)
print("roll:", roll)
roll = random.randint(1, 6) # [1, 6]
print("roll:", roll)