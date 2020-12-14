# define an integer
myint = 7
print(myint)

# define a floating point number
myfloat = 7.0
print(myfloat)

# define a string
mystring = 'yolo'
print(mystring)
mystring = "dolo"
print(mystring)
mystring = "Don't worry about jolo"
print(mystring)

# simple operator example using numbers
one = 1
two = 2
three = one + two
print(three)

# simple operator example using strings
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assignments can be done on more than one variable "simultaneuosly"
a, b = 3, 4
print(a, b)

# final exercise: create a string, integer and floating point number
mystring = "yolodolo"
myfloat = 8.0
myint = 100
if mystring == "yolodolo":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 8.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 100:
    print("Integer: %d" % myint)
