#Edward Haynes
#2/23/2025
#P2HW2
#Use list to capture grades


#Ask the user to enter the 6 modules - they should be floats
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))


#Create 'empty' list
grades_list = []
#Another way: grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]

#Use the append method to add all grades on the list
#Append method: list_name.append(information thats need)

grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
grades_list.append(grade6)
print()
#Display results
print(grades_list)
print()

#Display values to user
print("-----------------Results---------------------")
print(f"{'Lowest Grade:': <20} {min(grades_list)}")
print(f"{'Highest Grade:': <20} {max(grades_list)}")
print(f"{'Sum of Grade:': <20} {sum(grades_list)}")
average = sum(grades_list) / len(grades_list)
print(f"{'Average:': <20} {average:.2f}")
print("---------------------------------------------")