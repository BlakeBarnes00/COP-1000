tuition_ledger = [8000]
INCREASE_RATE = 0.03

def increase_tuition(tuition: int) -> None:
	amount_increased = (tuition * 1.03) - tuition
	tuition *= 1.03
	tuition_ledger.append(tuition)

def print_tuition(year: int) -> None:
	if year > 1:
		print(f"In {year} years, the tuition will be ${tuition_ledger[year]}.")
	elif year == 1:
		print(f"In {year} year, the tuition will be ${tuition_ledger[year]}.")

for i in range(0, 6): 
	increase_tuition(tuition_ledger[i])
	print_tuition(i)