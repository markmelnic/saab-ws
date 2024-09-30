def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Example usage
numbers = []
average = calculate_average(numbers)
if average is not None:
    print(f"The average is: {average}")
else:
    print("Cannot calculate average of an empty list.")
