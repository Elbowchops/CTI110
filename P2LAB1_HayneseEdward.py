# Edward Haynes
# 2/17/2025
# P2LAB1
# Circle FOrmuala

import math

# Get radius form user as float
radius = float(input("What is the radius of the circle? "))
print()

# Calculate diameter
diameter = 2 * radius

# Calculate circumference
circumference = 2 * math.pi * radius

# Calculate area
area = math.pi * radius ** 2


# Display values to user
print(f"diameter of the circle is {diameter:.2f}")
print()
print(f"circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")