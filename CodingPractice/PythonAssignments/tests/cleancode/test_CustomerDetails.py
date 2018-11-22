import unittest
import json
from CodingPractice.PythonAssignments.cleancode.CustomerDetails import CustomerDetails


def json_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


class CustomerDetailsTest(unittest.TestCase):

    def test_00_get_file(self):
        a = json_file('customers.json')
        print(a)


if __name__ == '__main__':
    unittest.main()
