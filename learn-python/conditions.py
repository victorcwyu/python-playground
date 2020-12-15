# single equals is for variable assignment
x = 2
# double equals is for comparison, != for not equals
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John and you are 23.")
if name == "John" or name == "Rick":
    print("You are John or Rick.")

# in is used to check if a specified object exists in an iterable object container
name = "John"
if name in ["John", "Rick"]:
    print("You are John or Rick.")

# code blocks defined by indentation, no termination necessary
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two!")

# a statement is true if:
# 1. the true boolean variable is given or calculated
# 2. an object which is not considered "empty" is passed
# examples of 2: empty string, empty list ([]), 0, the false boolean variable: False

# unlike ==, "is" does not match the values, but the instances
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# "not" before a boolean expression inverts it
print(not False)
print((not False) == False)

# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")