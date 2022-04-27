INITIAL_SALARY = 15000
SALARY_RATE = .10

def main():
	salary = INITIAL_SALARY
	for i in range(3):
		salary += salary * SALARY_RATE
		if(i == 0):
			print(f"In {i+1} year, the salary will be ${salary:.2f}.")
		else:
			print(f"In {i+1} years, the salary will be ${salary:.2f}.")
		

if __name__ == "__main__":
	main()