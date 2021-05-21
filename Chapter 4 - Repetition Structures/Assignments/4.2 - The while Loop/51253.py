# This program will find the perfect sqaures between k and m
import math

k = 10
m = 40

# Total amount of perfect squares between k and m
q = 0

perfectSquares = []

i = k
while i < m:
    r = int(math.sqrt(i))
    if i == math.pow(r, 2):
        perfectSquares.append(i)
    
    i += 1

q = len(perfectSquares)
print(f"Total amount of squares:{q}, {perfectSquares}")