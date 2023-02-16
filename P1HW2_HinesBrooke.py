# This program calculates and displays travel expenses
# 02-16-2023
# CTI-110 P1HW2 - Travel Expense
# Brooke Hines


print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter your budget: "))
print()
location = input("Enter your travel destination: ")
print()
fuel = float(input("How much do you thnk you will spend on gas: "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation: "))
print()
food = float(input("How much do you need for food: "))
print()
print("-"*12,"Travel Expenses",12*"-")
print("location: ", location)
print()
print("initial Budget: ", budget)
print()
print("fuel: ", fuel)
print()
print("accomodation: ", accomodation)
print()
print("food: ", food)
balance = budget - fuel - accomodation - food
print("Remaining Balanse: ", balance)
