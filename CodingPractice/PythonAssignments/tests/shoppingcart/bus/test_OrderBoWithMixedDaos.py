import unittest
import os
from decimal import *
import testing.postgresql
import psycopg2

from CodingPractice.PythonAssignments.shoppingcart.bus.OrderBo import OrderBo, OrderIdNonexistent, VatNegative, \
    InvalidMonth
from CodingPractice.PythonAssignments.shoppingcart.dao.json.OrderJsonDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.json.ProductJsonDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.CustomerPostgresDao import CustomerPostgresDao
from CodingPractice.PythonAssignments.shoppingcart.dao.json.PostageRateJsonDao import *

cust_create_sql = '''
CREATE TABLE customer(customer_id integer, 
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
    cursor.execute(insert_cust_sql,
                   (101, 'Spooky', 'Dogg', 'M', 10, '2008-04-02', 'spooky.dogg@burbage.rd.com', '11/25', 'UK'))
    cursor.execute(insert_cust_sql,
                   (102, 'Charlie', 'Bone', 'M', 10, '2008-04-02', 'charlie.bone@burbage.rd.com', '11/25', 'UK'))
    cursor.execute(insert_cust_sql,
                   (103, 'Lulu', 'Catz', 'M', 13, '2005-01-23', 'lulu@whats-in-the-bag.com', '11/20', 'USA'))
    cursor.close()
    conn.commit()
    conn.close()


class TestOrderBoWithJsonDaos(unittest.TestCase):

    def setUp(self):
        self.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        self.postgresql_instance = self.Postgresql()

        dirname = os.path.dirname(__file__)
        ordFp = os.path.join(dirname, '../resources/orders.json')
        prodFp = os.path.join(dirname, '../resources/products.json')
        postFp = os.path.join(dirname, '../resources/postage_matrix.json')
        orderJsonDao = OrderJsonDao(ordFp)
        prodJsonDao = ProductJsonDao(prodFp)
        custPostgresDao = CustomerPostgresDao(self.postgresql_instance)
        postJsonDao = PostageRateJsonDao(postFp)
        self._orderBo = OrderBo(orderJsonDao, prodJsonDao, custPostgresDao, postJsonDao)

    def test_00_order_bo_instantiates(self):
        try:
            import os
            dirname = os.path.dirname(__file__)
            ordFp = os.path.join(dirname, '../resources/orders.json')
            prodFp = os.path.join(dirname, '../resources/products.json')
            postFp = os.path.join(dirname, '../resources/postage_matrix.json')
            orderJsonDao = OrderJsonDao(ordFp)
            prodJsonDao = ProductJsonDao(prodFp)
            custPostgresDao = CustomerPostgresDao(self.postgresql_instance)
            postJsonDao = PostageRateJsonDao(postFp)
            a = OrderBo(orderJsonDao, prodJsonDao, custPostgresDao, postJsonDao)
        except Exception:
            self.fail("Insantiation incorrectly raised exception")

    def test_01_get_order_total_by_order_id(self):
        self.assertEqual(Decimal('1621.20'), self._orderBo.get_order_total_by_order_id(7, 20))

    def test_02_get_multiple_order_total_by_id(self):
        self.assertEqual(Decimal('204.24'), self._orderBo.get_order_total_by_order_id(5, 20))

    def test_03_order_id_does_not_exist(self):
        with self.assertRaises(OrderIdNonexistent) as e:
            self._orderBo.get_order_total_by_order_id(19, 20)
        self.assertEqual('Order ID 19 does not exist.', e.exception._message)

    def test_04_no_order_lines(self):
        self.assertEqual(0, self._orderBo.get_order_total_by_order_id(8, 20))

    def test_05_vat_is_zero(self):
        self.assertEqual(1351.0, self._orderBo.get_order_total_by_order_id(7, 0))

    def test_06_VAT_is_negative(self):
        with self.assertRaises(VatNegative) as e:
            self._orderBo.get_order_total_by_order_id(8, -1)
        self.assertEqual('In order ID 8 invalid VAT passed: -1', e.exception._message)

    def test_07_get_order_total_by_cust_id(self):
        self.assertEqual(Decimal('1621.20'), self._orderBo.get_order_total_by_customer_id(103, 20))

    def test_08_cust_id_has_no_orders(self):
        self.assertEqual(0, self._orderBo.get_order_total_by_customer_id(70, 20))

    def test_09_cust_has_no_order_lines(self):
        self.assertEqual(0, self._orderBo.get_order_total_by_customer_id(120, 20))

    def test_10_VAT_is_zero(self):
        self.assertEqual(1351.0, self._orderBo.get_order_total_by_customer_id(103, 0))

    def test_11_VAT_is_negative(self):
        with self.assertRaises(VatNegative) as e:
            self._orderBo.get_order_total_by_customer_id(103, -1)
        self.assertEqual('In customer ID 103 invalid VAT passed: -1', e.exception._message)

    def test_12_get_orders_by_month(self):
        self.assertEqual([OrderDto(order_id=8, customer_id=120, order_timestamp='2018-06-25 10:55:10',
                                   postage=2, order_lines=[])], self._orderBo.get_orders_by_month(6))

    def test_13_get_multiple_orders_by_month(self):
        self.assertEqual([OrderDto(order_id=1, customer_id=101, order_timestamp="2018-11-25 11:45:15",
                                   postage=1, order_lines=[OrderLineDto(1, 1, 1), OrderLineDto(1, 2, 3)]),
                          OrderDto(order_id=2, customer_id=101, order_timestamp="2018-11-30 11:45:15",
                                   postage=2, order_lines=[OrderLineDto(2, 1, 1), OrderLineDto(2, 2, 3)]),
                          OrderDto(order_id=5, customer_id=102, order_timestamp="2018-11-15 10:45:15",
                                   postage=1, order_lines=[OrderLineDto(5, 5, 1), OrderLineDto(5, 6, 1)])],
                         self._orderBo.get_orders_by_month(11))

    def test_14_invalid_month(self):
        with self.assertRaises(InvalidMonth) as e:
            self._orderBo.get_orders_by_month(45)
        self.assertEqual('Month number 45 is invalid.', e.exception._message)

    def test_15_no_orders_month(self):
        self.assertEqual([], self._orderBo.get_orders_by_month(1))

    def test_16_get_order_total_by_month(self):
        self.assertEqual(0, self._orderBo.get_order_total_by_month(6, 20))

    def test_17_get_multiple_total_by_month(self):
        self.assertEqual(Decimal('427.08'), self._orderBo.get_order_total_by_month(11, 20))

    def test_18_no_orders_month(self):
        self.assertEqual(0, self._orderBo.get_order_total_by_month(1, 20))

    def test_19_invalid_VAT(self):
        with self.assertRaises(VatNegative) as e:
            self._orderBo.get_order_total_by_month(11, -1)
        self.assertEqual('VAT rate -1 is invalid.', e.exception._message)

    def test_20_invalid_month(self):
        with self.assertRaises(InvalidMonth) as e:
            self._orderBo.get_order_total_by_month(45, 20)
        self.assertEqual('Month number 45 is invalid.', e.exception._message)

    def test_21_get_order_with_no_vatable_objects(self):
        self.assertEqual(Decimal('40.20'), self._orderBo.get_order_total_by_order_id(9, 20))

    def test_22_get_postage_cost_by_order_id(self):
        self.assertEqual(3.45, self._orderBo.get_postage_cost_by_order_id(1))

    def test_23_postage_USA_cost_over_1kg(self):
        self.assertEqual(15.50, self._orderBo.get_postage_cost_by_order_id(7))


if __name__ == '__main__':
    unittest.main()
