def power_to(num, pow):
	if pow < 0:
		return 0
	else:
		return num ** pow

print(power_to(5, 5))