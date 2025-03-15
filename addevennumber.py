# Function to generate even numbers up to a given limit
def generate_even_numbers(limit):
    even_numbers = []
    for num in range(2, limit + 1, 2):
        even_numbers.append(num)
    return even_numbers

# Example usage
limit = 613
even_numbers = generate_even_numbers(limit)
print(f"Even numbers up to {limit}: {even_numbers}")
