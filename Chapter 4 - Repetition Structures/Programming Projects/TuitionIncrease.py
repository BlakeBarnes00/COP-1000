# Tuition costs $8000 per semester.
# Tuition is increasing 3% each year for the next five years.
# Write a loop that displays the projected semester tuition 
# amount for the next five years.

# Place to store tuition each year, index 0 will be the initial price
tuitionLog = [8000]
INCREASE_RATE = 0.03

def increaseTuition(tuition):
	# Get the amount the tutition will increase by, add it to the tuition.
	amountIncreased = (tuition * 1.03) - tuition
	tuition *= 1.03

	# print(f"Tuition increase by ${amountIncreased} and is now ${tuition}.")
	tuitionLog.append(tuition) # Add tuition to the list for easy sorting

def printTuition(year):
	if year > 1:
		print(f"In {year} years, the tuition will be ${tuitionLog[year]}.")
	elif year == 1:
		print(f"In {year} year, the tuition will be ${tuitionLog[year]}.")


# Loop over 6 times since I include the first unincreased year
for i in range(6):
	increaseTuition(tuitionLog[i])
	printTuition(i)

print(tuitionLog)