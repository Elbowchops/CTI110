# Edward Haynes
# 3/26/2025
# P4HW1
# Capture Grades


# Number of scores from user

num_score = int(input("Enter the number of scores: "))

# Creat empty score list
score_list = []



# Loop to get all scores
for each in range(num_score):
    score = float(input(f"Enter score # {each + 1}: "))

# Validate scores
    while score < 0 or score > 100:
        if score <= 0 or score > 100:
            print("This score is invalid!!!")
            print("Score must be between 0 and 100.")
        score = float(input(f"Enter score # {each + 1} again: "))
    score_list.append(score)


print()
print()


# Display scores to user
print("-----------------Results---------------------")
lowest_score = min(score_list)
print(f"{'Lowest Score   :': <18} {min(score_list)}")

# Remove lowest score
score_list.remove(lowest_score)

print(f"{'Modified List  :' : <18} {score_list}")
average = sum(score_list) / len(score_list)
print(f"{'Scores Average :': <18} {average:.2f}")


# Use average to determine letter grade

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"{'Grade          :': <18} {grade}")

print("---------------------------------------------")

