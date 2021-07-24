import bankaccount

def main():
	startingBalance = float(input("Enter starting balance: $"))
	
	savings = bankaccount.BankAccount(startingBalance)
	pay = float(input("How much did you just get? $"))
	savings.deposit(pay)

	# Because of the __str__ function you can get a default string returned
	print(savings)


main()