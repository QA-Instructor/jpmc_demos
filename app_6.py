# File IO

# import the calculate_salary function from app_5b_functions.py
# import a new function to calculate the tax band from app_5b_functions.py
from app_5b_functions import calculate_salary, calculate_tax_band

# read employee data from a file

with open('files/employees.txt', 'r') as f:
    employees = []
    for line in f:
        data = line.strip().split(',')
        employee = {
            "employeeID": data[0],
            "name": data[1],
            "department": data[2],
            "hours_worked": float(data[3]),
            "hourly_rate": float(data[4])
        }
        employees.append(employee)


for employee in employees:
    print('-----------------------------')
    print(f'Employee ID: {employee["employeeID"]} \nName: {employee["name"]} \nDepartment: {employee["department"]}\n')

    hours_worked, hourly_rate = employee["hours_worked"], employee["hourly_rate"]
    
    salary = round(calculate_salary(hours_worked, hourly_rate), 2)
    tax_band = calculate_tax_band(salary)   

    print(f"Weekly Salary: ${salary}")
    print(f"Tax Band: {tax_band}")