import unittest
from CodingPractice.PythonAssignments.cleancode.ProductDto import ProductDetails


class ProductDetailsTest(unittest.TestCase):

    def test_00_construct_ProductDetails(self):
        a = ProductDetails(1, 'Gromet', 5.1, 100, 1000)
        self.assertEqual(1, a.get_id())

    def test_01_equality_operator(self):
        a = ProductDetails(1, 'Gromet', 5.1, 100, 1000)
        b = ProductDetails(1, 'Gromet', 5.1, 100, 1000)
        self.assertEqual(a, b)

    def test_02_getter_functions(self):
        a = ProductDetails(1, 'Gromet', 5.1, 100, 1000)
        self.assertEqual(1, a.get_id())
        self.assertEqual('Gromet', a.get_name())
        self.assertEqual(5.1, a.get_price())
        self.assertEqual(100, a.get_weight())
        self.assertEqual(1000, a.get_stock_qty())


if __name__ == '__main__':
    unittest.main()

