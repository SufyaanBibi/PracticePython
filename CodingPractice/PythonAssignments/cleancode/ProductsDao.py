from abc import ABC, abstractmethod
import json
from CodingPractice.PythonAssignments.cleancode.ProductDetails import *


class ProductsDao(ABC):

    @abstractmethod
    def get_products(self):
        return

    @abstractmethod
    def get_product_by_id(self, product_id):
        return

    @abstractmethod
    def get_products_by_name(self, product_name):
        return

    @abstractmethod
    def get_products_le_price(self, product_price):
        return

    @abstractmethod
    def get_products_ge_price(self, product_price):
        return

    @abstractmethod
    def get_products_le_stock_qty(self, stock_qty):
        return


class ProductsJsonDao(ProductsDao):

    @staticmethod
    def _get_file_path(fn):
        import os
        return os.path.join(os.path.dirname(__file__), fn)

    @staticmethod
    def _get_json(file_name):
        fn = ProductsJsonDao._get_file_path(file_name)
        with open(fn, 'r') as f:
            return json.load(f)

    @staticmethod
    def _create_product(p):
        return ProductDetails(p["product_id"], p["name"], p["price"], p["weight"], p["stock_qty"])

    @staticmethod
    def make_products_from_json(j):
        prods = []
        for prod in j["products"]:
            prods.append(ProductsJsonDao._create_product(prod))
        return prods

    def get_products(self):
        jf = ProductsJsonDao._get_json('products.json')
        return ProductsJsonDao.make_products_from_json(jf)

    def get_product_by_id(self, product_id):
        prods = self.get_products()
        return [prod for prod in prods if product_id == prod.get_id()][0]

    def get_products_by_name(self, product_name):
        prods = self.get_products()
        return [prod for prod in prods if product_name == prod.get_name()]

    def get_products_le_price(self, product_price):
        prods = self.get_products()
        return [prod for prod in prods if product_price <= prod.get_price()]

    def get_products_ge_price(self, product_price):
        prods = self.get_products()
        return [prod for prod in prods if product_price >= prod.get_price()]

    def get_products_le_stock_qty(self, stock_qty):
        prods = self.get_products()
        return [prod for prod in prods if stock_qty <= prod.get_stock_qty()]
