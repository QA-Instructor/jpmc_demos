# define a function

def say_hello():
    print("Hello!")

# call a function

say_hello()

# function with parameters
def greet_user(name):
    print(f'Hello, {name}!')

greet_user("Alice") 
greet_user("Bob")


# afunction that doesn't get called
def unused_function():
    print("This function is not called.")


# function with parameters and return value
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# call the function and pass in the arguments, then print the result
result = calculate_rectangle_area(10, 5)
print(f'Area of the rectangle: {result}')

result = calculate_rectangle_area(3, 4)
print(f'Area of the rectangle: {result}')