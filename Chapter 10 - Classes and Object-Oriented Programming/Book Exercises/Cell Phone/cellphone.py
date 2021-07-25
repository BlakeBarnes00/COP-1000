class CellPhone:
	def __init__(self, manufact, model, price) -> None:
		self.__manufact = manufact
		self.__model = model
		self.__price = price

	def set_manufact(self, manufact) -> str:
		self.__manufact = manufact
	
	def set_model(self, model) -> str:
		self.__model = model
	
	def set_price(self, price) -> float:
		self.__price = price

	def get_manufact(self) -> str:
		return self.__manufact

	def get_model(self) -> str:
		return self.__model
	
	def get_price(self) -> float:
		return self.__price
