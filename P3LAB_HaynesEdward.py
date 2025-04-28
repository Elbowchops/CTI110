56#Edward Haynes
#3/3/2025
#P3LAB
#Use if statements to determine coin combination

#Get a float from the user and convert to interger
input_money = float(input("Enter the amout of money as a float: $"))

money = int(input_money * 100)

print(money)

#Calcualte number of whole dollars
num_dollars = money // 100
print(f"Num dollars: ${num_dollars}")

#Remove the dollars from the amount of money
money = money - (num_dollars * 100)

print(f"The remaining money is: {money}")




#Calcualte number of whole dollars
num_quarters = money // 25
print(f"Num quarters: {num_quarters}")

#Remove the dollars from the amount of money
money = money - (num_quarters * 25)

print(f"The remaining money is: {money}")




#Calcualte number of whole dollars
num_dimes = money // 10
print(f"Num dimes: {num_dimes}")

#Remove the dollars from the amount of money
money = money - (num_dimes * 10)

print(f"The remaining money is: {money}")




#Calcualte number of whole dollars
num_nickels = money // 5
print(f"Num Nickles: {num_nickels}")

#Remove the dollars from the amount of money
money = money - (num_nickels * 5)

print(f"The remaining money is: {money}")


num_pennies = money


#Display coins/dollars needed only if they are being used
#Ensure all grammar is correct
print()
print()
print()

print(f"{input_money:.2f}")


#No change is due, display "No Change"
if input_money <= 0.00:
    print("No Change")


#Display dollars
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

#Display quarters
if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

#Display dimes
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dimes")
    else:
        print(f"{num_dimes} Dimes")

#Display nickels
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickels")
    else:
        print(f"{num_nickels} Dollars")

#Display pennies
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")




