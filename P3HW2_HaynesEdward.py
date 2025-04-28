# Edward Haynes
# 3/10/2025
# P3HW2
# Determine employee's regular pay, OT pay, and goss pay



'''
Pseudocode:

Get employee name from user (use input function)
Get employee hours worked form user (use input and float function)
Get employee pay rate from user (use input and float function)

Calculate value

# Overtime is worked
if hours_work > 40
    Calculate OT hours (hours_work - 40)
    Calculate OT_pay_rate (pay_rate * 1.5)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to 40 (creat variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross pay (OT_pay + reg_pay)

    
# No overtime is worked
else: 
    OT_hours is zero (hours_work - 0)
    OT_pay_rate is (OT_pay_rate = 0)(create a variable)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to hours_worked (create variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross pay (OT_pay + reg_pay)

    
Display all values with width formatting

print(f'{Hours Worked':>20}){Pay Rate':>20}")
print("----" * 20
print(f"{Hours Worked':>20}){Pay Rate':>20}2f")

'''

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter the number of hours the employee worked this week: "))
pay_rate = float(input("Enter the employee's pay rate per hour: "))


# Overtime is worked
OT_hours = 0
regular_hours = 40
OT_pay_rate = 1.5
regular_pay = 0


'''
# No overtime worked
OT_hours = 0
OT_pay_rate = 1.5
regular_hours = 0
regular_pay = 0
'''

if hours_worked > 40:
    OT_hours = hours_worked - 40
    regular_hours = 40
else:
    regular_hours = hours_worked

# Total pay
regular_pay = regular_hours * pay_rate
OT_pay = OT_hours * (pay_rate * OT_pay_rate)

# Gross pay
gross_pay = regular_pay + OT_pay


print("----" * 20)
print()
print(f"Employee Name: {employee_name}")
print(f"{'Hours Worked'}{'Pay Rate':>19}{'Overtime':>21}{'Overtime Pay':>23}{'Regular Pay':>20}{'Gross Pay':>20}")
print("----" * 30)

print(f"{hours_worked}{pay_rate:>25}{OT_hours:>18}{OT_pay:>21}{regular_pay:>21}{gross_pay:>23}")