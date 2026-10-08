# print("Hello, World!")

print('Employee Report Generator')

firstname = 'Victoria'
lucky_number = 13
is_british = False

print('Employee Name:', firstname)
print('Lucky Number:', lucky_number)
print('Is British:', is_british)

print(f'Firstname: {firstname}, Lucky Number: {lucky_number}, Is British: {is_british}')

print(type(firstname))
print(type(lucky_number))
print(type(is_british))

height = 168.9
print(type(height))

rounded_height = round(height)
print(f'Height: {height}, Rounded Height: {rounded_height}')
print(type(rounded_height))

# reassigning a value, changing the value of height to an integer
height = round(height)
# f strings
print(f'Height: {height}, Rounded Height: {rounded_height}')

# new lines
print(f'Firstname: {firstname}\nLucky Number: {lucky_number}\nIs British: {is_british}')

# shouting the name in uppercase
print(firstname.upper())

employee_2_firstname = 'john'
print(employee_2_firstname.upper())
print(employee_2_firstname.title())

employee_2_lastname = 'Smith'

employee2_username = employee_2_firstname.lower() + '.' + employee_2_lastname.lower()
print(employee2_username)

# if is_british:
#     print(f'{firstname} is British.')
# else:
#     print(f'{firstname} is not British.')