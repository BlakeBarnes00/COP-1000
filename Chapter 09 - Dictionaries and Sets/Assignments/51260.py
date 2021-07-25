# Dictionary that maps first n counting numbers and their squares
import math

n = int(input("n: "))

squares = {}

for k in range(1, n + 1):
	squares[k] = pow(k, 2)

print(squares)