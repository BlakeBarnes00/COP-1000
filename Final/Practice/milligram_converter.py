
# Returns a tuple of kilos and milligrams
def convert_to_kilos(mg: int) -> tuple:
	return int(mg / 1000000), (mg % 1000000)

# Returns a tuple of the grams and milligrams
def convert_to_grams(mg: int) -> tuple:
	return int(mg / 1000), (mg % 1000)


def main():
	milligrams = int(input("Milligrams: "))
	kilos, milligrams = convert_to_kilos(milligrams)
	grams, milligrams = convert_to_grams(milligrams)
	print(f"Kilos: {kilos}\tGrams: {grams}\tMilligrams: {milligrams}")

if __name__ == "__main__":
	main()