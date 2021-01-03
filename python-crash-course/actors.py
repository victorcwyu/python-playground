actors = ["me", "you"]

roles = ["hero", "villain"]

featuring = []

for index, person in enumerate(actors):
    match = person + " as " + roles[index]
    featuring.append(match)

print("Featuring: \n=_=_=_=_=_=_=_=")
for actor in featuring:
    print(actor)