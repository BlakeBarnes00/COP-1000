total = 0
line_count = 0

file = open("numbers.txt", "r")
curr_line = file.readline()
while curr_line != "":
	line_count += 1
	total += int(curr_line)
	curr_line = file.readline()
file.close()

average = total/line_count
print(average)