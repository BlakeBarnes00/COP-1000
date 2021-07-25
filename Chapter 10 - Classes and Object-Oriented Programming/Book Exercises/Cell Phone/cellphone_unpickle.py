from os import error
import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():
	EOF = False
	
	input_file = open(FILENAME, 'rb')

	while not EOF:
		try:
			phone = pickle.load(input_file)
			display_data(phone)
		
		except EOFError:
			print(error)
			EOF = True
		
	input_file.close()

def display_data(phone):
	print(f"Manufacturer: {phone.get_manufact()}")
	print(f"Model: {phone.get_model()}")
	print(f"Price: {phone.get_price():.2f}")
	print()

main()