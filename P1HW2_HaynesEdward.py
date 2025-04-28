# Edward Haynes
# 2/16/2025
# P1HW2
# Travel Expenses


# Ask the user their budget
budget = float(input("Enter budget: $"))

# Ask user to enter travel destination
destination = (input("Enter your travel destination: "))

# Ask user for amount they will spend on gas
travel = float(input("How much do you expect to pay for travel? $"))

# Ask user for amount they will spend on hotel/lodging
lodging = float(input("Approximately, how much will you need for hotel/lodging? $"))

# Ask user for amount they will spend on food
food = float(input("How much will you need for food? $"))

# Add expenses
expenses = travel + lodging + food

# Subtract expenses for budget
remaining_budget = budget - expenses

# Display travel expenses
remaining_budget = budget - expenses

print()
print("-----Travel Expensess for Euro Trip-----")
print("Destination: ", destination)
print("Budget: $", budget)
print("Travel: $", travel)
print("Lodging: $", lodging)
print("Food: $", food) 

print("Remaining Budget: $", remaining_budget)
