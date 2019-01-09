import unittest
from CodingPractice.PythonAssignments.shoppingcart.domain.PostageRateDto import PostageRateDto


class TestPostageRateDto(unittest.TestCase):

    def test_00_construct_PostageRateDto(self):
        a = PostageRateDto('UK', '1kg', '1st Class', 3.45)
        self.assertEqual('UK', a.get_country_iso_code())

    def test_01_equality_operator(self):
        a = PostageRateDto('UK', '1kg', '1st Class', 3.45)
        b = PostageRateDto('UK', '1kg', '1st Class', 3.45)
        self.assertEqual(a, b)

    def test_02_getter_functions(self):
        a = PostageRateDto('UK', '1kg', '1st Class', 3.45)
        self.assertEqual('UK', a.get_country_iso_code())
        self.assertEqual('1kg', a.get_weight())
        self.assertEqual('1st Class', a.get_postage_class())
        self.assertEqual(3.45, a.get_rate())


if __name__ == '__main__':
    unittest.main()
