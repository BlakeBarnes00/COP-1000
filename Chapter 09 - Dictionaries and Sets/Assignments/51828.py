# Flip the keys to the values, and the values to the keys
namesAndNumbers = {"Ellis": 123456789, "Roy": 987654321, "Blake": 753159842}
numbersAndNames = {}

for k in namesAndNumbers:
	numbersAndNames[namesAndNumbers[k]] = k

print(numbersAndNames)