# every function receives a predefined number of arguments, but it is also
# possible to declare functions which receive a variable number of arguments
# def foo(first, second, third, *therest):
#     print("First: %s" % first)
#     print("Second: %s" % second)
#     print("Third: %s" % third)
#     print("And all the rest... %s" % list(therest))
#
#
# foo(1, 2, 3, 4, 5, 6)


# it is possible to send arguments by keyword, so the order does not matter
# in this example, bar receives 3 arguments
# if an additional "action" arg is received, is sums the numbers and prints
# alternatively, the func knows it must return the first arg,
# if the the value of the number parameter is equal to "first"
# def bar(first, second, third, **options):
#     if options.get("action") == "sum":
#         print("The sum is: %d" % (first + second + third))
#
#     if options.get("number") == "first":
#         return first
#
#
# result = bar(1, 2, 3, action="sum", number="first")
# print("Result: %d" %(result))

# exercise: Fill in the foo and bar functions so they can receive
# a variable amount of arguments (3 or more) The foo function must
# return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber
# is worth 7, and False otherwise.
# edit the functions prototype and implementation
def foo(a, b, c, *therest):
    return len(therest)

def bar(a, b, c, **options):
    # if options.get("magicnumber") == 7:
    #     return True
    # else:
    #     return False
    # alternate answer
    # return True if options.get("magicnumber") == 7 else False
    #
    # alternate answer
    return options["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")