# the notation n! represents the factorial of nonnegative integer n.
# The factorial of n is the product of the nonnegative integers from 
# 1 to n. For example: 
# 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040

def calculate(n):
	numbers = []
	total = 1 # Can't be zero because of multiplication
	
	for i in range(n + 1):
		if i != 0:
			# Storing just for visualization of all the numbers.
			numbers.append(i)
			total *= i
	
	print(numbers)
	return total

n = int(input("Enter a nonnegative integer:"))
print(calculate(n))