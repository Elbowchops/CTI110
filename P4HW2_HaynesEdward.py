# Edward Haynes
# 3/26/2025
# P4HW2
# Calculate gross pay for multiple employees


'''
Pseudocode:

Get employee name from user (use input function)
Get employee hours worked form user (use input and float function)
Get employee pay rate from user (use input and float function)

# Overtime is worked (example)
regular_hours = 40
hours_worked = 0
pay_rate = 0
overtime_hours = 0
overtime_pay = 0
overtime_pay_rate = 1.5
regular_hour_pay = 0

Calculate value

# Overtime is worked (example)
if hours_work > 40
    Calculate OT hours (hours_work - 40)
    Calculate OT_pay_rate (pay_rate * 1.5)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to 40 (creat variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross pay (OT_pay + reg_pay)

    
# No overtime is worked (example)
else: 
    OT_hours is zero (hours_work - 0)
    OT_pay_rate is (OT_pay_rate = 0)(create a variable)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to hours_worked (create variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross pay (OT_pay + reg_pay)

    
# Display all values with width formatting (example)

print(f'{Hours Worked':>20}){Pay Rate':>20}")
print("----" * 20
print(f"{Hours Worked':>20}){Pay Rate':>20}2f")
'''

# create outer loop that runs until user inputs 'Done'

# create the accumlator variables
total_employees = 0
total_overtime_paid = 0
total_regular_hours_pay = 0
overtime_pay_rate = 1.5
total_gross = 0


# get name of employee
employee_name = input("Enter employee's name or Done to terminate: ")
while employee_name.lower() != 'done':

    # print("Loop is running" for printing statement)
    hours_worked= int(input(f"How many hours did {employee_name} work?: "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate?: $" ))

# if overtime worked
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * overtime_pay_rate
        regular_hours = 40
        regular_pay = regular_hours * pay_rate

# if no overtime worked
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_hours = hours_worked
        regular_pay = regular_hours * pay_rate

# gross pay
    gross_pay = regular_pay + overtime_pay

    # add to the accumulator variables
    total_employees += 1
    total_overtime_paid += overtime_pay
    total_regular_hours_pay += regular_pay
    total_gross += gross_pay

    print()
    print(f"Employee name: {employee_name:>5}")
    print()
    print(f"{'Hours Worked':<19}{'Pay Rate':<19}{'Overtime':<21}{'Overtime Pay':<23}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("----" * 30)
    print(f"{hours_worked:<19}{pay_rate:<19.2f}{overtime_hours:<21.2f}{overtime_pay:<23.2f}{regular_pay:<20.2f}{gross_pay:<20.2f}")
    print()
# input next employeer
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    print()

# loop ended, display final calculations
print(f"Total number of employees endered: {total_employees} ")
print(f"Total amount paid for overtime: ${total_overtime_paid:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_hours_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")

