from CodingPractice.PythonAssignments.shoppingcart.dao.OrderDao import *
from CodingPractice.PythonAssignments.shoppingcart.dao.ProductDao import *


class OrderBo:

    def __init__(self, order_dao, product_dao):
        self._order_dao = order_dao
        self._product_dao = product_dao

    def get_order_total_by_order_id(self, order_id, vat_rate):
        ordr = OrderDao()
        a = ordr.get_order_by_order_id(order_id)
        product_id = [prod for prod in a]     #This is not complete yet. 
        prod = ProductDao()
        prod.get_product_by_id(product_id)

    def get_order_total_by_customer_id(self, cust_id, vat_rate):
        return

    def get_orders_by_month(self, month_number):
        return

    def get_order_total_by_month(self, month_number, vat_rate):
        return
