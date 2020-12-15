# a module is a piece of software that has a specific functionality
# each module is a different file which can be edited separately

# Python modules are simply Python files with a .py extension

# .pyc files are Python files compiled into Python bytecode
# this avoids having to parse the files each time modules are loaded
# if a .pyc file exists, it gets loaded instead

# importing modules
# ex. import module

# importing module objects to the current namespace
# ex. from module import function
# the import command may replace an existing object in the namespace

# importing all objects from a module
# ex. from module import *
# a bit risky as changes in the module might affect the module which imports it,
# but it is shorter and also does not require you to specify which objects you wish to import from the module

# custom import name
# ex. import function as custom_name

# module initialization
# the first time a module is loaded into a running python script,
# it is initialized by executing the code in the module once,
# and only once

# extending module load path
# ex. use the environment variable PYTHONPATH to specify additional directories to look for modules in:
# PYTHONPATH=/foo python game.py
# enables the script to load modules from the foo directory as well as the local directory
# ex. use the sys.path.append function
# sys.path.append("/foo")
# execute it before running an import command

# exploring built-in modules
# two important ones: dir, help
# dir looks for which functions are implemented in each module
# ex. dir(module)
# help provides info about the function in he module
# ex. help(module.function)

# writing packages
# packages are namespaces which contain multiple packages and modules themselves
# they are simply directories, with a twist
# must contain a file called __init__.py, can be empty
# indicates that it is a Python package so it can be imported like a module
# __init__.py can can also decide which modules the package exports as the API,
# while keeping other modules internal, by overriding the __all__ variable
# example:
# __init__.py:
# __all__ = ["bar"]

# exercise: print an alphabetically sorted list of all functions in the re module,
# which contain the word find

import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))