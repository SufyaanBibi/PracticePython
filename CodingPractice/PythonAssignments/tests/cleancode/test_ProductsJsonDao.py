import unittest
import json
from CodingPractice.PythonAssignments.cleancode.ProductsDao import *


class TestProductJsonDao(unittest.TestCase):

    def test_00_get_products(self):
        expected = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p = ProductsJsonDao()
        actual = p.get_products()
        self.assertEqual(expected, actual[0])

    def test_01_get_prod_by_id(self):
        expected = ProductDetails(1, 'StandardWidget', 5.1, 100, 10000)
        p = ProductsJsonDao()
        actual = p.get_product_by_id(1)
        self.assertEqual(expected, actual)
        

if __name__ == '__main__':
    unittest.main()
