import unittest
from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import ProductDto


class ProductDtoTest(unittest.TestCase):

    def test_00_construct_ProductDto(self):
        a = ProductDto(1, 'Gromet', 5.1, 100, 1000, True)
        self.assertEqual(1, a.get_product_id())

    def test_01_equality_operator(self):
        a = ProductDto(1, 'Gromet', 5.1, 100, 1000, True)
        b = ProductDto(1, 'Gromet', 5.1, 100, 1000, True)
        self.assertEqual(a, b)

    def test_02_getter_functions(self):
        a = ProductDto(1, 'Gromet', 5.1, 100, 1000, True)
        self.assertEqual(1, a.get_product_id())
        self.assertEqual('Gromet', a.get_name())
        self.assertEqual(5.1, a.get_price())
        self.assertEqual(100, a.get_weight())
        self.assertEqual(1000, a.get_stock_qty())
        self.assertEqual(True, a.is_vatable())


if __name__ == '__main__':
    unittest.main()
