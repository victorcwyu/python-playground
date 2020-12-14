number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# concatenation
helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_nums = [2, 4, 6, 8]
odd_nums = [1, 3, 5, 7]
all_nums = odd_nums + even_nums
print(all_nums)

print([1, 2, 3] * 3)

# create x_list and y_list which contain 10 instances of x/y
# concatenate the 2 lists
x = object()
y = object()
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))
# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")