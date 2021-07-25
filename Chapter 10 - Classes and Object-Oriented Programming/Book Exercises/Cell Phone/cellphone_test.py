import cellphone

def main():
	c = cellphone.CellPhone("Samsung", "Note 8", 600.13)
	print(f"Manufacturer: {c.get_manufact()}")
	print(f"Model: {c.get_model()}")
	print(f"Price: {c.get_price():.2f}")

main()