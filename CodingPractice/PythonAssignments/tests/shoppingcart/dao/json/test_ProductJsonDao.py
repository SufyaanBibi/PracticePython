import unittest
from CodingPractice.PythonAssignments.shoppingcart.dao.json.ProductJsonDao import *


class TestProductJsonDao(unittest.TestCase):
    
    def setUp(self):
        import os
        dirname = os.path.dirname(__file__)
        fp = os.path.join(dirname, '../../resources/products.json')
        self._prodDao = ProductJsonDao(fp)

    def test_00_get_products(self):
        expected = ProductDto(product_id=1, name='StandardWidget', price=5.1, weight=100, stock_qty=10000, vatable=True)
        
        actual = self._prodDao.get_products()
        self.assertEqual(expected, actual[0])

    def test_01_get_prod_by_id(self):
        expected = ProductDto(product_id=1, name='StandardWidget', price=5.1, weight=100, stock_qty=10000, vatable=True)
        
        actual = self._prodDao.get_product_by_id(1)
        self.assertEqual(expected, actual)

    def test_02_get_prod_by_name(self):
        expected = ProductDto(product_id=1, name='StandardWidget', price=5.1, weight=100, stock_qty=10000, vatable=True)
        
        actual = self._prodDao.get_products_by_name('StandardWidget')
        self.assertEqual(expected, actual[0])

    def test_03_get_prods_by_le_price(self):
        p1 = ProductDto(product_id=1, name='StandardWidget', price=5.1, weight=100, stock_qty=10000, vatable=True)
        p2 = ProductDto(product_id=4, name="StandardGrommet", price=5.1, weight=34, stock_qty=10000, vatable=False)
        expected = [p1, p2]
        
        actual = self._prodDao.get_products_le_price(5.1)
        self.assertEqual(expected, actual)

    def test_04_get_prods_by_ge_price(self):
        p1 = ProductDto(product_id=3, name="SuperShinyWidget", price=135.1, weight=150, stock_qty=10, vatable=True)
        p2 = ProductDto(product_id=6, name="SuperShinyGrommet", price=135.1, weight=1200, stock_qty=10, vatable=True)
        expected = [p1, p2]
        
        actual = self._prodDao.get_products_ge_price(100)
        self.assertEqual(expected, actual)

    def test_05_get_prods_by_stock_qty(self):
        p1 = ProductDto(product_id=3, name="SuperShinyWidget", price=135.1, weight=150, stock_qty=10, vatable=True)
        p2 = ProductDto(product_id=6, name="SuperShinyGrommet", price=135.1, weight=1200, stock_qty=10, vatable=True)
        expected = [p1, p2]
        
        actual = self._prodDao.get_products_le_stock_qty(50)
        self.assertEqual(expected, actual)

    def test_05_MethodNotImplementedException_raised_on_create_product(self):
        prod1 = ProductDto(product_id=99, name="Wrow", price=3445, weight=987, stock_qty=133, vatable=True)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._prodDao.create_product(prod1)
        self.assertEqual('create_product called on ProductJsonDao', e.exception._message)

    def test_06_MethodNotImplementedException_raised_on_delete_product(self):
        prod1 = ProductDto(product_id=99, name="Wrow", price=3445, weight=987, stock_qty=133, vatable=True)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._prodDao.delete_product(prod1)
        self.assertEqual('delete_product called on ProductJsonDao', e.exception._message)

    def test_07_MethodNotImplementedException_raised_on_update_product(self):
        prod1 = ProductDto(product_id=99, name="Wrow", price=3445, weight=987, stock_qty=133, vatable=True)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._prodDao.update_product(prod1)
        self.assertEqual('update_product called on ProductJsonDao', e.exception._message)


if __name__ == '__main__':
    unittest.main()
