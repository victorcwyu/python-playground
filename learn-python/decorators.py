# decorators allow you to make simple modifications to callable objects like
# functions, methods or classes

# the following two examples are equivalent:
# @decorator
# def functions(arg):
#     return "value"
#
# def function(arg):
#     return "value"
# function = decorator(function) # this passes the function to the decorator,
# # and reassigns it to the functions

# the following two examples are also equivalent:
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = my_decorator(say_whee)
#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")

# a decorator is just a function which takes functions and returns one
# def repeater(old_function):
#     def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
#         old_function(*args, **kwds) # we run the old function
#         old_function(*args, **kwds) # we do it twice
#     return new_function # we have to return the new_function, or it wouldn't reassign it to the value
#
# # solution 1:
# @repeater
# def multiply(num1, num2):
#     print(num1 * num2)
#
# multiply(2, 3)
#
# # solution 2:
# def multiply(num1, num2):
#     print(num1 * num2)
#
# multiply = repeater(multiply)
#
# multiply(2, 3)

# # change the output:
# def double_out(old_function):
#     def new_function(*args, **kwds):
#         return 2 * old_function(*args, **kwds) # modify the return value
#     return new_function
#
# @double_out
# def yolo(num):
#     print(num)
#
# yolo(5)

# # change the input (if the old function has only one argument)
# def double_out(old_function):
#     def new_function(arg):
#         return old_function(arg * 10)  # modify the argumentt passed
#     return new_function
#
# @double_out
# def yolo(num):
#     print(num)
#
# yolo(5)

# # do checking:
# def check(old_function):
#     def new_function(arg):
#         if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
#         old_function(arg)
#     return new_function
#
# @check
# def yolo(num):
#     print(num)
#
# yolo(-2)

# # multiply the output by a variable amount
# def multiply(multiplier):
#     def multiply_generator(old_function):
#         def new_function(*args, **kwds):
#             return multiplier * old_function(*args, **kwds)
#         return new_function
#     return multiply_generator # it returns the new generator
#
# # Usage
# @multiply(3) # multiply is not a generator, but multiply(3) is
# def return_num(num):
#     return num
#
# # Now return_num is decorated and reassigned into itself
# return_num(5) # should return 15
# print(return_num(5))

# exercise: Make a decorator factory which returns a decorator that
# decorates functions with one argument.
# The factory should take one argument, a type, and then
# returns a decorator that makes function should check if
# the input is the correct type.
# If it is wrong, it should print("Bad Type")
# (In reality, it should raise an error, but
# error raising isn't in this tutorial).
# Look at the tutorial code and expected output to see
# what it is if you are confused (I know I would be.)
# Using isinstance(object, type_of_object) or type(object) might help.
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])