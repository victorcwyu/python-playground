# objects are an encapsulation of variables and functions into a single entity
# objects get variables and functions from classes
# classes are a template to create your own objects

# a basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

# access the variable inside the new object
print(myobjectx.variable)

# create another object
# each object contains independent copies of the variables defined in the class
myobjecty = MyClass()
myobjecty.variable = "yolo"
print(myobjectx.variable)
print(myobjecty.variable)

# access object function
myobjectx.function()

# Create two new vehicles called car1 and car2
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer
# and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())