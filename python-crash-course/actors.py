actors = ["me", "you"]

roles = ["hero", "villain"]

featuring = []

for person in actors:
    match = person + " as " + roles[actors.index(person)]
    featuring.append(match)

print("Featuring:")
for actor in featuring:
    print(actor)