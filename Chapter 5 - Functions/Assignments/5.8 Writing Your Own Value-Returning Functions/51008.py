def is_prime(x):
	factors = list()
	for i in range(1, x + 1):
		if(x % i) == 0:
			factors.append(i)
	
	if len(factors) == 2 or len(factors) == 1:
		return True
	else: 
		return False

print(is_prime(15))