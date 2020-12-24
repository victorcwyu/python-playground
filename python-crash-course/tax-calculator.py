# Your task is to build an app that calculates how much tax someones owes.
#
# The app will:
#
# Ask the user to input a subtotal.
# Calculate the tax owed using some (hard-coded) tax rate. This can be whatever you want, like 0.25.
# Print out a message with the amount of tax owed.
# Print out another message with the total owed including tax.

subtotal = float(input("Please enter the subtotal: $"))
taxRate = 0.25
taxOwed = subtotal * taxRate
tax = "{:.2f}".format(taxOwed)
total = "{:.2f}".format(subtotal + taxOwed)
print("The tax owed is $" + tax)
print("The total owed is $" + total)