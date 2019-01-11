from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.ProductDao import ProductDao
from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import ProductDto


class ProductPostgresDao(ProductDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

    INSERT_SQL = '''INSERT INTO product(product_id,
                    product_name,
                    product_price,
                    weight,
                    stock_qty
                    vatable)
                    VALUES(%s, %s, %s, %s, %s, %s);'''

    @staticmethod
    def _create_product_dto_from_row(row):
        return ProductDto(product_id=row[0], name=row[1], price=row[2], weight=row[3], stock_qty=row[4], vatable=row[5])

    def _fetch_products_with_sql(self, sql):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(sql)
            products = cursor.fetchall()
            return [self._create_product_dto_from_row(row) for row in products]

    def get_products(self):
        return self._fetch_products_with_sql('SELECT * FROM product;')

    def get_product_by_id(self, product_id):
        prods = self._fetch_products_with_sql(f'SELECT * FROM product WHERE product_id={product_id};')
        if prods:
            return prods[0]

    def get_products_by_name(self, product_name):
        return self._fetch_products_with_sql("SELECT * FROM product WHERE product_name='"+product_name+"';")

    def get_products_le_price(self, product_price):
        return self._fetch_products_with_sql("SELECT * FROM product WHERE product_price<="+product_price+";")

    def get_products_ge_price(self, product_price):
        return self._fetch_products_with_sql("SELECT * FROM product WHERE product_price>="+product_price+";")

    def get_products_le_stock_qty(self, stock_qty):
        return self._fetch_products_with_sql("SELECT * FROM product WHERE stock_qty<="+stock_qty+ ";")

    def create_product(self, product_dto):
        prod_tuple = (product_dto.get_id(),
                      product_dto.get_name(),
                      product_dto.get_price(),
                      product_dto.get_weight(),
                      product_dto.get_stock_qty,
                      product_dto.is_vatable)
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(self.INSERT_SQL, prod_tuple)
