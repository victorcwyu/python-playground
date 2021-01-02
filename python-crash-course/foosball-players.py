foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

# get the median player
median = len(foosballers) // 2
medianPlayer = foosballers[median]
print(medianPlayer)

# get the five players in the middle
low = median - 2
high = median + 3
middlePlayers = foosballers[low : high]
print(middlePlayers)

# add a fake player, called "Average Player," to the exact middle of the list
foosballers.insert(9, "Average Player")
print(foosballers)

# find "Average Player," and change their name to uppercase: "AVERAGE PLAYER."

foosballers[9] = "AVERAGE PLAYER"
print(foosballers)

# add five more players with names of your choosing, to the bottom of the list
newbies = ["Jolo", "Solo", "Dolo", "Yolo", "Lolo"]
foosballers = foosballers + newbies
print(foosballers)

# "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this.
del foosballers[9]
median = len(foosballers) // 2
foosballers[median - 1] = "AVERAGE PLAYER"
print(foosballers)

# insert at the appropriate location:
# Lacy is one spot ahead of Hubert
foosballers[foosballers.index("Hubert") - 1] = "Lacy"
print(foosballers)
# Omar is one spot behind Rebecca
foosballers[foosballers.index("Rebecca") + 1] = "Omar"
print(foosballers)
# Otto is 8th best in the league
foosballers[7] = "Otto"
print(foosballers)
# Chauncey is 10 spots from the bottom of the league
foosballers[-11] = "Chauncey"
print(foosballers)


