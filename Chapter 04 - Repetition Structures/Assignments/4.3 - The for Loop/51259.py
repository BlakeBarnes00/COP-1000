# Average the numbers from 1 to n

n = int(input("Enter number:"))
avg = 0
for i in range(n + 1):
	avg += i

avg = avg/n
print(avg)