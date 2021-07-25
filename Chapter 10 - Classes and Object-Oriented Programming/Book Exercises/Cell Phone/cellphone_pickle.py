import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():
	# Init a varialble to control the loop
	again = 'y'

	# Open the output file
	output_file = open(FILENAME, 'wb')

	# Get the phone data
	while again.lower() == 'y':
		man = input("Enter the manufacturer: ")
		mod = input("Enter the model: ")
		price = float(input("Enter the price: "))

		phone = cellphone.CellPhone(man, mod, price)

		pickle.dump(phone, output_file)

		again = input("Enter more phone data? (y/n) ")

	output_file.close()
	print(f"Data was written to {FILENAME}")

main()