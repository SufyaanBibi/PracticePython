import unittest
from CodingPractice.PythonAssignments.shoppingcart.dao.json.CustomerJsonDao import *


class TestCustomerJsonDao(unittest.TestCase):
    
    def setUp(self):
        import os
        dirname = os.path.dirname(__file__)
        fp = os.path.join(dirname, '../resources/customers.json')
        self._custDao = CustomerJsonDao(fp)

    def test_00_get_customers(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        
        actual = self._custDao.get_customers()
        self.assertEqual(expected, actual[0])
        self.assertEqual(4, len(actual))

    def test_01_get_cust_by_id(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        
        actual = self._custDao.get_customer_by_id(101)
        self.assertEqual(expected, actual)

    def test_02_get_cust_by_first_last_name(self):
        c1 = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        c2 = CustomerDto(104, 'Spooky', 'Dogg', 'M', '9', '2010-03-07', 'dodgy-paw@herne.hill.com',
                            '08/14', 'UK')
        expected = [c1, c2]
        
        actual = self._custDao.get_customers_by_name('Dogg', 'Spooky')
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
        
        actual = self._custDao.get_customers_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_04_idempotency_cust_id_v_iso_code(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                            mail_shot_date='11/25', iso_country_code='UK')

        
        by_id = self._custDao.get_customer_by_id(101)
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

        actual = self._custDao.get_customers_by_iso_country_code('UK')
        self.assertEqual(expec, actual)
        by_id = self._custDao.get_customer_by_id(101)
        self.assertEqual(expected, by_id)

    def test_05_MethodNotImplementedException_raised_on_create_customer(self):

        c1 = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age='10',
                         birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                         mail_shot_date='11/25', iso_country_code='UK')

        with self.assertRaises(MethodNotImplementedException) as e:
            self._custDao.create_customer(c1)
        self.assertEqual('create_customer called on CustomerJsonDao', e.exception._message)


if __name__ == '__main__':
    unittest.main()
