import unittest
from CodingPractice.PythonAssignments.cleancode.ProductDao import *


class TestProductJsonDao(unittest.TestCase):

    def test_00_get_products(self):
        expected = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p = ProductJsonDao()
        actual = p.get_products()
        self.assertEqual(expected, actual[0])

    def test_01_get_prod_by_id(self):
        expected = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p = ProductJsonDao()
        actual = p.get_product_by_id(1)
        self.assertEqual(expected, actual)

    def test_02_get_prod_by_name(self):
        expected = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p = ProductJsonDao()
        actual = p.get_products_by_name('StandardWidget')
        self.assertEqual(expected, actual[0])

    def test_03_get_prods_by_le_price(self):
        p1 = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p2 = ProductDetails(4, "StandardGrommet", 5.1, 34, 10000)
        expected = [p1, p2]
        p = ProductJsonDao()
        actual = p.get_products_le_price(5.1)
        self.assertEqual(expected, actual)

    def test_04_get_prods_by_ge_price(self):
        p1 = ProductDetails(3, "SuperShinyWidget", 135.1, 15, 10)
        p2 = ProductDetails(6, "SuperShinyGrommet", 135.1, 12, 10)
        expected = [p1, p2]
        p = ProductJsonDao()
        actual = p.get_products_ge_price(100)
        self.assertEqual(expected, actual)

    def test_05_get_prods_by_stock_qty(self):
        p1 = ProductDetails(3, "SuperShinyWidget", 135.1, 15, 10)
        p2 = ProductDetails(6, "SuperShinyGrommet", 135.1, 12, 10)
        expected = [p1, p2]
        p = ProductJsonDao()
        actual = p.get_products_le_stock_qty(50)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
