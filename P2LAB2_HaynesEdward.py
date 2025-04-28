#Edward Haynes
#2/23/2025
#P2LAB2
#Using Dictionaries

cars = {'Lamborghini':10, 'Ferrari':8.77, 'Jaguar':20, 'Aston Martin':10.1}

#Get keys from the dictionaries
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

#Get a car from user
car_name = input("Enter a car: ")

#Get mpg for the given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculation
gallons_needed = miles_driven/car_mpg

#Display results
print(f"{gallons_needed:.2f} gallon(s) of gas is needed to drive the {car_name} {miles_driven} miles")

