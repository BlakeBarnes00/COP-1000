numfile1 = open("numbers1.txt", "r")
numfile2 = open("numbers2.txt", "r")

scalar_product = 0

number1 = numfile1.readline()
number2 = numfile2.readline()

while number1 != "" and number2 != "":
	scalar_product += int(number1) * int(number2)
	number1 = numfile1.readline()
	number2 = numfile2.readline()

numfile1.close()
numfile2.close()