# map and filter are built-in (in the __builtins__ module) and require no importing
# reduce needs importing since it resides in the functools module

# map syntax: map(func, *iterables)
# func is the function on which each element in iterables would be applied on
# Python 3 returns a map object, to get the result as a list use:
# list(map(func, *iterables))
# the number of args to func must be the number of iterables listed

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# is equivalent to:
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# example with a function that takes 2 args:
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)

# example where iterable length is less than that of the first:
# Python simply stops when it can't find the next element in one of the iterables
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,3)))

print(result)

# example of zip() usage
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(zip(my_strings, my_numbers))

print(results)

# a custom zip() function:
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)

# filter() requires the function to return boolean values (true or false)
# and then passes each element in the iterable through the function,
# "filtering" away those that are false

# syntax: filter(func, iterable)

# only one iterable required

# The func argument is required to return a boolean type.
# If it doesn't, filter simply returns the iterable passed to it.
# Also, as only one iterable is required, it's implicit that func
# must only take one argument.

# filter passes each element in the iterable through func and
# returns only the ones that evaluate to true

# example: filter out those who passed with scores more than 75
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# example: palindrome detector
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

# reduce applies a function of two arguments cumulatively to the elements
# of an iterable, optionally starting with an initial argument

# syntax: reduce(func, iterable[, initial])

# func is the function on which each element in the iterable gets
# cumulatively applied to

# initial is the optional value that gets placed before
# the elements of the iterable in the calculation,
# and serves as a default when the iterable is empty

# func requires two arguments, the first of which is the first element
# in iterable (if initial is not supplied) and the second element in iterable.
# If initial is supplied, then it becomes the first argument to func and
# the first element in iterable becomes the second element.

# reduce "reduces" iterable into a single value

# example: sum() returns the sum of all the items in the iterable passed to it
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

# same example but with the optional initial value:
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)

# exercise: use each of map, filter, and reduce to fix broken code.
from functools import reduce

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x * x, 2), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)