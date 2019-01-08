from decimal import *


class OrderIdNonexistent(Exception):
    def __init__(self, message):
        self.message = message


class CustomerIdNonexistent(Exception):
    def __init__(self, message):
        self.message = message


class VatNegative(Exception):
    def __init__(self, message):
        self.message = message


class InvalidMonth(Exception):
    def __init__(self, message):
        self.message = message


class OrderBo:

    def __init__(self, order_dao, product_dao, cust_dao, postage_matrix):
        self._order_dao = order_dao
        self._product_dao = product_dao
        self._cust_dao = cust_dao
        self._postage_matrix = self._make_dict_from_postage_matrix(postage_matrix)

    @staticmethod
    def _make_dict_from_postage_matrix(postage_matrix):
        postage_dict = {}
        for country, weight, postage_class, price in postage_matrix:
            if weight == '1kg' and postage_class == '1st Class':
                new_weight = 1000
                new_postage_class = 1
                t = (country, new_weight, new_postage_class, price)
                result.append(t)
            elif weight == '1kg' and postage_class == '2nd Class':
                new_weight = 1000
                new_postage_class = 2
                t = (country, new_weight, new_postage_class, price)
                result.append(t)
            elif weight == '2kg' and postage_class == '1st Class':
                new_weight = 2000
                new_postage_class = 1
                t = (country, new_weight, new_postage_class, price)
                result.append(t)
            elif weight == '2kg' and postage_class == '2nd Class':
                new_weight = 2000
                new_postage_class = 2
                t = (country, new_weight, new_postage_class, price)
                result.append(t)
        return result

    pence = Decimal('.01')

    @staticmethod
    def quantize(float_number):
        deci = Decimal(float_number)
        return deci.quantize(OrderBo.pence, rounding=ROUND_HALF_UP)

    def _get_gross_for_order(self, order, vat_rate):
        gross = 0
        for order_line in order.get_order_lines():
            prod_dao = self._product_dao.get_product_by_id(order_line.get_product_id())
            prod_price = prod_dao.get_price()
            quantity = order_line.get_qty()
            price_before_vat = (prod_price * quantity)
            if prod_dao.is_vatable():
                gross += price_before_vat + (price_before_vat * (vat_rate / 100))
            else:
                gross += price_before_vat
        return self.quantize(gross)

    def get_order_total_by_order_id(self, order_id, vat_rate):
        if vat_rate < 0:
            raise VatNegative(f'In order ID {order_id} invalid VAT passed: {vat_rate}')
        order = self._order_dao.get_order_by_order_id(order_id)
        if order:
            return self._get_gross_for_order(order, vat_rate)
        else:
            raise OrderIdNonexistent(f'Order ID {order_id} does not exist.')

    def get_order_total_by_customer_id(self, cust_id, vat_rate):
        if vat_rate < 0:
            raise VatNegative(f'In customer ID {cust_id} invalid VAT passed: {vat_rate}')
        orders = self._order_dao.get_orders_by_customer_id(cust_id)
        gross_price = 0
        if orders:
            for order in orders:
                gross_price += self._get_gross_for_order(order, vat_rate)
        return gross_price

    def get_orders_by_month(self, month_number):
        if month_number < 0 or month_number > 12:
            raise InvalidMonth(f'Month number {month_number} is invalid.')
        orders = self._order_dao.get_orders()
        month_orders = []
        if orders:
            for order in orders:
                timestamp = order.get_order_timestamp()
                month = timestamp[5:7]
                if int(month) == month_number:
                    month_orders.append(order)
        return month_orders

    def get_order_total_by_month(self, month_number, vat_rate):
        if vat_rate < 0:
            raise VatNegative(f'VAT rate {vat_rate} is invalid.')
        elif month_number < 0 or month_number > 12:
            raise InvalidMonth(f'Month number {month_number} is invalid.')
        orders = self.get_orders_by_month(month_number)
        gross_price = 0
        if orders:
            for order in orders:
                gross_price += self._get_gross_for_order(order, vat_rate)
        return gross_price

    def get_postage_cost_by_order_id(self, order_id):
        order = self._order_dao.get_order_by_order_id(order_id)
        c_id = order.get_customer_id()
        postage = order.get_postage()
        cust = self._cust_dao.get_customer_by_id(c_id)
        iso_code = cust.get_iso_country_code()
        order_lines = order.get_order_lines()
        return self._get_postage_rate(iso_code, self._get_order_weight(order_lines), postage)

    def _get_order_weight(self, order_lines):
        weight = 0
        for order_line in order_lines:
            p_id = order_line.get_product_id()
            qty = order_line.get_qty()
            product = self._product_dao.get_product_by_id(p_id)
            product_weight = product.get_weight()
            weight += product_weight * qty
        return weight

    def _get_postage_rate(self, iso_country_code, weight, postage_class):
        if weight < 1000:
            weight = 1000
        elif weight > 1000:
            weight = 2000
        for c_c, w, p_c, rate in self._postage_matrix:
            if c_c == iso_country_code and w == weight and p_c == postage_class:
                return rate

