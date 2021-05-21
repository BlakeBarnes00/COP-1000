# Use an arithmetic to sum up all the values to 'n'
n = int(input("Enter a number:"))
distance = int(input("Enter disance:"))
sum = 0
numbers = []

for i in range(1, n+1, distance):
	numbers.append(i)
	sum += i

print(numbers)
print(f"Total: {sum}")