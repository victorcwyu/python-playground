# partial functions can be created by using the partial function from the functools library

# they allow one to derive a function with x parameters to a function with
# fewer parameters and fixed values set for the more limited function

# this code will return 8:
from functools import partial

def multiply(x, y):
    return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

# exercise: Edit the function provided by calling partial() and
# replacing the first three variables in func().
# Then print with the new partial function using
# only one input variable so that the output equals 60.

# Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
new = partial(func, 0, 0, 0)
print(new(60))
