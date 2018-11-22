import unittest
import json
from CodingPractice.PythonAssignments.cleancode.CustomerDetails import CustomerDetails
from CodingPractice.PythonAssignments.cleancode.CustomerDetailsDao import *


def json_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


class CustomerDetailsTest(unittest.TestCase):

    def test_00_get_file(self):
        a = json_file('customers.json')
        make_customers_from_json(a)


if __name__ == '__main__':
    unittest.main()
