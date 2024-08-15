# List to store the numbers that meet the criteria
result = []

# Iterate over the range from 0 to 100
for num in range(101):
    # Check if the number is odd and divisible by 3, 5, and 15
    if num % 2 != 0 and num % 3 == 0 and num % 5 == 0 and num % 15 == 0:
        result.append(num)

# Print the result
print("Odd numbers between 0 and 100 divisible by 3, 5, and 15:", result)

