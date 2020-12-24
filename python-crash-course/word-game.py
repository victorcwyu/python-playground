story = "Yesterday I ate FOOD before I went to play SPORT."
food = input("Please enter a food: ")
sport = input("Please enter a sport: ")
final = story.replace("FOOD", food).replace("SPORT", sport)
print(final)