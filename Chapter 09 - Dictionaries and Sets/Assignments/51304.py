weights = set([12, 19, 6, 14, 22, 7])

actual_weight = 0
desired_weight = int(input("Desired Weight: "))

# Iterate through the set
for weight in weights:
	# Check and see if the weight is either equal to the desired, or less than
	# or equal to the previously found.
	if(weight > actual_weight and weight <= desired_weight):
		actual_weight = weight

# Remove the weight
weights.discard(actual_weight)

print(actual_weight)
print(weights)