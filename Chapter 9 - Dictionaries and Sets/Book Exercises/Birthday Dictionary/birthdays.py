def lookUpBirthday(birthdayDict):
	# Get a name to look up
	name = input("Enter a name: ")

	# Print the date, if not found print not found.
	print(birthdayDict.get(name, "Not Found."))

def addBirthday(birthdayDict):
	name = input("Enter name: ")
	date = input("Enter date: ")

	if name not in birthdayDict:
		birthdayDict[name] = date
	else:
		print("That entry already exists.")

def changeBirthday(birthdayDict):
	name = input("Enter name: ")

	if name in birthdayDict:
		birthdayDict[name] = input("Enter new date")
	else:
		print("That name does not exist.")

def deleteBirthday(birthdayDict):
	name = input("Enter name: ")

	if name in birthdayDict:
		del birthdayDict[name]
	else:
		print("That name does not exist.")

def showAllBirthdays(birthdayDict):
	print(birthdayDict)