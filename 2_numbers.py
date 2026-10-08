# operators
number1 = 10
number2 = 5

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)   

# exponentiation
print("Exponentiation:", number1 ** number2)  # 10 raised to the power of 5
print("Exponentiation:", number2 ** 2)  # 5 raised to the power of 3    
print("Floor Division:", number1 // number2)  # quotient of division
print("Floor Division:", 11 // number2)  # quotient of division (no remainder)
print("Modulus:", number1 % number2)  # remainder of division
print("Modulus:", 11 % number2)  # remainder of division

# numeric functions
print("Absolute Value:", abs(-10))
print("Maximum:", max(number1, number2))
print("Minimum:", min(number1, number2))

test_scores = [88, 92, 79, 95, 85]
print("Sum of Test Scores:", sum(test_scores))
print("Average of Test Scores:", sum(test_scores) / len(test_scores))

print("Maximum test score:", max(test_scores))
print("Minimum test score:", min(test_scores))

# input function
user_input = input("Enter a number: ")  
print("You entered:", user_input)

doubled_value = user_input * 2
# doubled_value = int(user_input) * 2
print("Doubled value:", doubled_value)

# can convert at point of entry
user_input = int(input("Enter another number: "))
print("You entered:", user_input, "and its type is", type(user_input))
print("Doubled value:", user_input)