
class ProductDetails:

    def __init__(self, product_id, name, price, weight, stock_qty):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._weight = weight
        self._stock_qty = stock_qty

    def __eq__(self, other):
        return self._product_id == other._product_id and self._name == other._name and self._price == other._price \
               and self._weight == other._weight and self._stock_qty == other._stock_qty

    def get_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_weight(self):
        return self._weight

    def get_stock_qty(self):
        return self._stock_qty

