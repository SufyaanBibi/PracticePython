from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.ProductDao import ProductDao
from CodingPractice.PythonAssignments.shoppingcart.domain.ProductDto import ProductDto


class ProductPostgresDao(ProductDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

    INSERT_SQL = '''INSERT INTO product(
                    name,
                    price,
                    weight,
                    stock_qty,
                    vatable)
                    VALUES(%s, %s, %s, %s, %s)
                    RETURNING product_id;'''

    @staticmethod
    def _int_to_bool(i):
        return i != 0

    @staticmethod
    def _bool_to_int(b):
        if b:
            return 1
        else:
            return 0

    @staticmethod
    def _create_product_dto_from_row(row):
        v = ProductPostgresDao._int_to_bool(row[5])
        return ProductDto(product_id=row[0], name=row[1], price=row[2], weight=row[3], stock_qty=row[4], vatable=v)

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

    def get_products_by_name(self, name):
        return self._fetch_products_with_sql("SELECT * FROM product WHERE name='"+name+"';")

    def get_products_le_price(self, price):
        return self._fetch_products_with_sql(f"SELECT * FROM product WHERE price<={price};")

    def get_products_ge_price(self, price):
        return self._fetch_products_with_sql(f"SELECT * FROM product WHERE price>={price};")

    def get_products_le_stock_qty(self, stock_qty):
        return self._fetch_products_with_sql(f"SELECT * FROM product WHERE stock_qty<={stock_qty};")

    def create_product(self, productDto):
        v = self._bool_to_int(productDto.is_vatable())
        prod_tuple = (productDto.get_name(),
                      float(productDto.get_price()),
                      float(productDto.get_weight()),
                      productDto.get_stock_qty(),
                      v)
        try:
            self._BEGIN()
            with closing(self._postgres_conn.cursor()) as cursor:
                cursor.execute(self.INSERT_SQL, prod_tuple)
                p_id = cursor.fetchall()[0][0]
            self._COMMIT()
            return self.get_product_by_id(p_id)
        except Exception as e:
            self._ROLLBACK()
            raise e

    def delete_product(self, productDto):
        product_id = productDto.get_product_id()
        try:
            self._BEGIN()
            with closing(self._postgres_conn.cursor()) as cursor:
                cursor.execute(f"DELETE FROM product WHERE product_id={product_id};")
            self._COMMIT()
        except Exception as e:
            self._ROLLBACK()
            raise e

    def update_product(self, productDto):
        v = self._bool_to_int(productDto.is_vatable())
        product_id = productDto.get_product_id()
        name = productDto.get_name()
        price = productDto.get_price()
        weight = productDto.get_weight()
        stock_qty = productDto.get_stock_qty()
        vatable = v
        try:
            self._BEGIN()
            with closing(self._postgres_conn.cursor()) as cursor:
                cursor.execute(f"UPDATE product \
                                SET product_id={product_id}, name='{name}', price={price}, weight={weight}, \
                                stock_qty={stock_qty}, vatable={vatable} WHERE product_id={product_id};")
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
