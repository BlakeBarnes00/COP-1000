import coin

def main():
	c = coin.Coin() # Create the object and assign it to a value
	for i in range(10):
		c.toss()
		print(c.get_sideup())

main()	