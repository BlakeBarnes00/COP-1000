list1 = [1 , 2, 3]
list2 = [4, 5, 6, 7, 8]
list3 = []

def main():
	max_count = 0

	if len(list1) < len(list2):
		max_count = len(list1)
	elif len(list1) > len(list2):
		max_count = len(list2)
	else:
		max_count = len(list1)
	
	for i in range(max_count):
		list3.append(list1[i])
		list3.append(list2[i])

	print(list3)

main()