# This program calculates retail prices

MARK_UP = 2.5 # The markup percentage
another = 'y' # Variable to control the loop

# Process one or more items
while another == 'y' or another == 'Y':
	# Get the items wholesale cost
	wholesale = float(input("Enter the item's wholesale cost: "))

	# Validate the wholesale cost here
	while wholesale < 0:
		print("ERROR: the cost cannot be negative.")
		wholesale = float(input("Enter the item's wholesale cost: "))
	
	# Calculate the retail price
	retail = wholesale * MARK_UP
	
	# Display the retail price
	print(f"Retail price: ${retail}".format(retail, '.2f'), sep='')

	# Do it again?
	another = input("Do you have another item? (Enter y for yes): ")