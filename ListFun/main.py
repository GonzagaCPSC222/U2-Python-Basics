import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
# list_ints = [100, 1, 10, 20]
# # there are unique indexes for each element in the list
# # 0-based... meaning the first element is at 0, and the last element is at n - 1
# # where n is the number of elements in the list

# print(list_ints[0])
# print(list_ints[-4])

# # types can be mixed in a list
# list_numbers = [0, 0.0, 1, 1.0, -2]
# print(list_numbers)
# print(type(list_numbers))
# # lists are mutable (they can be changed)
# list_numbers[0] = "hello"
# print(list_numbers)

# # use len() to find out how many elements are in a list
# print(len(list_numbers))
# list_numbers.append("another element")
# # print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
# print(list_numbers[len(list_numbers) - 1])

# # we can declare an empty list!
# empty_list = []
# print(len(empty_list))

# # we can have lists of lists (2D or ND)
# nested_list = [[0, 1], [2], [3], [4, 5], []]
# print(len(nested_list))
# print(len(nested_list[0]))

# # looping through list items
# candies = ["twix", "reeses", "oreos", "snickers"]
# print(candies)

# for candy in candies:
#     print(candy)

# i = 0
# while i < len(candies):
#     print(i, candies[i])
#     i += 1

# i = 0
# for i in range(len(candies)):
#     print(i, candies[i])

# # common list operators
# # list concatenation... adding 2 lists together
# print(candies)
# candies += ["m&ms", "starburst"]
# print(candies)
# # list repetition... repeating elements in a list
# bag_o_candies = 5 * ["twix", "snickers"]
# print(bag_o_candies)
# # list slicing
# print(candies[1:3]) # : is the slice operator. start index is inclusive
# # end index is exclusive
# # if you ever need a copy of a list, you can simply use the : with no start or end indices
# copy_of_candies = candies[:]
# copy_of_candies[0] = "TWIX"
# print(copy_of_candies)
# print(candies)

# # list methods 
# candies.remove("reeses")
# print(candies)

# # more on list methods
# cars = ["corolla", "lambourghini"]
# # append()
# cars.append("pilot")
# print(cars)
# # extend()
# cars.extend(["sentra", "mercedes"])
# print(cars)
# # += 
# cars2 = ["civic", "acura"]
# cars += cars2
# print(cars)
# # pop()
# cars.pop(3)
# print(cars)
# # create a string from a list of strings
# word_list = ["c", "or", "o", "lla"]
# word_str = "".join(word_list)
# print(word_str)
# # create a list from a string
# word_list2 = list(word_str)
# print(word_list2)
# comma_separated_value_str = "c,or,o,lla"
# word_list3 = comma_separated_value_str.split(",")
# print(word_list3)

# # 1D List Practice Problem
# # In ListFun, write code that generates 20 random numbers between
# # 1 and 10 inclusive and puts them in a 1D list.
# # The program then does the following using the list:
# nums = []
# for i in range(20):
#     rand_num = random.randint(1, 10)
#     nums.append(rand_num)
# print(nums)

# # Prints the numbers all one line, each number separated by a space
# for num in nums:
#     print(num, end=" ")
# print()

# # Sorts the list using a list method
# nums.sort() # inplace sort
# print(nums)
# # nums_copy_sorted = sorted(nums) # sorts on copy and returns sorted copy
# # print(nums)
# # print(nums_copy_sorted)

# # Prints the largest and smallest number in the list
# # Hint: can you take advantage of the current ordering of your list?
# print("min:", nums[0], "max:", nums[-1])
# print("min:", min(nums), "max:", max(nums))

# # Determines the number of times a user-specified number is in the list
# user_input = int(input("Enter a number to count: "))
# print("Count:", nums.count(user_input))
# # OR
# count = 0
# for num in nums:
#     if num == user_input:
#         count += 1
# print("Count:", count)

# # Removes all instances of a user-specified number in the list. 
# # If the number is not in the list print the message: 
# # "Sorry, your number is not here!"
# user_input = int(input("Enter a number to remove all occurences of: "))
# if user_input in nums:
#     while user_input in nums:
#         nums.remove(user_input)
# else:
#     print("Sorry, your number is not here!")
# print(nums)


# # Note: for practice with functions, try solving this problem using functions :)

# # 2D List Practice Problem
# # In ListFun, write code that generates 50 random numbers between 1 and 10
# # inclusive and puts them in a 2D list that is 10x5
# # (e.g. 10 rows and 5 columns). The program then does the following using the list:
# table = []
# for i in range(10):
#     # build a row
#     row = []
#     for j in range(5):
#         # generate a random number
#         rand_num = random.randrange(1, 11)
#         row.append(rand_num)
#     table.append(row)
# print(table)

# # Prints the numbers in a nice grid format (like a table)
# for row in table:
#     # row is a 1D list of numbers
#     for num in row:
#         print(num, end="\t")
#     print()

# # Prints the largest and smallest number in the list
# # assume the first number is the smallest and the largest
# curr_min = curr_max = table[0][0]
# for row in table:
#     for value in row:
#         if value < curr_min:
#             # we have a new min
#             curr_min = value
#         if value > curr_max:
#             # we have a new max
#             curr_max = value
# print("min:", curr_min, "max:", curr_max)

# # Determines the number of times a user-specified number is in the list
# user_input = int(input("Enter a number to count: "))
# count = 0
# for row in table:
#     for num in row:
#         if num == user_input:
#             count += 1
# print("Count:", count)

# # Removes all instances of a user-specified number in the list.
# # If the number is not in the list print the message:
# # "Sorry, your number is not here!"
# user_input = int(input("Enter a number to remove all occurences of: "))
# removed = False
# for row in table:
#     while user_input in row:
#         row.remove(user_input)
#         removed = True
# if not removed:
#     print("Sorry, your number is not here!")
# print(table)

# Note: for practice with functions, try solving this problem using functions :)

# LIST ALIASING
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1 # not a copy!!! list3 is an "alias" for list1
print(list1, list2, list3)
list3[0] = 200
print(list1, list2, list3)

def add_one_to_each_element(some_list):
    # some_list is an alias to the same list list3 refers to
    for i in range(len(some_list)):
        some_list[i] += 1

add_one_to_each_element(list3)
print(list1, list2, list3)
# python is "pass by object reference"
# if you pass a list to a function, code in that
# function can modify the list

# more on STRINGS
word = "gonzaga"
# 0-based indexing
print(word[0], word[-1], word[2:4])
# strings are immutable (cannot be changed)
# word[0] = "G"
word = "G" + word[1:]
print(word)
# string concatenation +
# string repetition *
print(word * 5)
# string comparison < <= >= == !=
print("bird" < "cat")
# strings are compared character by characters
# based on ASCII values
print("bird" < "Bird")
