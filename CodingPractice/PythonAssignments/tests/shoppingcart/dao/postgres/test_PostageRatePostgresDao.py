import unittest

from contextlib import closing
import pg8000
import testing.postgresql
import psycopg2

from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto
from CodingPractice.PythonAssignments.shoppingcart.dao.postgres.PostageRatePostgresDao import PostageRatePostgresDao

postage_create_sql = '''
CREATE TABLE postage_rate(iso_country_code varchar(256),
weight integer, 
postage_class integer,
rate float);
'''

insert_postage_sql = '''
INSERT INTO postage_rate(iso_country_code,
weight,
postage_class,
rate)
VALUES(%s, %s, %s, %s);
'''


def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute(postage_create_sql)
    cursor.close()
    conn.commit()
    conn.close()


class PostageRatePostgresDaoTests(unittest.TestCase):

    #setUpClass/tearDownClass do not delete the database each time.

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

    def setUp(self):
        pg = type(self).postgresql_instance
        connection = pg8000.connect(**pg.dsn())

        with closing(connection.cursor()) as cursor:
            cursor.execute("BEGIN;")
            cursor.execute("DELETE FROM postage_rate;")
            cursor.execute("COMMIT;")
        connection.close()

    def test_00_create_dto_from_row(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        row = ['UK', 1000, 1, 3.45]

        actual = PostageRatePostgresDao._create_postage_rate_dto_from_row(row)

        self.assertEqual(expected, actual)

    def test_01_get_rates_iso_country_code(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        type(self).dao.create_postage_rate(expected)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_02_get_rates_by_weight(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        type(self).dao.create_postage_rate(expected)
        actual = type(self).dao.get_postage_rates_by_weight(1000)
        self.assertEqual([expected], actual)

    def test_03_get_rates_by_postage_class(self):
        expected = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        type(self).dao.create_postage_rate(expected)
        actual = type(self).dao.get_postage_rates_by_postage_class(1)
        self.assertEqual([expected], actual)

    @unittest.skip("We know it fails. Will fix when we fix the caching issue.")
    def test_04_get_appropriate_postage_rate(self):
        p1 = PostageRateDto(iso_country_code='UK', weight=1000, postage_class=1, rate=3.45)
        type(self).dao.create_postage_rate(p1)
        expected = 3.45
        actual = type(self).dao.get_appropriate_postage_rate('UK', 1000, 1)
        self.assertEqual([expected], actual)

    def test_05_create_postage_rate(self):
        postage_dto = PostageRateDto(iso_country_code='SE', weight=2000, postage_class=2, rate=2.34)
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

    def test_09_delete_postage_rate(self):
        post = PostageRateDto(iso_country_code='W', weight=1000, postage_class=2, rate=2.34)
        type(self).dao.create_postage_rate(post)
        type(self).dao.delete_postage_rate(post)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('W')
        self.assertEqual(None, actual)

    def test_10_update_postage_rate(self):
        post = PostageRateDto(iso_country_code='SE', weight=2000, postage_class=2, rate=2.34)
        type(self).dao.create_postage_rate(post)
        expected = PostageRateDto(iso_country_code='SE', weight=2000, postage_class=2, rate=12.34)
        type(self).dao.update_postage_rate(expected)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('SE')
        self.assertEqual(expected, actual)

    def test_11_delete_postage_rate_that_does_not_exist(self):
        post = PostageRateDto(iso_country_code='eee', weight=1000, postage_class=2, rate=2.34)
        type(self).dao.delete_postage_rate(post)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('eee')
        self.assertIsNone(actual)

    def test_12_update_postage_rate_that_does_not_exist(self):
        post = PostageRateDto(iso_country_code='rrr', weight=1000, postage_class=2, rate=2.34)
        type(self).dao.update_postage_rate(post)
        actual = type(self).dao.get_postage_rates_by_iso_country_code('rrr')
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
