# Program that gets the total amount of males and females and outputs the percentage for each

males = int(input("Enter number of males:"))
females = int(input("Enter number of females:"))

total = males + females
malePercentage = males / total
femalePercentage = females / total

# Found out how to use round so that I can easily get whole numbers from decimals
print("Percent males: {0}%".format(round(malePercentage*100)))
print("Percent females: {0}%".format(round(femalePercentage*100)))