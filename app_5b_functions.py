# functions to be stored in a module to be reused in other scripts

def calculate_salary(hours_worked, hourly_rate):
    salary = hours_worked * hourly_rate
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        salary += overtime_pay
    return salary


def calculate_tax_band(salary):
    if salary > 2000:
        band = "Higher rate tax payer"
    elif salary > 1500:
        band = "Middle rate tax payer"
    else:
        band = "Lower rate tax payer"
    return band