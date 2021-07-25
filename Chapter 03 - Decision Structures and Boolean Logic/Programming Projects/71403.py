# This program mixes primary colors to get the secondary color

primaryColors = ["red", "yellow", "blue"]

pColor1 = input("Enter primary color:")
pColor2 = input("Enter primary color:")

if (pColor1.lower() not in primaryColors) or (pColor2.lower() not in primaryColors):
    print("You didn't input two primary colors.")

if ((pColor1.lower() == "red" and pColor2.lower() == "blue") or (pColor1.lower() == "blue"  and pColor2.lower() == "red")):
    print("When you mix {0} and {1}, you get purple.".format(pColor1, pColor2))
elif ((pColor1.lower() == "red" and pColor2.lower() == "yellow") or (pColor1.lower() == "yellow" and pColor2.lower() == "red")):
    print("When you mix {0} and {1}, you get orange.".format(pColor1, pColor2))
elif ((pColor1.lower() == "yellow" and pColor2.lower() == "blue") or (pColor1.lower() == "blue" and pColor2.lower() == "yellow")):
    print("When you mix {0} and {1}, you get green.".format(pColor1, pColor2))