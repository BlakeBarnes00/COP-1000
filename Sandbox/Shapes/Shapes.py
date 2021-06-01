# Class that holds all the shapes and nested loops I have made.
import math

class Shapes:
	shapedict = {
		0 : "Square", 
		1 : "Rectangle", 
		2 : "Right Triangle", 
		3 : "Custom Triangle", 
		4 : "Circle",
	}

	def printShapeList(self):
		# Used to help keep length even between divs
		dividerLength = 35 
		for r in range(1):
			for c in range(dividerLength):
				print('=', end='')
			print()
		
		# The actual menu choiceis printed here.
		for i in range(len(self.shapedict)):
			print(f"{i} | {self.shapedict[i]}")

		# another divider
		for r in range(1):
			for c in range(dividerLength):
				print('=', end='')
			print()

	def square(self):
		rows = int(input("How big do you want the square? "))

		for r in range(rows):
			for c in range(rows):
				print('*', end=' ')
			print()
	
	def rectangle(self):
		rows = int(input("How many rows do you want? "))
		cols = int(input("How many columns do you want? "))
		
		for r in range(rows):
			for c in range(cols):
				print('*', end=' ')
			print()

	def rightTriangle(self):
		# This gets us the height that the triangle will be along the left side.
		rows = int(input("What height do you want the triangle to be? ")) 
		
		# Every iteration, r will pause while c fills in the characters
		# it grabs the value the current r/row and adds one to create
		# a constantly even slope. If it doesn't add 1, then it will be missing a whole column.	
		for r in range(rows):
			for c in range(r + 1):
				print('*', end=' ')
			print()

	def customTriangle(self):
		# This is making steps
		height =  int(input("What do you want the height of the steps to be? "))

		# Choosing the outline and filling
		outline = input("Enter a character for the outline: ")
		fill = input("Enter a character for the filling: ")

		# This gets the amount of characters to put at the bottom for us
		baseCount = 0 

		# Print the point of the triangle just to make it look better.
		print(f"{outline}")

		for r in range(height):
			# This prints the far left side, aka the start of every row.
			print(f'{outline}', end=' ')
			
			for c in range(r + 1):
				# This prints the inside of the triangle, as empty spaces.
				print(f"{fill}", end=' ')
				
				# This increments with every collum so that we can get the size of the base for the inside
				# then adds two so that the triangle will have complete points on either side.
				if r == (height - 1):
					baseCount += 1
				
			# This is the diagnal edge on the right of the triangle. 
			print(f"\b{outline}")
		
		# This prints the entire base of the triangle, it adds two however. On for the edge on the left, 
		# and one for the point on the far right, just to keep things neat.
		for i in range(height + 2):
			print(f"{outline}", end=' ')
	 
	def circle(self):

		#      # # #        Diameter = 7
		#    # # # # #   
		#  # # # # # # # 
		#  # # # # # # #
		#  # # # # # # # 
		#    # # # # #   
		#      # # # 

		diameter = int(input("What is the diameter of the circle? "))
		radius = int(diameter / 2)
		
		if diameter < 3:
			print(f"{diameter} is not a big enough diameter.")
			self.circle() # run the function again until diameter is big enough
		
		else:
			# Horizontal Movement
			for i in range((2 * radius) + 1):
				
				# Vertical Movement
				for j in range((2 * radius) + 1):
					dist = math.sqrt((i - radius) * (i - radius) + (j - radius) * (j - radius))

					# Dist should be in the range (radius - 0.5)
					# and (radius + 0.5) to print stars
					if(dist > radius - 0.5 and dist < radius + 0.5):
						print('#', end=' ')
					else: 
						print(' ', end=' ')
					
				print()
			
			print("\n")