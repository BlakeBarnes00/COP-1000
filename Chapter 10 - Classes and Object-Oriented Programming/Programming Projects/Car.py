class Car:
	def __init__(self, year, make) -> None:
		self.__year_model = year
		self.__make = make
		self.__speed = 0

	def accelerate(self) -> None:
		self.__speed += 5

	def brake(self) -> None:
		self.__speed -= 5

	def get_speed(self) -> int:
		return self.__speed

def main():
	car = Car(2003, "BMW")

	for i in range(5):
		car.accelerate()
		print(car.get_speed())

	for i in range(5):
		car.brake()
		print(car.get_speed())

main()