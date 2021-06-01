from Shapes import Shapes 

# Create Shapes object
myObj = Shapes()

while True:
	myObj.printShapeList()
	
	choice = ''
	choice = input("Type the name or the index of the shape that you want to see: ")
	
	if choice == "exit" or choice == "0":
		print("Exiting....")
		break
	
	elif choice == "Square" or choice == "1":
		myObj.square()

	elif choice == "Rectangle" or choice == "2":
		myObj.recangle()

	elif choice == "Right Triangle" or choice == "3":
		myObj.rightTriangle()
	
	elif choice == "Custom Triangle" or choice == "4":
		myObj.customTriangle()

	else:
		print("ERROR: Input not valid.")