# Check if an integer is prime or not

n = int(input("Enter number:"))

factors = list()
is_prime = False
for i in range(1, n + 1):
	if int(n % i) == 0:
		factors.append(i)


if len(factors) == 2 or len(factors) == 1:
	is_prime = True
else:
	is_prime = False

print(f"{len(factors)} factors \n{factors}")
print(f"{is_prime=}")