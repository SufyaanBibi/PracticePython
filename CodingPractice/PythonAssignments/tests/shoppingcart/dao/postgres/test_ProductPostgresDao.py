import unittest

import testing.postgresql
import psycopg2
import pg8000
from contextlib import closing

from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import ProductDto
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.ProductPostgresDao import ProductPostgresDao

prod_create_sql = '''
CREATE TABLE product(
product_id SERIAL,
name varchar(256) NOT NULL,
price float,
weight float,
stock_qty integer, 
vatable integer
);
'''


def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(prod_create_sql)
    cursor.close()
    conn.commit()
    conn.close()


class ProductPostgresDaoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        cls.postgresql_instance = cls.Postgresql()
        cls.dao = ProductPostgresDao(cls.postgresql_instance)

    @classmethod
    def tearDownClass(cls):
        cls.postgresql_instance.stop()
        cls.Postgresql.clear_cache()

    def setUp(self):
        pg = type(self).postgresql_instance
        connection = pg8000.connect(**pg.dsn())

        with closing(connection.cursor()) as cursor:
            cursor.execute("BEGIN;")
            cursor.execute("DELETE FROM product;")
            cursor.execute("COMMIT;")
        connection.close()

    def test_00_create_dto_from_row(self):
        expected = ProductDto(product_id=None, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                              vatable=True)

        row = [None, "StandardWidget", 5.1, 100, 10000, True]

        actual = ProductPostgresDao._create_product_dto_from_row(row)

        self.assertEqual(expected, actual)

    def test_01_create_product(self):
        prod = ProductDto(product_id=None, name="Panpans", price=78, weight=12, stock_qty=13, vatable=True)
        new_prod_in_db = type(self).dao.create_product(prod)
        self.assertEqual(prod.get_name(), new_prod_in_db.get_name())
        self.assertEqual(prod.get_price(), new_prod_in_db.get_price())
        self.assertEqual(prod.get_weight(), new_prod_in_db.get_weight())
        self.assertEqual(prod.get_stock_qty(), new_prod_in_db.get_stock_qty())
        self.assertEqual(prod.is_vatable(), new_prod_in_db.is_vatable())

    def test_02_get_product_by_name(self):
        prod = ProductDto(product_id=None, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                               vatable=True)
        prod_in_db = type(self).dao.create_product(prod)
        self.assertEqual(prod.get_name(), prod_in_db.get_name())

    def test_03_get_product_by_less_than_or_equal_to_price(self):
        prod = ProductDto(product_id=None, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                               vatable=True)
        prod_in_db = type(self).dao.create_product(prod)
        actual = type(self).dao.get_products_le_price(5.1)
        self.assertEqual([prod_in_db], actual)

    def test_04_get_product_by_greater_than_or_equal_to_price(self):
        p1 = ProductDto(product_id=None, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                               vatable=True)
        p2 = ProductDto(product_id=None, name="ShinyWidget", price=35.1, weight=10, stock_qty=100,
                               vatable=False)
        prod_1_in_db = type(self).dao.create_product(p1)
        prod_2_in_db = type(self).dao.create_product(p2)
        expected = [prod_1_in_db, prod_2_in_db]
        actual = type(self).dao.get_products_ge_price(5.1)
        self.assertEqual(expected, actual)

    def test_05_get_product_by_le_stock_qty(self):
        p1 = ProductDto(product_id=None, name="StandardWidget", price=5.1, weight=100, stock_qty=10000,
                        vatable=True)
        p2 = ProductDto(product_id=None, name="ShinyWidget", price=35.1, weight=10, stock_qty=100,
                        vatable=False)
        prod_1_in_db = type(self).dao.create_product(p1)
        prod_2_in_db = type(self).dao.create_product(p2)
        expected = [prod_1_in_db, prod_2_in_db]
        actual = type(self).dao.get_products_le_stock_qty(10000)
        self.assertEqual(expected, actual)

    def test_06_no_product_id(self):
        self.assertEqual(None, type(self).dao.get_product_by_id(99))

    def test_07_no_product_by_name(self):
        self.assertEqual([], type(self).dao.get_products_by_name('Panpan'))

    def test_08_delete_product(self):
        prod = ProductDto(product_id=999, name="StWid", price=15.1, weight=120, stock_qty=100,
                        vatable=True)
        type(self).dao.create_product(prod)
        type(self).dao.delete_product(prod)
        actual = type(self).dao.get_product_by_id(999)
        self.assertEqual(None, actual)

    def test_09_update_product(self):
        prod = ProductDto(product_id=None, name="StWid", price=15.1, weight=120, stock_qty=100,
                          vatable=True)
        prod_in_db = type(self).dao.create_product(prod)
        expected = ProductDto(product_id=prod_in_db.get_product_id(), name="StandWid", price=7.1, weight=120, stock_qty=10,
                          vatable=True)
        type(self).dao.update_product(expected)
        actual = type(self).dao.get_product_by_id(prod_in_db.get_product_id())
        self.assertEqual(expected, actual)

    def test_10_delete_product_that_does_not_exist(self):
        prod = ProductDto(product_id=139, name="St", price=13.1, weight=1203, stock_qty=1300,
                          vatable=True)
        type(self).dao.delete_product(prod)
        actual = type(self).dao.get_product_by_id(139)
        self.assertEqual(None, actual)

    def test_11_update_product_that_does_not_exist(self):
        prod = ProductDto(product_id=139, name="St", price=13.1, weight=1203, stock_qty=1300,
                          vatable=True)
        type(self).dao.update_product(prod)
        actual = type(self).dao.get_product_by_id(139)
        self.assertEqual(None, actual)

    def test_12_ROLLBACK(self):
        prod = ProductDto(product_id=None, name=None, price=13.1, weight=1203, stock_qty=1300,
                          vatable=True)

        with self.assertRaises(Exception) as e:
            type(self).dao.create_product(prod)

        actual = type(self).dao.get_products_by_name("Steve")
        self.assertEqual([], actual)

    def test_13_is_vatable_is_bool(self):
        prod = ProductDto(product_id=None, name="Panpans", price=78, weight=12, stock_qty=13, vatable=True)
        new_prod_in_db = type(self).dao.create_product(prod)
        self.assertTrue(new_prod_in_db.is_vatable)


if __name__ == '__main__':
    unittest.main()
