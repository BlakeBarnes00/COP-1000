my_list = [1, 2, 3, 4, 5, 6]
new_list = []

for i in range(0, len(my_list)):
	if my_list[i] % 2 == 0:
		new_list.append(my_list[i])

print(my_list)
print(new_list)