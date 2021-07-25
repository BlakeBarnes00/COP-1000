file1 = open("data1.txt", "r")
file2 = open("data2.txt", "w")

for line in file1:
	file2.write(line)