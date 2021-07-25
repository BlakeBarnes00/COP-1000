# You are a swimmer and you want to compare all of your race times to find
# the fastes one. Write a program that continuosly doubles from standard
# input, until input is "no more races", at which point it should print out 
# the time of your fastest race.

print("You can recieve the result by entering 'no more races'")
time = input("Enter lap time:")

# holds the list values
times = []

while time != "no more races":
	times.append(float(time))
	time = input("Enter lap time:")

print(f"Best time {min(times)}")