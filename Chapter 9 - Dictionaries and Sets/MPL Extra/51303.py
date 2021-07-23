d =  {1:2, 3:4, 5:6, 7:8}
not_found = set()
lst = [1, 6, 7]

for i in lst:
	print(i)
	if i in d:
		del d[i]
	else:
		not_found.add(i)


print(d)
print(not_found)