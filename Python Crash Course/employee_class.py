class Employee:

    def __init__(self, name, surname, annual_salary):
        self.name = name
        self.surname = surname
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        self.annual_salary += salary_raise
