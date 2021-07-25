import matplotlib.pyplot as plt

def main():
	x_coords = [0, 1, 2, 3, 4]
	y_coords = [15, 25, 75, 150, 300]

	# Graph preferences
	plt.title("LSD Dosage")
	plt.ylabel("Dose (µg)")
	plt.grid(True)
	plt.xlim(xmin = 0, xmax = 4)
	plt.ylim(ymin = 15, ymax = 300)
	plt.xticks(
		[0, 1, 2, 3, 4], 
		["Threshold", "Light", "Common", "Strong", "Heavy"]
	)
	plt.yticks(
		[15, 25, 75, 150, 300],
		["15 µg", "25 µg", "74 µg", "150 µg", "300 µg+"]
	)

	plt.plot(x_coords, y_coords, marker='o')

	# Display the graph
	plt.show()

main()