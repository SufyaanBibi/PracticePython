import unittest

import testing.postgresql
import psycopg2
import pg8000
from contextlib import closing

from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.OrderPostgresDao import OrderPostgresDao
from CodingPractice.PythonAssignments.shoppingcart.domain.OrderDto import OrderDto, OrderLineDto

create_order_sql = '''
CREATE TABLE orders(
order_id SERIAL,
customer_id integer NOT NULL,
order_timestamp varchar(256),
postage integer);
'''

create_order_line_sql = '''
CREATE TABLE order_line(order_id integer NOT NULL,
product_id integer, 
qty integer);
'''

insert_order_sql = '''
INSERT INTO orders(order_id,
customer_id,
order_timestamp,
postage)
VALUES(%s, %s, %s, %s);
'''

insert_order_line_sql = '''
INSERT INTO order_line(order_id,
product_id, 
qty)
VALUES(%s, %s, %s);
'''


# create initial data in Postgres as fixtures to be used for testing
def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(create_order_sql)
    cursor.execute(create_order_line_sql)
    cursor.close()
    conn.commit()
    conn.close()


class OrderPostgresDaoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        cls.postgresql_instance = cls.Postgresql()
        cls.dao = OrderPostgresDao(cls.postgresql_instance)

    @classmethod
    def tearDownClass(cls):
        cls.postgresql_instance.stop()
        cls.Postgresql.clear_cache()

    def setUp(self):
        pg = type(self).postgresql_instance
        connection = pg8000.connect(**pg.dsn())

        with closing(connection.cursor()) as cursor:
            cursor.execute("BEGIN;")
            cursor.execute("DELETE FROM orders;")
            cursor.execute("DELETE FROM order_line;")
            cursor.execute("COMMIT;")
        connection.close()

    def test_00_can_get_orders(self):
        new_order = OrderDto(order_id=None, customer_id=1, order_timestamp="2018-12-01 10:45:15", postage=1,
                             order_lines=[OrderLineDto(order_id=None, product_id=1, qty=50),
                                          OrderLineDto(order_id=None, product_id=2, qty=100)])
        db_order = type(self).dao.create_order(new_order)
        actual = type(self).dao.get_orders()
        self.assertEqual(db_order, actual[0])

    def test_01_can_create_orders(self):
        order = OrderDto(order_id=None, customer_id=2, order_timestamp="2019-03-20 12:25:09", postage=1,
                         order_lines=[OrderLineDto(order_id=None, product_id=2, qty=15)])
        new_order_in_db = type(self).dao.create_order(order)
        self.assertEqual(order.get_customer_id(), new_order_in_db.get_customer_id())
        self.assertEqual(order.get_postage(), new_order_in_db.get_postage())
        self.assertEqual(order.get_order_timestamp(), new_order_in_db.get_order_timestamp())

    def test_02_can_get_orders_by_customer_id(self):
        new_order = OrderDto(order_id=None, customer_id=2, order_timestamp="2018-12-25 10:45:15", postage=1,
                             order_lines=[OrderLineDto(order_id=None, product_id=1, qty=50),
                                          OrderLineDto(order_id=None, product_id=2, qty=100)])
        new_order_in_db = type(self).dao.create_order(new_order)
        actual = type(self).dao.get_orders_by_customer_id(2)
        self.assertEqual([new_order_in_db], actual)

    def test_03_get_orders_by_product_id(self):
        new_order = OrderDto(order_id=None, customer_id=1, order_timestamp="2018-12-01 10:45:15", postage=1,
                               order_lines=[OrderLineDto(100, 2, 100)])
        new_order_in_db = type(self).dao.create_order(new_order)
        actual = type(self).dao.get_orders_by_product_id(2)
        self.assertEqual([new_order_in_db], actual)

    def test_05_create_an_order_fails(self):
        order = OrderDto(order_id=None, customer_id=1, order_timestamp="2018-12-01 10:45:15", postage=1, order_lines=[])

        with self.assertRaises(Exception) as e:
            type(self).dao.create_order(order)

    def test_06_ROLLBACK_has_worked_after_create_order_fails(self):
        order = OrderDto(order_id=None, customer_id=1, order_timestamp="2018-12-01 10:45:15", postage=1,
                         order_lines=[OrderLineDto(order_id=None, product_id='Abd', qty=50),
                                      OrderLineDto(order_id=None, product_id=2, qty=100)])

        with self.assertRaises(Exception) as e:
            type(self).dao.create_order(order)

        actual = type(self).dao.get_orders()
        self.assertEqual([], actual)

    def test_07_delete_order(self):
        order = OrderDto(order_id=None, customer_id=2, order_timestamp="2019-12-01 10:15:23", postage=1,
                         order_lines=[OrderLineDto(order_id=None, product_id=1, qty=50),
                                      OrderLineDto(order_id=None, product_id=2, qty=100)])
        new_order_in_db = type(self).dao.create_order(order)
        type(self).dao.delete_order(new_order_in_db)
        actual = type(self).dao.get_orders_by_customer_id(2)
        self.assertEqual([], actual)

    def test_08_update_order(self):
        order = OrderDto(order_id=None, customer_id=2, order_timestamp="2019-12-01 10:15:23", postage=1,
                         order_lines=[OrderLineDto(order_id=None, product_id=1, qty=50),
                                      OrderLineDto(order_id=None, product_id=2, qty=100)])
        order_in_db = type(self).dao.create_order(order)
        updated_order = OrderDto(order_id=order_in_db.get_order_id(), customer_id=2, order_timestamp="2019-13-01 10:15:23", postage=1,
                                 order_lines=[OrderLineDto(order_id=order_in_db.get_order_id(), product_id=1, qty=10),
                                              OrderLineDto(order_id=order_in_db.get_order_id(), product_id=2, qty=45)])
        type(self).dao.update_order(updated_order)
        actual = type(self).dao.get_orders_by_customer_id(2)
        self.assertEqual([updated_order], actual)

    def test_09_ROLLBACK_works_after_update_order_fails(self):
        order = OrderDto(order_id=None, customer_id=2, order_timestamp="2019-12-01 10:15:23", postage=1,
                         order_lines=[OrderLineDto(order_id=None, product_id='ABC', qty=50),
                                      OrderLineDto(order_id=None, product_id=2, qty=100)])

        with self.assertRaises(Exception) as e:
            type(self).dao.update_order(order)

        actual = type(self).dao.get_orders_by_customer_id(2)
        self.assertEqual([], actual)


if __name__ == '__main__':
    unittest.main()
