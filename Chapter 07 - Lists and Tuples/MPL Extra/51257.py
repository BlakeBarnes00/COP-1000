# Create a list of odd numbers between 1 and n (including 1)
n = int(input("n: "))
odds = []

for i in range(1, n + 1):
	if (i % 2) == True:
		odds.append(i)

print(odds)