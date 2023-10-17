import unittest
import datetime


# import functions from solutions
from solution_1 import read_database_version
from solution_2 import get_warehouse_detail, get_employee_detail
from solution_3 import update_employee_experience
from solution_4 import get_specialist_employee_list

# get the database version information
database_version = read_database_version()


class TestCalcSolution(unittest.TestCase):

    def test_read_database_version(self):
        expected_output = database_version
        actual_output = read_database_version()

        self.assertEqual(expected_output, actual_output)

    def test_get_employee_detail(self):
        expected_output = (105, 'Linda', 3, datetime.date(
            2004, 6, 4), 'Logistics Spcialist', 42000, 19)
        actual_output = get_employee_detail(105)

        self.assertEqual(expected_output, actual_output)

    def test_get_warehouse_detail(self):
        expected_output = (2, 'Rewe Warehouse', 400)
        actual_output = get_warehouse_detail(2)

        self.assertEqual(expected_output, actual_output)

    def test_update_employee_experience(self):
        expected_output = None
        actual_output = update_employee_experience(101)

        self.assertEqual(expected_output, actual_output)

    def test_get_specialist_employee_list(self):
        expected_output = None
        actual_output = get_specialist_employee_list("Driver", 30000)

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
# --------------------------------
#     Ran 5 tests in 0.062s

# OK
