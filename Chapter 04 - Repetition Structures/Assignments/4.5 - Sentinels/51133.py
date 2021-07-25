# You want to know your grade in Computer Science, so write a program that coninuously
# takes grades between 0-100 to standard input until you "stop", at which point it 
# should print your average to standard output.

print("You can exit program to receive average by entering 'stop'.\n")
grade = input("Enter grade:")

grades = []

while grade != "stop":
	if float(grade) <= 100 and float(grade) >= 0:
		grades.append(float(grade))
	
	grade = input("Enter grade:")

average = sum(grades)/len(grades)
print(grades)
print(f"Your average for Computer Science is {average}.")
