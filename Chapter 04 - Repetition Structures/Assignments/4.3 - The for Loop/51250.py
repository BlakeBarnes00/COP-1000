# Compute the sum of perfect sqaures up to h

import math

h = int(input("Enter number:"))
q = 0
perfectSquares = []

for i in range(1, h+1):
	perfectSquares.append(i)
	q += int(math.pow(i, 2))

print(perfectSquares)
print(f"Sum: {q}")