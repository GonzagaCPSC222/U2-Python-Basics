import math # use code from another python module (AKA file)
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