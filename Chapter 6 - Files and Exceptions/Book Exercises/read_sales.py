# This program reads from the file sales.txt

def main():
	# Open the sales.txt file for reading only
	salesFile = open("sales.txt", "r")

	# Read the first line from the file, but dont convert to a number yet.
	# We still need to test for an empty string
	line = salesFile.readline()

	# As long as an empty line is not returned, continue processing

	while line != "":
		# Convert line to a int
		amount = int(line)

		# Format and display the amount
		print(amount)

		# Read the next line
		line = salesFile.readline()
	
	# Close the file
	salesFile.close()

main()