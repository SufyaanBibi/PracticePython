import unittest
from CodingPractice.PythonAssignments.shoppingcart.dao.CustomerJsonDao import *


class TestCustomerJsonDao(unittest.TestCase):

    def test_00_get_customers(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        c = CustomerJsonDao()
        actual = c.get_customers()
        self.assertEqual(expected, actual[0])
        self.assertEqual(4, len(actual))

    def test_01_get_cust_by_id(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        c = CustomerJsonDao()
        actual = c.get_customer_by_id(101)
        self.assertEqual(expected, actual)

    def test_02_get_cust_by_first_last_name(self):
        c1 = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        c2 = CustomerDto(104, 'Spooky', 'Dogg', 'M', '9', '2010-03-07', 'dodgy-paw@herne.hill.com',
                            '08/14', 'UK')
        expected = [c1, c2]
        c = CustomerJsonDao()
        actual = c.get_customers_by_name('Dogg', 'Spooky')
        self.assertEqual(expected, actual)

    def test_03_get_cust_by_iso_country_code(self):
        c1 = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                                birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                                mail_shot_date='11/25', iso_country_code='UK')
        c2 = CustomerDto(customer_id=102, first_name='Charlie', last_name='Dogg', sex='M', age='4',
                         birthday='2015-06-19', email_address='snarly.dogg@burbage.rd.com',
                            mail_shot_date='11/30', iso_country_code='UK')
        c3 = CustomerDto(customer_id=104, first_name='Spooky', last_name='Dogg', sex='M', age='9',
                         birthday='2010-03-07', email_address='dodgy-paw@herne.hill.com',
                            mail_shot_date='08/14', iso_country_code='UK')
        expected = [c1, c2, c3]
        c = CustomerJsonDao()
        actual = c.get_customers_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_04_idempotency_cust_id_v_iso_code(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                            mail_shot_date='11/25', iso_country_code='UK')
        c = CustomerJsonDao()
        by_id = c.get_customer_by_id(101)
        self.assertEqual(expected, by_id)
        c1 = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                            mail_shot_date='11/25', iso_country_code='UK')
        c2 = CustomerDto(customer_id=102, first_name='Charlie', last_name='Dogg', sex='M', age='4',
                         birthday='2015-06-19', email_address='snarly.dogg@burbage.rd.com',
                            mail_shot_date='11/30', iso_country_code='UK')
        c3 = CustomerDto(customer_id=104, first_name='Spooky', last_name='Dogg', sex='M', age='9',
                         birthday='2010-03-07', email_address='dodgy-paw@herne.hill.com',
                            mail_shot_date='08/14', iso_country_code='UK')
        expec = [c1, c2, c3]
        c = CustomerJsonDao()
        actual = c.get_customers_by_iso_country_code('UK')
        self.assertEqual(expec, actual)
        by_id = c.get_customer_by_id(101)
        self.assertEqual(expected, by_id)


if __name__ == '__main__':
    unittest.main()
