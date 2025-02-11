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
# continuing in class
food = ["chips", "fish"]
# append 
food.append("pizza")
print(food)
# extend (for appending items in another list)
food.extend(["cheese", "crackers"])
print(food)
# += list concatenate and assign
food += candies
print(food)
# pop(index) for position based removal
item = food.pop(1)
print(item, food)

# lists and strings
# creating a string from a list of strings
# using the string join method
list_of_strings = ["co", "m", "pute", "r"]
word = "julian".join(list_of_strings)
print(word)
# how to make a list from a string
list_of_strings2 = list(word)
print(list_of_strings2)
comma_separated_word = "co,m,pute,r"
# split is a string method
list_of_strings3 = comma_separated_word.split(",") # default delimiter is 
# any whitespace
print(list_of_strings3)

# LIST ALIASING
def add_one_to_each_element(nums_list):
    nums_list = []
    for i in range(len(nums_list)):
        nums_list[i] += 1

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
# list2 is a different list object from list1 (though they have the same values)
list1[0] = 10
print(list1, list2)
list3 = list1
# list3 is an "alias" for the same object that list1 refers to
list3[0] = 100
print(list1, list2, list3)
add_one_to_each_element(list1) # nums_list will be an alias for list1's object
print("after call:", list1, list2, list3)
# to make a copy of a 1D list: use the list copy() method
list4 = list1.copy() # "shallow" copy
list1[0] = 10000
print(list1, list2, list3, list4)
# python is pass by object reference
# functions with a reference to an object passed in
# can modify the object

# a few more words about strings
# strings are immutable (cannot be changed)
# they support 0-based indexing and slicing
# they have methods, like split() and join()
# strip()
word = "  \t   \n\n  basketball\n   \n"
print(word)
print(repr(word))
word = word.strip()
print(repr(word))
# find()
print(word.find("et"))
print(word.find("k"))
print(word.find("z"))
