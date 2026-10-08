# Collections

# Change the individual variables to be a dictionary


# employeeID = "ID001"
# name = "John Doe"
# dept = "Software Engineering"

employee = {
    "employeeID": "ID001",
    "name": "John Doe",
    "department": "Software Engineering"
}


hours_worked = 37.5
hourly_rate = 18.74


print(f'Employee ID: {employee["employeeID"]} \nName: {employee["name"]} \nDepartment: {employee["department"]}')

def calculate_salary(hours_worked, hourly_rate):
    salary = hours_worked * hourly_rate
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        salary += overtime_pay
    return salary



salary = calculate_salary(hours_worked, hourly_rate)
print(f'Weekly Salary: ${round(salary, 2)}') # round to


if salary > 2000:
    print("Higher rate tax payer")
elif salary > 1500:
    print("Middle rate tax payer")
else:
    print("Lower rate tax payer")


