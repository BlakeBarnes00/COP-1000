def mymin(str1, str2):
	if ord(str1[0]) < ord(str2[0]):
		return str1
	elif ord(str1[0]) > ord(str2[0]):
		return str2


print(ord("large"[0]))
print(ord("small"[0]))

print(mymin("large", "small"))