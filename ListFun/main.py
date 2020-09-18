import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
list_ints = [100, 1, 10, 20]
# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list

print(list_ints[0])
print(list_ints[-4])

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)
print(type(list_numbers))
# lists are mutable (they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

# use len() to find out how many elements are in a list
print(len(list_numbers))
list_numbers.append("another element")
# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
print(list_numbers[len(list_numbers) - 1])

# we can declare an empty list!
empty_list = []
print(len(empty_list))

# we can have lists of lists (2D or ND)
nested_list = [[0, 1], [2], [3], [4, 5], []]
print(len(nested_list))
print(len(nested_list[0]))

# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]
print(candies)

for candy in candies:
    print(candy)

i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

i = 0
for i in range(len(candies)):
    print(i, candies[i])

# common list operators
# list concatenation... adding 2 lists together
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
# list repetition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)
# list slicing
print(candies[1:3]) # : is the slice operator. start index is inclusive
# end index is exclusive
# if you ever need a copy of a list, you can simply use the : with no start or end indices
copy_of_candies = candies[:]
copy_of_candies[0] = "TWIX"
print(copy_of_candies)
print(candies)

# list methods 
candies.remove("reeses")
print(candies)

# 1D list practice problem (warm-up 9/18)
# GENERATE THE RANDOM LIST
# make sure you import random
rand_nums = []
for _ in range(20):
    rand_nums.append(random.randint(1, 10))

# PRINT THE LIST ALL ON ONE LINE
def pretty_print(nums):
    for val in nums:
        print(val, end=" ")
    print() 

pretty_print(rand_nums)

# SORT THE LIST USING A LIST METHOD
rand_nums.sort()
print("after sorting")
pretty_print(rand_nums)

# PRINT LARGEST AND SMALLEST NUMBERS IN THE LIST
print(rand_nums[0], rand_nums[-1])

# DETERMINE NUMBER OF TIMES A USER-SPECIFIED NUMER IS IN LIST
# user_val = int(input("Enter a number in [1, 10] to count: "))
# count = 0
# for val in rand_nums:
#     if val == user_val:
#         count += 1
# print(user_val, "is in the list", count, "times")

# # REMOVE ALL INSTANCES OF A USER-SPECIFIED NUMBER
# user_val = int(input("Enter a number in [1, 10] to remove: "))
# while user_val in rand_nums:
#     rand_nums.remove(user_val)
# pretty_print(rand_nums)

# (more) list methods
chips = ["doritos"]
print(chips)
# append
chips.append("bbq")
print(chips)
# extend
# += 
chips.extend(["salt&vinegar", "cheetos"])
print(chips)
# sort
chips.sort()
print(chips)
# pop (like remove, but you pass in an index)
chip_popped = chips.pop(0)
print("popped", chip_popped, "from", chips)
# make a string from a list of strings
cool_ranch = ["c", "o", "ol", " ", "ranch"]
cool_ranch_string = "".join(cool_ranch)
print(cool_ranch_string)
# make a list from a string
cool_ranch_list_of_chars = list(cool_ranch_string)
print(cool_ranch_list_of_chars)
# another way to make a list from a string... separate on delimiter
chip_string2 = "cheetos,bbq,doritos" # delimiter ,
chip_list2 = chip_string2.split(",")
print(chip_list2)

# TODO: list aliasing
# TODO: 2D list practice problem
