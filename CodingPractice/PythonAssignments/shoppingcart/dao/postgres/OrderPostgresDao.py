from contextlib import closing
import pg8000
from itertools import groupby


from CodingPractice.PythonAssignments.shoppingcart.dao.OrderDao import OrderDao
from CodingPractice.PythonAssignments.shoppingcart.domain.OrderDto import OrderDto, OrderLineDto


class OrderPostgresDao(OrderDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

    _INSERT_ORDER_SQL = '''INSERT INTO orders(order_id,
                                customer_id,
                                order_timestamp,
                                postage)
                           VALUES(%s, %s, %s, %s);'''

    _INSERT_ORDER_LINE_SQL = '''INSERT INTO order_line(order_id,
                                    product_id, 
                                    qty)
                                VALUES(%s, %s, %s);'''

    _SELECT_SQL = '''SELECT *
                    FROM orders
                    JOIN order_line ON 
                    orders.order_id = order_line.order_id;'''

    def _create_order_line_dto(self, oline):
        return OrderLineDto(order_id=oline[4], product_id=oline[5], qty=oline[6])

    def _create_order_dto(self, order_group_tuple):
        key, g = order_group_tuple
        order_line_dtos= [self._create_order_line_dto(ol) for ol in g]
        order_dto = OrderDto(order_id=key[0], customer_id=key[1], order_timestamp=key[2],
                             postage=key[3], order_lines=order_line_dtos)
        return order_dto

    def _fetch_orders_with_sql(self, sql):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def _order_as_key(self, row):
        return (row[0], row[1], row[2], row[3])

    def get_orders(self):
        all_order_rows = self._fetch_orders_with_sql(OrderPostgresDao._SELECT_SQL)
        grouped  = groupby( all_order_rows, key=self._order_as_key )
        return [self._create_order_dto(og) for og in grouped]

    def get_order_by_order_id(self, order_id):
        sql = f'SELECT * FROM orders \
                JOIN order_line ON orders.order_id = order_line.order_id \
                WHERE orders.order_id={order_id};'
        all_order_rows = self._fetch_orders_with_sql(sql)
        grouped = groupby(all_order_rows, key=self._order_as_key)
        return [self._create_order_dto(og) for og in grouped]

    def get_orders_by_customer_id(self, customer_id):
        sql = f'SELECT * FROM orders \
                JOIN order_line ON orders.order_id = order_line.order_id \
                WHERE orders.customer_id={customer_id};'
        all_order_rows = self._fetch_orders_with_sql(sql)
        grouped = groupby(all_order_rows, key=self._order_as_key)
        return [self._create_order_dto(og) for og in grouped]

    def get_orders_by_product_id(self, product_id):
        sql = f'SELECT * FROM orders \
                JOIN order_line ON orders.order_id = order_line.order_id \
                WHERE order_line.product_id={product_id};'
        all_order_rows = self._fetch_orders_with_sql(sql)
        grouped = groupby(all_order_rows, key=self._order_as_key)
        return [self._create_order_dto(og) for og in grouped]

    def create_order(self, order_dto):
        try:
            self._BEGIN()
            self._save_order_lines(order_dto)
            self._save_order(order_dto)
            self._COMMIT()
        except Exception as e:
            self._ROLLBACK()
            raise e

    def _save_order(self, order_dto):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(self._INSERT_ORDER_SQL, (order_dto.get_order_id(), order_dto.get_customer_id(),
                                                    order_dto.get_order_timestamp(), order_dto.get_postage()))

    def _save_order_lines(self, order_dto):
        for ol in order_dto.get_order_lines():
            with closing(self._postgres_conn.cursor()) as cursor:
                cursor.execute(self._INSERT_ORDER_LINE_SQL, (ol.get_order_id(), ol.get_product_id(), ol.get_qty()))

    def delete_order(self, order_dto):
        order_id = order_dto.get_order_id()
        try:
            self._BEGIN()
            self._delete_orders_and_order_lines(order_id)
            self._COMMIT()
        except Exception as e:
            self._ROLLBACK()
            raise e

    def _delete_orders_and_order_lines(self, order_id):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"DELETE FROM orders \
                            WHERE order_id={order_id};")

        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"DELETE FROM order_line WHERE order_id={order_id};")

    def update_order(self, order_dto):
        try:
            self._BEGIN()
            self._delete_orders_and_order_lines(order_dto.get_order_id())
            self.create_order(order_dto)
            self._COMMIT()
        except Exception as e:
            self._ROLLBACK()
            raise e

    def _BEGIN(self):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute("BEGIN;")

    def _COMMIT(self):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute("COMMIT;")

    def _ROLLBACK(self):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute("ROLLBACK;")
