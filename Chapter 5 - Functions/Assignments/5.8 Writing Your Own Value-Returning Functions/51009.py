def is_prime(x):
	factors = list()
	for i in range(1, x + 1):
		if(x % i) == 0:
			factors.append(i)
	
	if len(factors) == 2 or len(factors) == 1:
		return True
	else: 
		return False

n = int(input("Number: "))
total = 0
count = 0
i = 2
while(count < n):
	if(is_prime(i)):
		total += i
		count += 1
		i += 1
	elif(is_prime(i) == False):
		count += 1
		i += 1

print(f"{total = }")