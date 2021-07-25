# Fibonacci numbers are a sequence of integers, starting with 1,
# where the value of each number is the sum of the two previous
# numbers. Write a function that takes the parameter n that contains
# an integer value, and have it return the nth Fib number.

# First few fib numbers are as follows: 0 1 1 2 3 5 8 13
# The index starts as 0 at 0
# So 0 = 0 | 1st = 1 | 2nd = 1 | 3rd = 2 | 4th = 3 | 5th = 5 | 6th = 8 | and so on forever.
def fibonacci(n):
	if n < 0:
		print("Incorrect input.")
	
	# The first fib number is 0
	elif n == 0:
		return 0

	# The second fib number is 1
	elif n == 1:
		return 1

	# Use recursion to subtract the previous two numbers
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))