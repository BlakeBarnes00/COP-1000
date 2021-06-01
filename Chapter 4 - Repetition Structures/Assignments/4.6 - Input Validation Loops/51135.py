# Program that continually checks to see if the correct ID is 
# entered through the input, if not an error will come out.

id = 337788
card = int()

while card != id:
	card = int(input("Enter your ID: "))
	
	if card == id:
		print(f"This is your ID number: {id}")
		break
	
	else:	
		print("This is not your ID number.")
