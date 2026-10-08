# create a weekly payroll file and include a datestamp in the file name
from datetime import date
current_date = date.today()
# Modules and writing out a file with a datestamp in the file name

# import the calculate_salary function from app_5b_functions.py
# import a new function to calculate the tax band from app_5b_functions.py
from app_5b_functions import calculate_salary, calculate_tax_band

# read employee data from a file

# Instead of printing to the console, we will write the output to a new file with a datestamp in the file name

# Open 2 files, one with source data, one as a destination file to write the output to
with ( 
    open('files/employees.txt', 'r') as f,
    open(f'files/payroll_{current_date:%Y-%m-%d}.txt', 'w') as payroll_file):
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

        hours_worked, hourly_rate = employee["hours_worked"], employee["hourly_rate"]
        salary = round(calculate_salary(hours_worked, hourly_rate), 2)
        tax_band = calculate_tax_band(salary)  

        payroll_file.write('-----------------------------\n')   
        payroll_file.write(f'Employee ID: {employee["employeeID"]} \nName: {employee["name"]} \nDepartment: {employee["department"]}\n')
        payroll_file.write(f"Weekly Salary: ${salary}\n")
        payroll_file.write(f"Tax Band: {tax_band}\n")



