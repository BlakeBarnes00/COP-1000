try:
	print(budget/(num_boys + num_girls))
except ZeroDivisionError:
	print("unavailable")