import unittest

import testing.postgresql
import psycopg2

from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.PostageRatePostgresDao import PostageRatePostgresDao

postage_create_sql = '''
CREATE TABLE postage_rate(iso_country_code varchar(256),
weight integer, 
postage_class integer,
rates float);
'''

insert_postage_sql = '''
INSERT INTO postage_rate(iso_country_code,
weight,
postage_class,
rates)
VALUES(%s, %s, %s, %s);
'''


def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(postage_create_sql)
    cursor.execute(insert_postage_sql,
                   ('UK', 1000, 1, 3.45))
    cursor.execute(insert_postage_sql,
                   ('USA', 2000, 2, 12.95))
    cursor.close()
    conn.commit()
    conn.close()


class PostageRatePostgresDaoTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        cls.postgresql_instance = cls.Postgresql()
        cls.dao = PostageRatePostgresDao(cls.postgresql_instance)

    @classmethod
    def tearDownClass(cls):
        cls.postgresql_instance.stop()
        cls.Postgresql.clear_cache()

    def test_00_create_dto_from_row(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        row = ['UK', 1000, 1, 3.45]

        actual = PostageRatePostgresDao._create_postage_rate_dto_from_row(row)

        self.assertEqual(expected, actual)

    def test_01_get_rates_iso_country_code(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_02_get_rates_by_weight(self):
        expected = [PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)]
        actual = type(self).dao.get_postage_rates_by_weight(1000)
        self.assertEqual(expected, actual)

    def test_03_get_rates_by_postage_class(self):
        expected = [PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)]
        actual = type(self).dao.get_postage_rates_by_postage_class(1)
        self.assertEqual(expected, actual)

    def test_04_get_postage_rate(self):
        expected = 3.45
        actual = type(self).dao.get_postage_rate('UK', 1000, 1)
        self.assertEqual(expected, actual)

    def test_05_create_postage_dto_with_weight_between_1000_and_2000(self):
        postage_dto = PostageRateDto(iso_country_code='SE', weight=1234, postage_class=2, rate=2.34)
        expected = PostageRateDto(iso_country_code='SE', weight=2000, postage_class=2, rate=2.34)
        type(self).dao.create_postage_rate(postage_dto)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('SE')
        self.assertEqual(expected, actual)

    def test_06_no_iso_country_code(self):
        self.assertEqual(None, type(self).dao.get_postage_rates_by_iso_country_code('TH'))

    def test_07_no_weight(self):
        self.assertEqual([], type(self).dao.get_postage_rates_by_weight(0))

    def test_08_no_postage_class(self):
        self.assertEqual([], type(self).dao.get_postage_rates_by_postage_class(8))


if __name__ == '__main__':
    unittest.main()
