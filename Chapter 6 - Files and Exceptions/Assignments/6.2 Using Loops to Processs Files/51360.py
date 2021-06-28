file = open("numbers.txt", "r")
maxvalue = 0
runsum = 0

for number in file:
	if int(number) > maxvalue:
		maxvalue = int(number)
		runsum += int(number)
		
file.close()