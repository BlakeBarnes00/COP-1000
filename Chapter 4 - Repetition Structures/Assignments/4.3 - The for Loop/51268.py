# Determine if the element of the lists are ascending

numbers = []
is_ascending = False

for i in numbers:
	print(i)
	if i >= numbers.index(i) + 1:
		is_ascending = True
	elif i < numbers.index(i) + 1 or len(numbers) == 0:
		is_ascending = False

print(f"{numbers} {is_ascending=}")
