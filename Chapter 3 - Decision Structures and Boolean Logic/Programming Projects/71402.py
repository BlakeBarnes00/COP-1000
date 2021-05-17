# Design a program that asks user to enter month, day, and year in numerical forms
# in this format mm/dd/yy individually. The program should determine if the month 
# and the date make a sum of the year.

month = int(input("Enter month (numeric):"))
day = int(input("Enter day:"))
year = int(input("Enter two digit year:"))

if (month * day) == year:
    print("This date is magic!")
else:
    print("This date is not magic.")