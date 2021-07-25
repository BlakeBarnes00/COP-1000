# This program displays property taxes

TAX_FACTOR = 0.0065 # Represents the tax factor

# Get the first lot number
print("Enter the property lot number \nor enter 0 to end.")
lot = int(input("Lot number: "))

# Continue processing as long as the user doesn't enter 0
while lot != 0:
	# Get the property value
	value = float(input("Enter property value: "))

	# Calculate the property tax
	tax = value * TAX_FACTOR
	
	# Display the tax
	print(f"Property tax: ${tax}")

	# Get the next lot number
	print("Enter the next lot number\n or enter 0 to end.")
	lot = int(input("Lot number: "))