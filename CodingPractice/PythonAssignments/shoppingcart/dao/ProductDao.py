from abc import ABC, abstractmethod


class ProductDao(ABC):

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
