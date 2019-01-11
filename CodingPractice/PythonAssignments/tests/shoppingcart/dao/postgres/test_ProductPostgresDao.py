import unittest

import testing.postgresql
import psycopg2

from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import ProductDto
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.ProductPostgresDao import ProductPostgresDao

prod_create_sql = '''
CREATE TABLE product(product_id integer,
name varchar(256),
price float,
weight float,
stock_qty integer, 
vatable integer
);
'''

insert_product_sql = '''
INSERT INTO product(product_id,
name, 
price, 
weight,
stock_qty,
vatable)
VALUES(%s, %s, %s, %s, %s, %s);
'''


def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(prod_create_sql)
    cursor.execute(insert_product_sql,
                   (1, "StandardWidget", 5.1, 100, 10000, 1))
    cursor.execute(insert_product_sql,
                   (2, "ShinyWidget", 35.1, 10, 100, 0))
    cursor.close()
    conn.commit()
    conn.close()


class ProductPostgresDaoTests(unittest.TestCase):

    def setUp(self):
        self.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        self.postgresql_instance = self.Postgresql()
        self.dao = ProductPostgresDao(self.postgresql_instance)

    def tearDown(self):
        self.postgresql_instance.stop()
        self.Postgresql.clear_cache()

    def test_00_create_dto_from_row(self):
        expected = ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                              vatable=True)

        row = [1, "StandardWidget", 5.1, 100, 10000, True]

        actual = ProductPostgresDao._create_product_dto_from_row(row)

        self.assertEqual(expected, actual)

    def test_01_get_product_by_id(self):
        expected = ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                              vatable=True)
        actual = self.dao.get_product_by_id(1)
        self.assertEqual(expected, actual)

    def test_02_get_product_by_name(self):
        expected = [ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                              vatable=True)]
        actual = self.dao.get_products_by_name("StandardWidget")
        self.assertEqual(expected, actual)

    def test_03_get_product_by_less_than_or_equal_to_price(self):
        expected = [ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                               vatable=True)]
        actual = self.dao.get_products_le_price(5.1)
        self.assertEqual(expected, actual)

    def test_04_get_product_by_greater_than_or_equal_to_price(self):
        p1 = ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                               vatable=True)
        p2 = ProductDto(product_id=2, name="ShinyWidget", price=35.1, weight=10, stock_qty=100,
                               vatable=False)
        expected = [p1, p2]
        actual = self.dao.get_products_ge_price(5.1)
        self.assertEqual(expected, actual)

    def test_05_get_product_by_le_stock_qty(self):
        p1 = ProductDto(product_id=1, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                        vatable=True)
        p2 = ProductDto(product_id=2, name="ShinyWidget", price=35.1, weight=10, stock_qty=100,
                        vatable=False)
        expected = [p1, p2]
        actual = self.dao.get_products_le_stock_qty(10000)
        self.assertEqual(expected, actual)

    def test_06_create_product(self):
        prod = ProductDto(product_id=666, name="Panpans", price=78, weight=12, stock_qty=13, vatable=True)
        self.dao.create_product(prod)
        actual = self.dao.get_product_by_id(666)
        self.assertEqual(prod, actual)

    def test_06_no_product_id(self):
        self.assertEqual(None, self.dao.get_product_by_id(99))

    def test_07_no_product_by_name(self):
        self.assertEqual([], self.dao.get_products_by_name('Adrian'))


if __name__ == '__main__':
    unittest.main()
