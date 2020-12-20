# Python 2.5 = simplejson
# Python 2.7 = json

# 2 basic formats for JSON data: string/object
# objects in Python consist of lists/dictionaries nested inside each other

# objects allow one to use python methods
# (for lists and dictionaries) to add, list, search and
# remove elements from the datastructure

# string format is mainly used to pass the data into
# another program or load into a datastructure

# the loads method takes a string and turns it back into
# the json object datastructure
import json
json_string = '{"yolo": 1}'
print(json.loads(json_string))

# the "dumps" method takes an object and returns a string
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

# Python supports a Python proprietary data serialization method
# called pickle (and a faster alternative called cPickle, used the same way)
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# exercise: print out the JSON string with key-value pair "Me" : 800 added to it
# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])