class Employee:
	def __init__(self, name, id, dep, title) -> None:
		self.__name = name
		self.__id = id
		self.__department = dep
		self.__job_title = title

	def set_name(self, name):
		self.__name = name
	
	def set_ID(self, id):
		self.__id = id

	def set_department(self, dep):
		self.__department = dep
	
	def set_job(self, job):
		self.__job_title = job

	def get_name(self):
		return self.__name

	def get_ID(self):
		return self.__id
	
	def get_department(self):
		return self.__department
	
	def get_job(self):
		return self.__job_title

def main():
	employees = []
	
	employees.append(Employee("Susan Meyers", 47899, "Accounting", "Vice President")) 
	employees.append(Employee("Mark Jones", 39119, "IT", "Programmer"))
	employees.append(Employee("Joy Rogers", 81774, "Manufacturing", "Engineer"))

	for employee in employees:
		print(f"Name: {employee.get_name()}")
		print(f"ID Number: {employee.get_ID()}")
		print(f"Department: {employee.get_department()}")
		print(f"Job Title: {employee.get_job()}")
		print()

main()