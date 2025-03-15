def add_even_numbers(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return num1 + num2
    else:
        return "Both numbers must be even."

# Example usage
number1 = 4
number2 = 6
result = add_even_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {result}")
