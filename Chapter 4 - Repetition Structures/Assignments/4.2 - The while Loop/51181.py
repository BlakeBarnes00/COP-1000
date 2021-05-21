# sum of cubes to the first n counting numbers
total = 0

n = int(input("Enter number:"))
k = 0
while k <= n:
    total += pow(k, 3)
    k += 1

print(total)
