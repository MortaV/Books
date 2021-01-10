import unittest
from employee_class import Employee


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee('Maria', 'Maximovich', 10000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 20000)


if __name__ == '__main__':
    unittest.main()
