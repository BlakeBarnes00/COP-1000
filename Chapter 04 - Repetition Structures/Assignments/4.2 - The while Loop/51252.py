# This program is to count the number of perfect squares whos value are less than h
import math

h = int(input("Enter number:"))

# Total amount of perfect squares
q = 0

# Create an array to store the perfect squares in
perfectSquares = []

i = 1
while i < h:
    r = int(math.sqrt(i))
    if i == math.pow(r, 2):
        perfectSquares.append(i)

    i += 1

q = len(perfectSquares)
print(f"Total amount of squares: {q} {perfectSquares}")