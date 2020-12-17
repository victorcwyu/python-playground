# generators are simple functions which return an iterable set of items,
# one at a time, in a special way
#
# when an iteration over a set of items starts using the for statement,
# the generator is run
#
# once the code reaches a "yield", the generator yields its execution back to
# the for loop, returning a new value from the set
#
# the function can generate infinite values, yielding each one in its turn

import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)
#
#     # return a 7th number between 1 and 15
#     yield random.randint(1, 15)
#
# for random_number in lottery():
#     print("And the next number is... %d!" % (random_number))
#
# exercise: write a generator function which returns the Fibonacci series
#
# this code will simultaneously switch the values of a and b:
# a = 1
# b = 2
# a, b = b, a
# print(a,b)
#
# fill in this function
def fib():
    # pass #this is a null statement which does nothing when executed, useful as a placeholder.
    a, b = 1, 1
    # infinite loop
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break