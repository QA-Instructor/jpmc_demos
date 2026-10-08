# numbers

employeeID = "ID001"
name = "John Doe"
dept = "Software Engineering"

print(f'Employee ID: {employeeID} \nName: {name} \nDepartment: {dept}')

# ========================================================================
# Part 2 - add salary information and print it out

hours_worked = 37.5
hourly_rate = 18.74
salary = hours_worked * hourly_rate

print(f'Employee ID: {employeeID} \nName: {name} \nDepartment: {dept}')
print(f'Weekly Salary: ${salary}') # needs rounding
print(f'Weekly Salary: ${round(salary, 2)}') # round to 2 decimal places