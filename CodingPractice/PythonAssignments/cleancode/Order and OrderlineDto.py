
class OrderDto:

    def __init__(self, order_id, customer_id, order_timestamp, order_lines):
        self._order_id = order_id
        self._customer_id = customer_id
        self._order_timestamp = order_timestamp
        self._order_lines = order_lines

    def get_order_id(self):
        return self._order_id

    def get_customer_id(self):
        return self._customer_id

    def get_order_timestamp(self):
        return self._order_timestamp


