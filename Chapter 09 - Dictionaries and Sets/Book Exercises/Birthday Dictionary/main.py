# Program that creates a dictionary of birthdays
import birthdays as b
# Global constants for choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
SHOW_ALL = 5
QUIT = 6


def main():
	birthdays = {}

	choice = 0
	while choice != QUIT:
		choice = getMenuChoices()
		if choice == LOOK_UP:
			b.lookUpBirthday(birthdays)
		elif choice == ADD:
			b.addBirthday(birthdays)
		elif choice == CHANGE:
			b.changeBirthday(birthdays)
		elif choice == DELETE:
			b.deleteBirthday(birthdays)
		elif choice == SHOW_ALL:
			b.showAllBirthdays(birthdays)

def getMenuChoices():
	print()
	print("------------------------")
	print("1. Look up a birthday.")
	print("2. Add a new birthday.")
	print("3. Change a birthday.")
	print("4. Delete a birthday.")
	print("5. Show all birthdays.")
	print("6. Quit the program.")
	print("------------------------")
	print()

	# Get the input from the user
	choice = int(input("Enter your choice: "))

	while choice < LOOK_UP or choice > QUIT:
		choice = int(input("Enter a valid choice: "))
	
	return choice

main()