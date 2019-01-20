import unittest

import testing.postgresql
import psycopg2

from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.OrderPostgresDao import OrderPostgresDao
from CodingPractice.PythonAssignments.shoppingcart.domain.OrderDto import OrderDto, OrderLineDto

create_order_sql = '''
CREATE TABLE orders(order_id integer NOT NULL,
customer_id integer,
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
    cursor.execute(insert_order_line_sql, (100, 1, 50))
    cursor.execute(insert_order_line_sql, (100, 2, 100))
    cursor.execute(insert_order_sql, (100, 1, "2018-12-01 10:45:15", 1) )

    cursor.execute(insert_order_line_sql, (101, 1, 50))
    cursor.execute(insert_order_line_sql, (101, 2, 100))
    cursor.execute(insert_order_sql, (101, 2, "2018-12-25 10:45:15", 1))
    cursor.close()
    conn.commit()
    conn.close()


class OrderPostgresDaoTests(unittest.TestCase):

    def setUp(self):
        self.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        self.postgresql_instance = self.Postgresql()
        self.dao = OrderPostgresDao(self.postgresql_instance)

    def tearDown(self):
        self.postgresql_instance.stop()
        self.Postgresql.clear_cache()

    def test_00_can_get_orders(self):
        expected = [OrderDto(100, 1, "2018-12-01 10:45:15", 1,
                              [OrderLineDto(100, 1, 50),
                               OrderLineDto(100, 2, 100)]),
                    OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                             [OrderLineDto(101, 1, 50),
                              OrderLineDto(101, 2, 100)])
                    ]
        actual = self.dao.get_orders()
        self.assertEqual(expected, actual)

    def test_01_can_get_order_by_id(self):
        expected = [OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                             [OrderLineDto(101, 1, 50),
                              OrderLineDto(101, 2, 100)])
                    ]
        actual = self.dao.get_order_by_order_id(101)
        self.assertEqual(expected, actual)

    def test_02_can_get_orders_by_customer_id(self):
        expected = [OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                             [OrderLineDto(101, 1, 50),
                              OrderLineDto(101, 2, 100)])
                    ]
        actual = self.dao.get_orders_by_customer_id(2)
        self.assertEqual(expected, actual)

    def test_03_get_orders_by_product_id(self):
        expected = [OrderDto(100, 1, "2018-12-01 10:45:15", 1,
                               [OrderLineDto(100, 2, 100)]),
                    OrderDto(101, 2, "2018-12-25 10:45:15", 1,
                              [OrderLineDto(101, 2, 100)])
                             ]
        actual = self.dao.get_orders_by_product_id(2)
        self.assertEqual(expected, actual)

    def test_04_can_create_an_order(self):
        order = OrderDto(999, 1, "2018-12-01 10:45:15", 1,
                             [OrderLineDto(999, 1, 50),
                              OrderLineDto(999, 2, 100)])
        self.dao.create_order(order)

        actual = self.dao.get_order_by_order_id( 999 )
        self.assertEqual([order], actual)

    def test_05_create_an_order_fails(self):
        order = OrderDto(None, 1, "2018-12-01 10:45:15", 1, [])

        with self.assertRaises(Exception) as e:
            self.dao.create_order(order)

    def test_06_ROLLBACK_has_worked_after_create_order_fails(self):
        order = OrderDto(1000, 1, "2018-12-01 10:45:15", 1,
                                [OrderLineDto(None, 1, 50),
                                OrderLineDto(1000, 2, 100)])

        with self.assertRaises(Exception) as e:
            self.dao.create_order(order)

        actual = self.dao.get_order_by_order_id(1000)
        self.assertEqual([], actual)


if __name__ == '__main__':
    unittest.main()
