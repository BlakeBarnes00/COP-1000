def square():
	rows = int(input("How big do you want the square? "))

	for r in range(rows):
		for c in range(rows):
			print('*', end=' ')
		print()
		
def rectangle():
	rows = int(input("How many rows do you want? "))
	cols = int(input("How many columns do you want? "))
	
	for r in range(rows):
		for c in range(cols):
			print('*', end=' ')
		print()

def rightTriangle():
	# This gets us the height that the triangle will be along the left side.
	rows = int(input("What height do you want the triangle to be? ")) 
	# Every iteration, r will pause while c fills in the characters
	# it grabs the value the current r/row and adds one to create
	# a constantly even slope. If it doesn't add 1, then it will be missing a whole column.	

	for r in range(rows):
		for c in range(r + 1):
			print('*', end=' ')
		print()
	

rightTriangle()