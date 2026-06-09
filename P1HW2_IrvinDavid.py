# David Irvin
# 06/09/2026
# P1HW2
# Calculating travel expenses

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses
print("------------Travel Expenses------------")
print("Location: ", destination)
print("Initial Budget: ", format(budget))
print()
print("Fuel: ", format(gas))
print("Accommodation: ", format(accommodation))
print("Food: ", format(food))
print()
print("Remaining Balance: ", format(remaining_budget))
