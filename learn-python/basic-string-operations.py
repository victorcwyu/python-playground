astring = "Hello world!"
# length
print(len(astring))
# first occurrence
print(astring.index("o"))
# number of character occurrences
print(astring.count("l"))
# slice of string
print(astring[3:7])
# slice of string from start to n-1
print(astring[:7])
# character at that index
print(astring[3])
# slice of string from that index to the end
print(astring[7:])
# slice of string from n characters from the end to the end
print(astring[-3:])
# character at that index (from the end
print(astring[-3])
# slice of string from start to n characters from the end
print(astring[:-7])
# following 2 are the same (start at 0, end at 7, skip one character)
print(astring[0:7])
print(astring[0:7:1])
# [start:stop:step]
print(astring[0:7:2])
# reverse a string
print(astring[::-1])
# convert to uppercase
print(astring.upper())
# convert to lowercase
print(astring.lower())
# string starts with x
print(astring.startswith("Hello"))
# string ends with x
print(astring.endswith("asdfasdfasdf"))
# split string into a bunch of strings grouped together in a list
afewwords = astring.split(" ")
print(afewwords)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))