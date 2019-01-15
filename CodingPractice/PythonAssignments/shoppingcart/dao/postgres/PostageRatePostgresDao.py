from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateDao import PostageRateDao
from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto


class PostageRatePostgresDao(PostageRateDao):

    def __init__(self, postgres_instance):
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())

    INSERT_SQL = '''INSERT INTO postage(country_iso_code,
                    weight,
                    postage_class,
                    rate)
                    VALUES(@s, %s, %s, %s);'''

    @staticmethod
    def _create_postage_rate_dto_from_row(row):
        return PostageRateDto(country_iso_code=row[0], weight=row[1], postage_class=row[2], rate=row[3])

    def _fetch_products_with_sql(self, sql):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(sql)
            postages = cursor.fetchall()
            return [self._create_postage_rate_dto_from_row(row) for row in postages]

    def get_postage_rates(self):
        return self._fetch_products_with_sql('SELECT * FROM postage;')

    def get_postage_rates_by_iso_country_code(self, iso_country_code):
        return self._fetch_products_with_sql("SELECT * FROM postage WHERE iso_country_code='"+iso_country_code+"';")

    def get_postage_rates_by_weight(self, weight):
        return self._fetch_products_with_sql(f"SELECT * FROM postage WHERE weight={weight};")

    def get_postage_rates_by_postage_class(self, postage_class):
        return self._fetch_products_with_sql(f"SELECT * FROM postage WHERE postage_class={postage_class}'")

    def get_postage_rate(self, iso_country_code, weight, postage_class):
        return self._fetch_products_with_sql(
            "SELECT * FROM postage "
            "WHERE iso_country_code='"+iso_country_code+"' AND weight="+weight+" AND postage_class="+postage_class+"';")

    def create_postage_matrix(self, postage_dto):
        postage_tuple = (postage_dto.get_country_iso_code(),
                         postage_dto.get_weight(),
                         postage_dto.get_postage_class(),
                         postage_dto.get_rate())
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute((self.INSERT_SQL, postage_tuple))
