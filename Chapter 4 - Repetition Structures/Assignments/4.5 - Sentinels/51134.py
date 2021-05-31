# This program just tracks the stock of muffins and cupcakes in a bakery.
# The goal is to track how many are purchased by removing 1 from the
# integer value that is storing it. If they reach 0 then then
# it will print 'Out of stock'. The program will close if '0' is inputted

muffins = 5
cupcakes = 3

choice = ''

while choice != '0':
	choice = input("Cupcake or Muffin? ")
	if choice.lower() == "cupcake":
		if cupcakes > 0:
			cupcakes -= 1
		else:
			print("Out of stock")
	elif choice.lower() == "muffin":
		if muffins > 0:
			muffins -= 1
		else:
			print("Out of stock")
	
print(f"Cupcakes left {cupcakes} \nMuffins left {muffins}")