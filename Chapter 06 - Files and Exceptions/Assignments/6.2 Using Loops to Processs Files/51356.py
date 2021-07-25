sum = 0

file = open('numbers.txt', 'r')

for line in file:
	sum += int(line)