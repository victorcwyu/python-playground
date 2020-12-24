# exercise:  build an app that takes a bill total, tip amount, and number of people as input; and outputs how much each person should pay.
#
# The app will:
#
# Ask for a total dollar amount
# Ask for the percentage tip
# Ask for the number of people splitting the bill
# Use those numbers to calculate the amount that each person owes, printing it out to the terminal, along with the overall total

subtotal = float(input("Please enter the subtotal: $"))
percentTip = float(input("Please enter the percentage tip: "))
people = float(input("Please enter the number of diners: "))
tip = subtotal * (percentTip / 100)
total = "{:.2f}".format(subtotal + tip)
person = "{:.2f}".format((subtotal + tip) / people)
print("The total owed is $" + total)
print("Each diner owes $" + person)
