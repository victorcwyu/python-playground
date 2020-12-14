mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
# loop through list and print each element/item
for x in mylist:
    print(x)
# add numbers and strings using .append
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
second_name = names[1]
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)