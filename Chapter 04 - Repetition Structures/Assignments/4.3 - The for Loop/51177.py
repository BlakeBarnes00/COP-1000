# Compute the sum of cubes up to n
import math

total = 0

n = int(input("Enter a number:"))
for k in range(n+1):
	total += int(math.pow(k, 3))

print(total)