# Use a for loop to compute the sum of squares up to 50
import math

total = 0

for k in range(51):
	total += math.pow(k, 2)

print(total)