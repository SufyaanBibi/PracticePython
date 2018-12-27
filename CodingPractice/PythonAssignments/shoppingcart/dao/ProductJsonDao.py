from CodingPractice.PythonAssignments.shoppingcart.dao.JsonFileReader import JsonFileReader
from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import *
from CodingPractice.PythonAssignments.shoppingcart.dao.ProductDao import *


class ProductJsonDao(ProductDao, JsonFileReader):

    @staticmethod
    def make_products_from_json(j):
        prods = []
        for prod in j["products"]:
            prods.append(ProductJsonDao._create_product(prod))
        return prods

    @staticmethod
    def _create_product(p):
        return ProductDto(p["product_id"], p["name"], p["price"], p["weight"], p["stock_qty"], p["vatable"])

    def __init__(self, json_file_path):
        self._json_file_path = json_file_path

    def get_products(self):
        jf = ProductJsonDao._get_json(self._json_file_path)
        return ProductJsonDao.make_products_from_json(jf)

    def get_product_by_id(self, product_id):
        prods = self.get_products()
        return [prod for prod in prods if product_id == prod.get_id()][0]

    def get_products_by_name(self, product_name):
        prods = self.get_products()
        return [prod for prod in prods if product_name == prod.get_name()]

    def get_products_le_price(self, product_price):
        prods = self.get_products()
        return [prod for prod in prods if prod.get_price() <= product_price]

    def get_products_ge_price(self, product_price):
        prods = self.get_products()
        return [prod for prod in prods if prod.get_price() >= product_price]

    def get_products_le_stock_qty(self, stock_qty):
        prods = self.get_products()
        return [prod for prod in prods if prod.get_stock_qty() <= stock_qty]
