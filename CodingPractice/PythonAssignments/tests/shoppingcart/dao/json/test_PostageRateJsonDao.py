import unittest
from CodingPractice.PythonAssignments.shoppingcart.dao.json.PostageRateJsonDao import *


class TestPostageJsonDao(unittest.TestCase):

    def setUp(self):
        import os
        dirname = os.path.dirname(__file__)
        fp = os.path.join(dirname, '../../resources/postage_matrix.json')
        self._postDao = PostageRateJsonDao(fp)

    def test_00_get_postage_matrix(self):
        expected = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)
        actual = self._postDao.get_postage_rates()
        self.assertEqual(expected, actual[0])
        self.assertEqual(8, len(actual))

    def test_01_get_postages_by_iso_country_code(self):
        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)
        p2 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='2nd Class', rate=2.95)
        p3 = PostageRateDto(iso_country_code='UK', weight='2kg', postage_class='1st Class', rate=5.50)
        p4 = PostageRateDto(iso_country_code='UK', weight='2kg', postage_class='2nd Class', rate=2.95)
        expected = [p1, p2, p3, p4]
        actual = self._postDao.get_postage_rates_by_iso_country_code('UK')
        self.assertEqual(expected, actual)

    def test_02_get_postages_by_weight(self):
        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)
        p2 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='2nd Class', rate=2.95)
        p3 = PostageRateDto(iso_country_code='USA', weight='1kg', postage_class='1st Class', rate=8.45)
        p4 = PostageRateDto(iso_country_code='USA', weight='1kg', postage_class='2nd Class', rate=7.95)
        expected = [p1, p2, p3, p4]
        actual = self._postDao.get_postage_rates_by_weight('1kg')
        self.assertEqual(expected, actual)

    def test_03_get_postages_by_postage_class(self):
        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)
        p2 = PostageRateDto(iso_country_code='UK', weight='2kg', postage_class='1st Class', rate=5.50)
        p3 = PostageRateDto(iso_country_code='USA', weight='1kg', postage_class='1st Class', rate=8.45)
        p4 = PostageRateDto(iso_country_code='USA', weight='2kg', postage_class='1st Class', rate=15.50)
        expected = [p1, p2, p3, p4]
        actual = self._postDao.get_postage_rates_by_postage_class('1st Class')
        self.assertEqual(expected, actual)

    def test_04_get_postage_rate(self):
        self.assertEqual(3.45, self._postDao.get_postage_rate(iso_country_code='UK', weight=1000, postage_class=1))

    def test_05_MethodNotImplementedException_raised_on_create_postage_rate(self):

        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._postDao.create_postage_rate(p1)
        self.assertEqual('create_postage_rate called on PostageRateJsonDao', e.exception._message)

    def test_06_MethodNotImplementedException_raised_on_delete_postage_rate(self):

        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._postDao.delete_postage_rate(p1)
        self.assertEqual('delete_postage_rate called on PostageRateJsonDao', e.exception._message)

    def test_07_MethodNotImplementedException_raised_on_update_postage_rate(self):

        p1 = PostageRateDto(iso_country_code='UK', weight='1kg', postage_class='1st Class', rate=3.45)

        with self.assertRaises(MethodNotImplementedException) as e:
            self._postDao.update_postage_rate(p1)
        self.assertEqual('update_postage_rate called on PostageRateJsonDao', e.exception._message)


if __name__ == '__main__':
    unittest.main()
