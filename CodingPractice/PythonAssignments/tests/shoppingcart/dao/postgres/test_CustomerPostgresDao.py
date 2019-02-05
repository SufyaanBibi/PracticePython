import unittest
import pg8000
import testing.postgresql
import psycopg2
from contextlib import closing


from CodingPractice.PythonAssignments.shoppingcart.domain.CustomerDto import CustomerDto
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.CustomerPostgresDao import CustomerPostgresDao

cust_create_sql = '''
CREATE TABLE customer(customer_id SERIAL PRIMARY KEY, 
first_name varchar(256),
last_name varchar(256),
sex varchar(1),
age integer,
birthday varchar(12),
email_address varchar(256),
mail_shot_date varchar(12),
iso_country_code varchar(3)
);
'''

insert_cust_sql = '''
INSERT INTO  customer(customer_id, 
first_name,
last_name,
sex,
age,
birthday,
email_address,
mail_shot_date,
iso_country_code)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
'''


# create initial data in Postgres as fixtures to be used for testing
def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(cust_create_sql)
    cursor.close()
    conn.commit()
    conn.close()


class CustomerPostgresDaoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        cls.postgresql_instance = cls.Postgresql()
        cls.dao = CustomerPostgresDao(cls.postgresql_instance)

    @classmethod
    def tearDownClass(cls):
        cls.postgresql_instance.stop()
        cls.Postgresql.clear_cache()

    def setUp(self):
        pg = type(self).postgresql_instance
        connection = pg8000.connect(**pg.dsn())

        with closing(connection.cursor()) as cursor:
            cursor.execute("BEGIN;")
            cursor.execute("DELETE FROM customer;")
            cursor.execute("COMMIT;")
        connection.close()

    def test_00_test_create_dto_from_row(self):
        expected = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age=10,
                               birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')

        row = [101, 'Spooky', 'Dogg', 'M', 10, '2008-04-02', 'spooky.dogg@burbage.rd.com', '11/25', 'UK']

        actual = CustomerPostgresDao._create_cust_dto_from_row(row)

        self.assertEqual(expected, actual)

    def test_01_get_customers(self):
        cust = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age=10,
                                birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                                mail_shot_date='11/25', iso_country_code='UK')
        cust_2 = CustomerDto(customer_id=102, first_name='Charlie', last_name='Bone', sex='M', age=10,
                                birthday='2008-04-02', email_address='charlie.bone@burbage.rd.com',
                                mail_shot_date='11/25', iso_country_code='UK')
        type(self).dao.create_customer(cust)
        type(self).dao.create_customer(cust_2)
        expected = [cust, cust_2]
        actual = type(self).dao.get_customers()
        self.assertEqual(expected, actual)

    def test_02_get_customer_by_id(self):
        expected = CustomerDto(customer_id=102, first_name='Charlie', last_name='Bone', sex='M', age=10,
                                birthday='2008-04-02', email_address='charlie.bone@burbage.rd.com',
                                mail_shot_date='11/25', iso_country_code='UK')
        type(self).dao.create_customer(expected)
        actual = type(self).dao.get_customer_by_id(102)
        self.assertEqual(expected, actual)

    def test_03_get_customers_by_name(self):
        expected = CustomerDto(customer_id=102, first_name='Charlie', last_name='Bone', sex='M', age=10,
                               birthday='2008-04-02', email_address='charlie.bone@burbage.rd.com',
                               mail_shot_date='11/25', iso_country_code='UK')
        type(self).dao.create_customer(expected)
        actual = type(self).dao.get_customers_by_name('Bone', 'Charlie')
        self.assertEqual([expected], actual)

    def test_04_get_customers_by_iso_country_code(self):
        cust = CustomerDto(customer_id=101, first_name='Spooky', last_name='Dogg', sex='M', age=10,
                           birthday='2008-04-02', email_address='spooky.dogg@burbage.rd.com',
                           mail_shot_date='11/25', iso_country_code='UK')
        cust_2 = CustomerDto(customer_id=102, first_name='Charlie', last_name='Bone', sex='M', age=10,
                             birthday='2008-04-02', email_address='charlie.bone@burbage.rd.com',
                             mail_shot_date='11/25', iso_country_code='UK')
        type(self).dao.create_customer(cust)
        type(self).dao.create_customer(cust_2)
        expected = [cust, cust_2]
        actual = type(self).dao.get_customers_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_05_create_customer(self):
        cust = CustomerDto(customer_id=999, first_name='Pangur', last_name='Ban', sex='M', age=23,
                               birthday='1995-10-12', email_address='pan.ban@burbage.rd.com',
                               mail_shot_date='09/08', iso_country_code='USA')
        type(self).dao.create_customer(cust)
        actual = type(self).dao.get_customer_by_id(999)
        self.assertEqual(cust, actual)

    def test_06_no_customer_id(self):
        self.assertEqual(None, type(self).dao.get_customer_by_id(7))

    def test_07_no_customer_by_name(self):
        self.assertEqual([], type(self).dao.get_customers_by_name('Adrian', 'Fawn'))

    def test_08_no_customer_by_iso_country_code(self):
        self.assertEqual([], type(self).dao.get_customers_by_iso_country_code('SE'))

    def test_09_delete_customer(self):
        cust = CustomerDto(customer_id=999, first_name='Pangur', last_name='Ban', sex='M', age=23,
                           birthday='1995-10-12', email_address='pan.ban@burbage.rd.com',
                           mail_shot_date='09/08', iso_country_code='USA')
        type(self).dao.create_customer(cust)
        type(self).dao.delete_customer(cust)
        actual = type(self).dao.get_customer_by_id(999)
        self.assertEqual(None, actual)

    def test_10_update_customer(self):
        cust = CustomerDto(customer_id=999, first_name='Pangur', last_name='Ban', sex='M', age=23,
                           birthday='1995-10-12', email_address='pan.ban@burbage.rd.com',
                           mail_shot_date='09/08', iso_country_code='USA')
        type(self).dao.create_customer(cust)
        expected = CustomerDto(customer_id=999, first_name='Pangur', last_name='Ban', sex='M', age=24,
                             birthday='1995-10-12', email_address='panpan@northernlights.com', mail_shot_date='09/08',
                             iso_country_code='UK')
        type(self).dao.update_customer(expected)
        actual = type(self).dao.get_customer_by_id(999)
        self.assertEqual(expected, actual)

    def test_11_delete_customer_that_does_not_exist(self):
        cust = CustomerDto(customer_id=88, first_name='Pangur', last_name='Ban', sex='M', age=23,
                           birthday='1995-10-12', email_address='pan.ban@burbage.rd.com',
                           mail_shot_date='09/08', iso_country_code='USA')
        type(self).dao.delete_customer(cust)
        actual = type(self).dao.get_customer_by_id(88)
        self.assertEqual(None, actual)

    def test_12_update_customer_that_does_not_exist(self):
        cust = CustomerDto(customer_id=90, first_name='Pangur', last_name='Ban', sex='M', age=23,
                           birthday='1995-10-12', email_address='pan.ban@burbage.rd.com',
                           mail_shot_date='09/08', iso_country_code='USA')
        type(self).dao.update_customer(cust)
        actual = type(self).dao.get_customer_by_id(90)
        self.assertEqual(None, actual)

    def test_13_ROLLBACK(self):
        cust = CustomerDto(customer_id=None, first_name='Julia', last_name='Bibi', sex='F', age=56,
                           birthday='1962-5-5', email_address='julia.bibi@burbage.rd.com',
                           mail_shot_date='12/08', iso_country_code='UK')

        with self.assertRaises(Exception) as e:
            type(self).dao.create_customer(cust)

        actual = type(self).dao.get_customers_by_name('Julia', 'Bibi')
        self.assertEqual([], actual)

    def test_14_check_SERIAL_works(self):
        cust = CustomerDto(customer_id=1, first_name='Tom', last_name='Bull', sex='M', age=25,
                           birthday='1993-10-12', email_address='tom.bull@hotmail.com',
                           mail_shot_date='04/09', iso_country_code='UK')
        cust_2 = CustomerDto(customer_id=2, first_name='Wren', last_name='Smith', sex='F', age=43,
                             birthday='1913-11-12', email_address='wren.smith@hotmail.com',
                             mail_shot_date='04/10', iso_country_code='USA')
        type(self).dao.create_customer(cust)
        type(self).dao.create_customer(cust_2)

        expected = CustomerDto(customer_id=2, first_name='Wren', last_name='Smith', sex='F', age=43,
                               birthday='1913-11-12', email_address='wren.smith@hotmail.com',
                               mail_shot_date='04/10', iso_country_code='USA')
        actual = type(self).dao.get_customer_by_id(2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
