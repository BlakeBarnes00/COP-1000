# Create a list of odd numbers between m and n (including m)
m = int(input("m: "))
n = int(input("n: "))
odds = []

for i in range(m, n + 1):
	if (i % 2) == True:
		odds.append(i)

print(odds)