class WeatherForcast():
	# This is how I would make it, however in MPL it doesn't let me use 
	# private variables
	def __init__(self):
		self.__skies = ""
		self.__high = 0
		self.__low = 0

	def set_skies(self, skies) -> str:
		self.__skies = skies
	
	def set_high(self, amount) -> int:
		self.__high = amount
	
	def set_low(self, amount) -> int:
		self.__low = amount

	def get_skies(self) -> str:
		return self.__skies

	def get_high(self) -> int:
		return self.__high

	def get_low(self) -> int:
		return self.__low	

def main():
	fc = WeatherForcast()
	print(fc.get_high())
	print(fc.get_low())
	print(fc.get_skies())

main()