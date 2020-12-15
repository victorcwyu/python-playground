# divide code into useful blocks
# allows us to order code, make it more readable, reuse it and save time
# a key way to define interfaces to share code

# defined using the block keyword "def", followed by the function name as the block name
def my_function():
    print("Yolo")

# may receive arguments (variables passed from the caller to the function)
def my_function_args(name, greeting):
    print("Yolo %s %s!" % (name, greeting))
my_function_args("Jolo", "Dolo")

# may also return a value to the caller
def sum_nums(a, b):
    return a + b

print(sum_nums(2, 4))

# use an existing function, while adding own to create a program
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    # return benefit + " is a benefit of functions!"
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()