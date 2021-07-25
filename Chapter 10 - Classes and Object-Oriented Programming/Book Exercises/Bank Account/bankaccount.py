class BankAccount:
	def __init__(self, balance):
		self.__balance = balance
	
	def deposit(self, amount):
		self.__balance += amount
	
	def withdrawal(self, amount):
		if self.__balance >= amount:
			self.__balance -= amount
		else:
			print("Error: Insufficient funds.")
	
	def get_balance(self):
		return self.__balance
	
	# The __str__ method returns a string indicating the object's state
	def __str__(self) -> str:
		return f"The balance is ${self.__balance}"
