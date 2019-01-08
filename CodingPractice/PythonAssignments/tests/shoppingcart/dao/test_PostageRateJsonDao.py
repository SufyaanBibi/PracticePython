'''def test_22_get_postage_rate(self):
    expected = 3.45
    actual = self._orderBo._get_postage_rate('UK', 1000, 1)
    self.assertEqual(expected, actual)


def test_23_weight_under_1000g(self):
    expected = 3.45
    actual = self._orderBo._get_postage_rate('UK', 900, 1)
    self.assertEqual(expected, actual)

    def test_26_postage_matrix_dict(self):
        expected = {('UK', 1000, 1): 3.45,
                    ('UK', 1000, 2): 2.95,
                    ('UK', 2000, 1): 5.5,
                    ('UK', 2000, 2): 2.95,
                    ('USA', 1000, 1): 8.45,
                    ('USA', 1000, 2): 7.95,
                    ('USA', 2000, 1): 15.5,
                    ('USA', 2000, 2): 12.95
                    }
        self.assertEqual(expected, self._orderBo._make_dict_from_postage_matrix(postage_matrix))

'''