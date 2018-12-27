
class OrderDto:

    def __init__(self, order_id, customer_id, order_timestamp, order_lines, postage):
        self._order_id = order_id
        self._customer_id = customer_id
        self._order_timestamp = order_timestamp
        self._order_lines = order_lines
        self._postage = postage

    def __eq__(self, other):
        return self._order_id == other._order_id and self._customer_id == other._customer_id and self._order_timestamp \
               == other._order_timestamp and self._order_lines == other._order_lines and self._postage == other._postage

    def get_order_id(self):
        return self._order_id

    def get_customer_id(self):
        return self._customer_id

    def get_order_timestamp(self):
        return self._order_timestamp

    def get_order_lines(self):
        return self._order_lines

    def get_postage(self):
        return self._postage


class OrderLineDto:

    def __init__(self, order_id, product_id, qty):
        self._order_id = order_id
        self._product_id = product_id
        self._qty = qty

    def __eq__(self, other):
        return self._order_id == other._order_id and self._product_id == other._product_id and self._qty == other._qty

    def get_order_id(self):
        return self._order_id

    def get_product_id(self):
        return self._product_id

    def get_qty(self):
        return self._qty
