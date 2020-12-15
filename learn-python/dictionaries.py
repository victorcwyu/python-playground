# similar to an array but works with keys and values instead of indexes
# each value stored can be accessed with a key, which is any type of object
phonebook = {}
phonebook["John"] = 222
phonebook["Jack"] = 234
phonebook["Jill"] = 345
print(phonebook)

# alternate notation
phonebook = {
    "John" : 123,
    "Jack" : 234,
    "Jill" : 345
}
print(phonebook)

# can be iterated over, like a list
# difference is that it does not keep the order of the values
phonebook = {
    "John" : 123,
    "Jack" : 234,
    "Jill" : 345
}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# removing a value
del phonebook["John"]
print(phonebook)
# or
phonebook.pop("Jill")
print(phonebook)