# creates a new list based on another list, in a single, readable line

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
# print(words)
# print(word_lengths)

# using a list comprehension
word_lengths = [len(word) for word in words if word != "the"]
# print(word_lengths)

# exercise: Using a list comprehension, create a new list called "newlist"
# out of the list "numbers", which contains only the positive numbers from
# the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]
print(newlist)