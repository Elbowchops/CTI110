# Edward Haynes
# 223/2025
# P2HW1
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
print(f"{'Destination: ':<20}  {destination}")
print(f"{'Budget: ': <21} ${budget:.2f}")
print(f"{'Travel: ': <21} ${travel:.2f}")
print(f"{'Lodging: ': <21} ${lodging:.2f}")
print(f"{'Food: ': <21} ${food:.2f}") 

print("----------------------------------------")

print(f"{'Remaining Budget: ': <21} ${remaining_budget:.2f}")