file = open("numbers.txt", "r")

maxvalue = 0
for line in file:
	if maxvalue <= int(line):
		maxvalue = int(line)