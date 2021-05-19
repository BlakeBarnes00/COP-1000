# Sum of perfect squares up to h
import math

h = int(input("Enter a number:"))

q = 0
i = 0
while i < h:
    root = int(math.sqrt(i))
    if i == math.pow(root, 2):
        q += i

    i += 1

print(q)