"""This file contains Employee class which represents an employee details"""


class Employee:
	"""Represents an employee details"""

	_employee_count = 0

	def __init__(self, employee_id: int, name: str, position: str, salary: float) -> None:
		self.employee_id = employee_id
		self.name = name
		self.position = position
		self.salary = salary
		Employee._employee_count += 1

	def __str__(self) -> str:
		return f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

	@property
	def salary(self) -> float:
		return self._salary

	@salary.setter
	def salary(self, value: float) -> None:
		self._salary = value

	@classmethod
	def total_employees(cls) -> int:
		return cls._employee_count

	@classmethod
	def from_string(cls, employee_str: str) -> bool:
		employee_id, name, position, salary = employee_str.split(',')
		for employee in employees:
			if employee.employee_id == int(employee_id) and employee.name == name and employee.position == position and employee.salary == float(salary):
				return True
		return False

class Manager(Employee):
	def __init__(self, employee_id: int, name: str, salary: float) -> None:
		super().__init__(employee_id, name, "Manager", salary)

	def promote(self, employee_id: int, increase: float) -> None:
		for employee in employees:
			if employee.employee_id == employee_id:
				employee.salary += increase
				return

class Developer(Employee):
	def __init__(self, employee_id: int, name: str, salary: float) -> None:
		super().__init__(employee_id, name, "Developer", salary)

	def role(self) -> str:
		return f"{self.name} is a developer."


class Intern(Employee):
	def __init__(self, employee_id: int, name: str, salary: float) -> None:
		super().__init__(employee_id, name, "Intern", salary)

	def learn(self, skill: str) -> str:
		return f"{self.name} is learning {skill}."


if __name__ == "__main__":
	employees = [
		Manager(1, "Harith", 60000),
		Developer(2, "Hareesh", 50000),
		Intern(3, "Akshayan", 25000)
	]

	manager = employees[0]
	developer = employees[1]
	intern = employees[2]

	manager.promote(2, 5000)
	print(manager)
	print(developer)
	print(developer.role())
	print(intern)
	print(intern.learn("Python"))
	print(f"Total employees: {Employee.total_employees()}")

	print(f"Employee Harith found: {Employee.from_string('1,Harith,Manager,60000')}")