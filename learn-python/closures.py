# a closure is a function object that remembers values in
# enclosing scopes even if they are not present in memory

# a nested function is a function defined inside another function:
# they have access to the variables of the enclosing scope -
# in Python, they are readonly but one can use the "nonlocal" keyword explicitly
# with these variables in order to modify them

# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)
#
#     data_transmitter()
#
# print(transmit_to_space("Test message"))

# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         print(number)
#     printer()
#     print(number)
#
# print_msg(9)

# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)
#     return data_transmitter
#
# fun2 = transmit_to_space("Burn the Sun!")
# fun2()

# the advantage of closures is the avoidance of using global variables and
# provides some form of data hiding (ex. case: when there are few methods in
# a class, use closures instead

# Decorators in Python also make extensive use of closures

# exercise: Make a nested loop and a python closure to make
# functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create
# multiply_with_5() or multiply_with_4() functions using closures.
# your code goes here
def multiplier_of(n):
    def multiplier(number):
        return number * n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))