# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5000 to the
# annual salary by default but also accepts a different raise amount.
# Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so
# you don’t have to create a new employee instance in each test method. Run
# your test case, and make sure both tests pass.
import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Test case for Employee class."""
    def setUp(self):
        """Create an employee to use in all tests."""
        self.new_employee = Employee('Christian', 'Goeke', 75000)

    def test_give_default_raise(self):
        """Test that the default raise of 5000 is given."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 80000)

    def test_give_custom_raise(self):
        """Test custom raise amount."""
        self.new_employee.give_raise(25000)
        self.assertEqual(self.new_employee.salary, 100000)


unittest.main()