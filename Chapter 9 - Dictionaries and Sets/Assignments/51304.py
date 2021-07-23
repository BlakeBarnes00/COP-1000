weights = set([12, 19, 6, 14, 22, 7])

actual_weight = 0

desired_weight = int(input("Desired Weight: "))
for weight in weights:
	if(weight > actual_weight and weight <= desired_weight):
		actual_weight = weight

# Remove the weight
weights.discard(actual_weight)

print(actual_weight)
print(weights)