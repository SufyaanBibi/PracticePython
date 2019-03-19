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
        new_order = OrderDto(None, 1, "2018-12-01 10:45:15", 1,
                             [OrderLineDto(None, 1, 50),
                              OrderLineDto(None, 2, 100)])
        db_order = type(self).dao.create_order(new_order)
        actual = type(self).dao.get_orders()
        self.assertEqual(db_order, actual[0])

    def test_01_can_get_order_by_id(self):
        expected = OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                             [OrderLineDto(101, 1, 50),
                              OrderLineDto(101, 2, 100)])
        type(self).dao.create_order(expected)
        actual = type(self).dao.get_order_by_order_id(101)
        self.assertEqual([expected], actual)

    def test_02_can_get_orders_by_customer_id(self):
        expected = OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                             [OrderLineDto(101, 1, 50),
                              OrderLineDto(101, 2, 100)])
        type(self).dao.create_order(expected)
        actual = type(self).dao.get_orders_by_customer_id(2)
        self.assertEqual([expected], actual)

    def test_03_get_orders_by_product_id(self):
        expected = OrderDto(100, 1, "2018-12-01 10:45:15", 1,
                               [OrderLineDto(100, 2, 100)])
        type(self).dao.create_order(expected)
        actual = type(self).dao.get_orders_by_product_id(2)
        self.assertEqual([expected], actual)

    def test_04_can_create_an_order(self):
        order = OrderDto(999, 1, "2018-12-01 10:45:15", 1,
                             [OrderLineDto(999, 1, 50),
                              OrderLineDto(999, 2, 100)])
        type(self).dao.create_order(order)

        actual = type(self).dao.get_order_by_order_id( 999 )
        self.assertEqual([order], actual)

    def test_05_create_an_order_fails(self):
        order = OrderDto(None, 1, "2018-12-01 10:45:15", 1, [])

        with self.assertRaises(Exception) as e:
            type(self).dao.create_order(order)

    def test_06_ROLLBACK_has_worked_after_create_order_fails(self):
        order = OrderDto(1000, 1, "2018-12-01 10:45:15", 1,
                         [OrderLineDto(None, 1, 50),
                          OrderLineDto(1000, 2, 100)])

        with self.assertRaises(Exception) as e:
            type(self).dao.create_order(order)

        actual = type(self).dao.get_order_by_order_id(1000)
        self.assertEqual([], actual)

    def test_07_delete_order(self):
        order = OrderDto(777, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto(777, 1, 50),
                          OrderLineDto(777, 2, 100)])
        type(self).dao.create_order(order)
        type(self).dao.delete_order(order)
        actual = type(self).dao.get_order_by_order_id(777)
        self.assertEqual([], actual)

    def test_08_update_order(self):
        order = OrderDto(777, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto(777, 1, 50),
                          OrderLineDto(777, 2, 100)])
        updated_order = OrderDto(777, 2, "2019-13-01 10:15:23", 1,
                                 [OrderLineDto(777, 1, 10),
                                  OrderLineDto(777, 2, 45)])
        type(self).dao.create_order(order)
        type(self).dao.update_order(updated_order)
        actual = type(self).dao.get_order_by_order_id(777)
        self.assertEqual([updated_order], actual)

    def test_09_ROLLBACK_works_after_update_order_fails(self):
        order = OrderDto(65, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto('abc', 1, 50),
                          OrderLineDto(65, 2, 100)])

        with self.assertRaises(Exception) as e:
            type(self).dao.update_order(order)

        actual = type(self).dao.get_order_by_order_id(65)
        self.assertEqual([], actual)

    def test_10_ROLLBACK_occurs_when_delete_fails_in_update_order(self):
        order = OrderDto(777, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto(777, 1, 50),
                          OrderLineDto(777, 2, 100)])

        type(self).dao.create_order(order)

        order2 = OrderDto(777, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto('abc', 1, 50),
                          OrderLineDto(777, 2, 100)])

        updated_order = OrderDto(777, 2, "2019-13-01 10:15:23", 1,
                                 [OrderLineDto(777, 1, 10),
                                  OrderLineDto(777, 2, 45)])

        type(self).dao.update_order(updated_order)
        actual = type(self).dao.get_order_by_order_id(777)
        self.assertEqual([updated_order], actual)

    def test_11_ROLLBACK_occurs_when_create_fails_in_update_order(self):
        order = OrderDto(654, 2, "2019-12-01 10:15:23", 1,
                         [OrderLineDto(654, 1, 50),
                          OrderLineDto(654, 2, 100)])
        type(self).dao.create_order(order)

        updated_order = OrderDto(654, 2, "2019-13-01 10:15:23", 1,
                                 [OrderLineDto('bcv', 1, 10),
                                  OrderLineDto(654, 2, 45)])

        with self.assertRaises(Exception) as e:
            type(self).dao.update_order(updated_order)

        actual = type(self).dao.get_order_by_order_id(654)
        self.assertEqual([order], actual)


if __name__ == '__main__':
    unittest.main()
