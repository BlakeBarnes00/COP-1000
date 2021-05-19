# Get the sum of squares up to the number of 50

# Initialized as 0
total = 0 

k = 1
while k <= 50:
    total += pow(k, 2)
    k += 1

print(total)