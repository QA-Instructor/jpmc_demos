# Lists
employees = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]

print("Employee List:")
print(employees)

# print an individual employee
print(employees[0])
print(employees[3])

# lists are mutable, we can change the value of an item in the list
employees[3] = "Millie Bobby Brown"

print("Amended Employee List:")
print(employees)

# Append a new employee to the list
employees.append("Noah Schnapp")

print("Updated Employee List:")
print(employees)

# Tuples
# Tuples are immutable, we cannot change the value of an item in the tuple

employees_tuple = ("John Doe", "Jane Smith", "Alice Johnson", "Bob Brown")

print("Employee Tuple:")
print(employees_tuple)

# print an individual employee
print(employees_tuple[0])
print(employees_tuple[3])

# attempting to change the value of an item in the tuple will result in an error
# employees_tuple[3] = "Millie Bobby Brown" # this will result in an error

# Dictionaries
employee = {
    "employeeID": "ID001",
    "name": "John Doe",
    "department": "Engineering"
}

print("Employee Dictionary:")
print(employee)

# print an individual value from the dictionary
print(employee["name"])
print(employee["department"])   

# amending a value in the dictionary
employee["department"] = "Software Engineering"

print("Amended Employee Dictionary:")
print(employee)