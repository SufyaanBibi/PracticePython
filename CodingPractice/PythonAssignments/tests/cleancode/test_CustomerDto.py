import unittest
import json
from CodingPractice.PythonAssignments.cleancode.CustomerDetailsDao import *
from CodingPractice.PythonAssignments.cleancode.CustomerDtoUtils import *


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def json_file(file_name):
    fn = get_file_path(file_name)
    with open(fn, 'r') as f:
        return json.load(f)


class CustomerDetailsTest(unittest.TestCase):

    def test_00_construct_CustomerDetails(self):
        a = CustomerDetails('49', 'Sufi', 'Bibi', 'M', '23', '1995-10-12', 'sufi.bibi@gmail.com',
                            '11/15', 'UK')
        self.assertEqual('Sufi', a.get_first_name())

    def test_01_equality_operator(self):
        a = CustomerDetails('49', 'Sufi', 'Bibi', 'M', '23', '1995-10-12', 'sufi.bibi@gmail.com',
                            '11/15', 'UK')
        b = CustomerDetails('49', 'Sufi', 'Bibi', 'M', '23', '1995-10-12', 'sufi.bibi@gmail.com',
                            '11/15', 'UK')
        self.assertEqual(a, b)

    def test_02_getter_functions(self):
        a = CustomerDetails(49, 'Sufi', 'Bibi', 'M', '23', '1995-10-12', 'sufi.bibi@gmail.com',
                            '11/15', 'UK')
        self.assertEqual(49, a.get_customer_id())
        self.assertEqual('Bibi', a.get_last_name())
        self.assertEqual('M', a.get_sex())
        self.assertEqual('23', a.get_age())
        self.assertEqual('1995-10-12', a.get_birth_date())
        self.assertEqual('sufi.bibi@gmail.com', a.get_email_addr())
        self.assertEqual('11/15', a.get_mail_shot_date())
        self.assertEqual('UK', a.get_iso_country_code())

    def test_03_create_cust(self):
        customer = {"customer_id": 101,
                    "first_name": "Spooky",
                    "last_name": "Dogg",
                    "sex": "M",
                    "age": "10",
                    "birthday": "2008-04-02",
                    "email_address": "spooky.dogg@burbage.rd.com",
                    "mail_shot_date": "11/25",
                    "iso_country_code": "UK",
                    "__type__": "Customer"
                    }
        a = create_cust(customer)
        self.assertEqual(101, a.get_customer_id())
        self.assertEqual('Spooky', a.get_first_name())
        self.assertEqual('Dogg', a.get_last_name())
        self.assertEqual('M', a.get_sex())
        self.assertEqual('10', a.get_age())
        self.assertEqual('2008-04-02', a.get_birth_date())
        self.assertEqual('spooky.dogg@burbage.rd.com', a.get_email_addr())
        self.assertEqual('11/25', a.get_mail_shot_date())
        self.assertEqual('UK', a.get_iso_country_code())

    def test_04_json_in_mk_customers_function(self):
        j = json_file('customers.json')
        custs = make_customers_from_json(j)
        self.assertEqual(3, len(custs))

    def test_05_make_customers_from_json(self):
        j = json_file('customers.json')
        custs = make_customers_from_json(j)
        expected = CustomerDetails(101, 'Spooky', 'Dogg', 'M', '10', '2008-04-02', 'spooky.dogg@burbage.rd.com',
                            '11/25', 'UK')
        self.assertEqual(expected, custs[0])

    def test_06_sort_customers(self):
        j = json_file('customers.json')
        custs = make_customers_from_json(j)
        expected = CustomerDetails(103, 'Lulu', 'Catz', 'M', '13', '2005-01-23', 'lulu@whats-in-the-bag.com',
                            '11/20', 'USA')
        result = sort_customers_by_last_name(custs)
        actual = result[0]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
