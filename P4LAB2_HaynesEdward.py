# Edward Haynes
# 3/19/2025
# P4LAB2
# Using a for loop inside a while loop to print math



# ceate variable to control while loop
run_again = "yes"


# while loop tthat controls the program 
while run_again != "no":
    # get it from user
    user_num = int(input ("Enter an integer: "))
    if user_num < 0:
        print("Negative numbers are not allowed")
    else: # user_num is 0 or greater
        for i in range(1,13):
            print(f"{user_num} * {i} = {user_num*i} ")
    run_again = input("Would you like to run again?  'yes'/'no': ")
    # while loop ends here
    print("End of program........")


