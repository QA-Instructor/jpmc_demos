# a collection of collections 
# e.g. a list of dictionaries

# import the calculate_salary function from app_5b_functions.py
# import a new function to calculate the tax band from app_5b_functions.py
from app_5b_functions import calculate_salary, calculate_tax_band

employees = [
    {
    "employeeID": "ID001",
    "name": "John Doe",
    "department": "Software Engineering"
},
    {
    "employeeID": "ID002", 
    "name": "Jane Smith",
    "department": "Marketing"
},
    {
    "employeeID": "ID003",
    "name": "Alice Johnson",
    "department": "Software Engineering"
}
]   

employee_hours_worked_and_rate = {
    "ID001": (37.5, 20.0),
    "ID002": (42.0, 25.0),
    "ID003": (40.0, 30.0)
}

for employee in employees:
    print(f'Employee ID: {employee["employeeID"]} \nName: {employee["name"]} \nDepartment: {employee["department"]}\n')

    hours_worked, hourly_rate = employee_hours_worked_and_rate[employee["employeeID"]]
    salary = round(calculate_salary(hours_worked, hourly_rate), 2)
    tax_band = calculate_tax_band(salary)
    
    print(f"Weekly Salary: ${salary}")
    print(f"Tax Band: {tax_band}")
    print('-----------------------------')
