file1 = open("data1.txt", "r")
file2 = open("dataplus.txt", "w")
file3 = open("dataminus.txt", "w")

for line in file1:
	line = int(line.strip())
	if line > 0:
		file2.write(str(line) + "\n")
	elif line < 0:
		file3.write(str(line) + "\n")