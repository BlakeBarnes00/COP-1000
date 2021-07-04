# This program tests whether or not a list has duplicates

pList = [1, 2, 3, 3]

def main():
	if len(pList) == len(set(pList)):
		print("No dupes")
	else:
		print("Has dupes")


main()