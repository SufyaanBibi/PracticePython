
class OrderBo:

    def __init__(self, order_dao, product_dao):
        self._order_dao = order_dao
        self._product_dao = product_dao

    def get_order_total_by_order_id(self, order_id, vat_rate):
        order = self._order_dao.get_order_by_order_id(order_id)
        price_before_vat = 0
        for order_line in order.get_order_lines():
            prod_dao = self._product_dao.get_product_by_id(order_line.get_product_id())
            prod_price = prod_dao.get_price()
            quantity = order_line.get_qty()
            price_before_vat += (prod_price * quantity)
        gross = price_before_vat + (price_before_vat*(vat_rate/100))
        return gross

    def get_order_total_by_customer_id(self, cust_id, vat_rate):
        return

    def get_orders_by_month(self, month_number):
        return

    def get_order_total_by_month(self, month_number, vat_rate):
        return
