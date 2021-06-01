import os # For the clear function from windows
from Shapes import Shapes 

# Create Shapes object
shapes = Shapes()

while True:
	shapes.printShapeList()
	
	choice = ''
	choice = input("Type the name or the index of the shape that you want to see: ")

	if choice == "exit":
		os.system("cls")
		print("Exiting....")
		break
	
	elif choice == "Square" or choice == "0":
		os.system("cls")
		shapes.square()

	elif choice == "Rectangle" or choice == "1":
		os.system("cls")
		shapes.recangle()

	elif choice == "Right Triangle" or choice == "2":
		os.system("cls")
		shapes.rightTriangle()
	
	elif choice == "Custom Triangle" or choice == "3":
		os.system("cls")
		shapes.customTriangle()

	elif choice == "Circle" or choice == "4":
		os.system("cls")
		shapes.circle()

	else:
		os.system("cls")
		print(f"ERROR: '{choice}'' is not valid for input here.")