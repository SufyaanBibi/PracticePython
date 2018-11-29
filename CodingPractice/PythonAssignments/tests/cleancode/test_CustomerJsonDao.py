import unittest
from CodingPractice.PythonAssignments.cleancode.CustomerDao import *


class TestCustomerJsonDao(unittest.TestCase):

    def test_00_get_customers(self):
        expected = CustomerDetails(101, 'Spooky', 'Dogg', 'M', '10', '2008-04-02', 'spooky.dogg@burbage.rd.com',
                            '11/25', 'UK')
        c = CustomerJsonDao()
        actual = c.get_customers()
        self.assertEqual(expected, actual[0])
        self.assertEqual(4, len(actual))

    def test_01_get_cust_by_id(self):
        expected = CustomerDetails(101, 'Spooky', 'Dogg', 'M', '10', '2008-04-02', 'spooky.dogg@burbage.rd.com',
                            '11/25', 'UK')
        c = CustomerJsonDao()
        actual = c.get_customer_by_id(101)
        self.assertEqual(expected, actual)

    def test_02_get_cust_by_first_last_name(self):
        c1 = CustomerDetails(101, 'Spooky', 'Dogg', 'M', '10', '2008-04-02', 'spooky.dogg@burbage.rd.com',
                            '11/25', 'UK')
        c2 = CustomerDetails(104, 'Spooky', 'Dogg', 'M', '9', '2010-03-07', 'dodgy-paw@herne.hill.com',
                            '08/14', 'UK')
        expected = [c1, c2]
        c = CustomerJsonDao()
        actual = c.get_customers_by_name('Dogg', 'Spooky')
        self.assertEqual(expected, actual)

    def test_03_get_cust_by_iso_code(self):
        c1 = CustomerDetails(101, 'Spooky', 'Dogg', 'M', '10', '2008-04-02', 'spooky.dogg@burbage.rd.com',
                            '11/25', 'UK')
        c2 = CustomerDetails(102, 'Charlie', 'Dogg', 'M', '4', '2015-06-19', 'snarly.dogg@burbage.rd.com',
                            '11/30', 'UK')
        c3 = CustomerDetails(104, 'Spooky', 'Dogg', 'M', '9', '2010-03-07', 'dodgy-paw@herne.hill.com',
                            '08/14', 'UK')
        expected = [c1, c2, c3]
        c = CustomerJsonDao()
        actual = c.get_customers_by_country('UK')
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
