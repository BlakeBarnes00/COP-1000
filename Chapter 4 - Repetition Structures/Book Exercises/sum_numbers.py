# This program calculates the sum of a series 
# of numbers entered by the user.

MAX = 5

# Initialize the accumulator to 0
total = 0.0

# Explain what the program is doing
print(f"This program calculates the sum of {MAX} numbers you will enter.")

# Get the input from the user
for counter in range(MAX):
	number = int(input("Enter a number: "))
	total += number

print(f"The total of your numbers is: {total}")