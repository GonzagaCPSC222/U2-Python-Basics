# Write Python code that prompts the user for a letter. Count the number of times the letter appears in the following string: 
# sentence = "the quick brown fox jumps over the lazy dog".
# You may assume the sentence variable is defined. You do not need to define a function to do this.
# For example, if the user enters in "t", then the program displays 2 (there are 2 of t in the sentence).

# sentence is assumed declared as follows
sentence = "the quick brown fox jumps over the lazy dog"

user_letter = input("Enter a letter: ")
count = 0
for letter in sentence:
    if letter == user_letter:
        count += 1
print(count)

# OR use a string method:
print(sentence.count(user_letter))


# Define a Python function called doubleList() that accepts a 1D list of integers
# and returns a new list that contains all the values in the parameter list, multiplied by 2. 
# For example, doubleList([1, 2, 3]) should return the list [2, 4, 6]

def double_list(values):
    doubled_values = []
    for val in values:
        doubled_values.append(val * 2)
    return doubled_values

# example call
print(double_list([1, 2, 3]))