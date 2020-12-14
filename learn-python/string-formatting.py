name = "John"
print("Hello, %s!" % name)
age = 23
print("%s is %d years old." % (name, age))
mylist = [1, 2, 3]
print("A list: %s" % mylist)
# %s - string (or objects with a string representation, like numbers)
# %d - integers
# %.<number of digits>f - floating point numbers with a fixed amount of digits to the right of the dot
# %x/%X - integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

name_data = ("Yolo", "Dolo")
money_data = 420.00
format_strings = "Hello %s and %s, you have $%s!"
print(format_strings % (name_data[0], name_data[1], money_data))
