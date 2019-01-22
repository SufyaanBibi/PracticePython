from contextlib import closing
import pg8000

from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateDao import PostageRateDao
from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto
from CodingPractice.PythonAssignments.shoppingcart.dao.PostageRateCache import PostageRateCache


class PostageRatePostgresDao(PostageRateDao, PostageRateCache):

    def __init__(self, postgres_instance):
        super().__init__()
        self._postgres_conn = pg8000.connect(**postgres_instance.dsn())
        self._make_postage_rate_cache(self.get_postage_rates())

    INSERT_SQL = '''INSERT INTO postage_rate(iso_country_code,
                    weight,
                    postage_class,
                    rate)
                    VALUES(%s, %s, %s, %s);'''

    @staticmethod
    def _create_postage_rate_dto_from_row(row):
        return PostageRateDto(iso_country_code=row[0], weight=row[1], postage_class=row[2], rate=row[3])

    def _fetch_products_with_sql(self, sql):
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(sql)
            postages = cursor.fetchall()
            return [self._create_postage_rate_dto_from_row(row) for row in postages]

    def get_postage_rates(self):
        return self._fetch_products_with_sql('SELECT * FROM postage_rate;')

    def get_postage_rates_by_iso_country_code(self, iso_country_code):
        postage = self._fetch_products_with_sql("SELECT * FROM postage_rate WHERE iso_country_code='"+iso_country_code+"';")
        if postage:
            return postage[0]

    def get_postage_rates_by_weight(self, weight):
        return self._fetch_products_with_sql(f"SELECT * FROM postage_rate WHERE weight={weight};")

    def get_postage_rates_by_postage_class(self, postage_class):
        return self._fetch_products_with_sql(f"SELECT * FROM postage_rate WHERE postage_class={postage_class};")

    def get_postage_rate(self, iso_country_code, weight, postage_class):
        key = (iso_country_code, self._convert_weight(weight), postage_class)
        return self._postage_rate_cache[key]

    def create_postage_rate(self, postage_dto):
        weight = self._convert_weight(postage_dto.get_weight())
        postage_tuple = (postage_dto.get_iso_country_code(),
                         weight,
                         postage_dto.get_postage_class(),
                         float(postage_dto.get_rate()))
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(self.INSERT_SQL, postage_tuple)

    def delete_postage_rate(self, postageDto):
        weight = self._convert_weight(postageDto.get_weight())
        iso_country_code = postageDto.get_iso_country_code()
        postage_class = postageDto.get_postage_class()
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"DELETE FROM postage_rate \
                             WHERE iso_country_code='{iso_country_code}' AND weight={weight} AND postage_class={postage_class};")

    def update_postage_rate(self, postageDto):
        iso_country_code = postageDto.get_iso_country_code()
        weight = self._convert_weight(postageDto.get_weight())
        postage_class = postageDto.get_postage_class()
        rate = postageDto.get_rate()
        with closing(self._postgres_conn.cursor()) as cursor:
            cursor.execute(f"UPDATE postage_rate \
                             SET rate={rate} \
                             WHERE iso_country_code='{iso_country_code}' AND weight={weight} AND\
                             postage_class={postage_class};")
