file = open("BoyNames.txt", "r")
data = file.read()
boys_names = data.split('\n')

file = open("GirlNames.txt", "r")
data = file.read()
girls_names = data.split('\n')
file.close()


choice = input("Enter 'boy', 'girl', or 'both':")
if choice == "boy":
	name = input("Enter a boy's name:")
	if name in boys_names:
		print(f"{name} was a popular boy's name between 2000 and 2009.")
	else:
		print(f"{name} was not a popular boy's name between 2000 and 2009.")

elif choice == "girl":
	name = input("Enter a girl's name:")
	if name in girls_names:
		print(f"{name} was a popular girl's name between 2000 and 2009.")
	else:
		print(f"{name} was not a popular girl's name between 2000 and 2009.")

elif choice == "both":
	bname = input("Enter a boy's name:")
	if bname in boys_names:
		print(f"{bname} was a popular boy's name between 2000 and 2009.")
	else:
		print(f"{bname} was not a popular boy's name between 2000 and 2009.")
	
	gname = input("Enter a girl's name:")
	if gname in girls_names:
		print(f"{gname} was a popular girl's name between 2000 and 2009.")
	else:
		print(f"{gname} was not a popular girl's name between 2000 and 2009.")
