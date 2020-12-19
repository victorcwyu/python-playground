# sets are lists with no duplicate entries
# print(set("my name is Eric and Eric is my name".split()))

# sets have the ability to calculate differences/intersections between other sets
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)
# attended both events
print(a.intersection(b))
print(b.intersection(a))
# attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
# attended one event and not the other
print(a.difference(b))
print(b.difference(a))
# list of all participants
print(a.union(b))

# exercise: use the given lists to print out a set containing
# all the participants from event A which did not attend event B
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))