def rightTriangle():
	rows = int(input("Enter number of lines for pattern:"))

	for r in range(rows):
		print('#', end='') # LEFT SIDE
		
		for c in range(r):
			print('  ', end='') # MIDDLE
			
		print('#', end='\n') # RIGHT EDGE

rightTriangle()