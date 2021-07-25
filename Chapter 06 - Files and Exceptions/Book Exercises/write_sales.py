# This program writes sales for a certain amount of days into a file

def main():
	# Get the number of days
	numDays = int(input("For how many days do you have sales? "))

	# Open a new file named sales.txt for writing
	salesFile = open("sales.txt", "w")

	# Now loop through the file for the amount of sales early inputted
	for count in range(1, numDays + 1):
		sales = int(input(f"Enter the sales for the day #{count}: "))
		salesFile.write(str(sales) + '\n')

	# Close the file
	salesFile.close()
	print("Data written to sales.txt")

main()