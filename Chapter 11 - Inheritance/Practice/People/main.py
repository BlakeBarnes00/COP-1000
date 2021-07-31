class Person:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def print_name(self):
		print(self.first, self.last)

class Student(Person):
	def __init__(self, first, last, year):
		super().__init__(first, last)
		self.__grad_year = year

	def get_year(self):
		return self.__grad_year

def main():
	x = Person("John", "Doe")
	x.print_name()

	y = Student("Ellis", "Barnes", 2022)
	y.print_name()
	print(y.get_year())
	

main()