# Functions

employeeID = "ID001"
name = "John Doe"
dept = "Software Engineering"

# print(f'Employee ID: {employeeID} \nName: {name} \nDepartment: {dept}')

# ========================================================================
# Part 2 - add salary information and print it out

hours_worked = 37.5
hourly_rate = 18.74
# salary = hours_worked * hourly_rate

print(f'Employee ID: {employeeID} \nName: {name} \nDepartment: {dept}')
# print(f'Weekly Salary: ${round(salary, 2)}') # round to 2 decimal places

# ######################################## Step 4 FUNCTIONS ########################################

def calculate_salary(hours_worked, hourly_rate):
    salary = hours_worked * hourly_rate
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        salary += overtime_pay
    return salary



salary = calculate_salary(hours_worked, hourly_rate)
print(f'Weekly Salary: ${round(salary, 2)}') # round to

# ========================================================================
# Part 3 - add conditional statements re tax rate

if salary > 2000:
    print("Higher rate tax payer")
elif salary > 1500:
    print("Middle rate tax payer")
else:
    print("Lower rate tax payer")

# ========================================================================
# Part 4 - functions

# def calculate_salary(hours_worked, hourly_rate):
#     salary = hours_worked * hourly_rate
#     if hours_worked > 40:
#         overtime_hours = hours_worked - 40
#         overtime_pay = overtime_hours * hourly_rate * 1.5
#         salary += overtime_pay
#     return salary

# added into STEP 2
