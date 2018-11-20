import unittest
from CodingPractice.PythonAssignments.cleancode.StockExchangeUtils import uncommon_tickers


class UncommonTickersTests(unittest.TestCase):

    def test_00_uncommon_tickers(self):
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        self.assertEqual({'LXE'}, uncommon_tickers(LON, NYSE))

    def test_01_common_tickers(self):
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        NYSE = {'APPL', 'IBM', 'AAC', 'LXE'}
        self.assertEqual(set(), uncommon_tickers(LON, NYSE))

    def test_02_both_empty(self):
        LON = set()
        NYSE = set()
        self.assertEqual(set(), uncommon_tickers(LON, NYSE))

    def test_03_one_empty(self):
        LON = set()
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        self.assertEqual(set(), uncommon_tickers(LON, NYSE))

    def test_04_the_other_empty(self):
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        NYSE = set()
        self.assertEqual({'IBM', 'APPL', 'AAC', 'LXE'}, uncommon_tickers(LON, NYSE))


if __name__ == '__main__':
    unittest.main()
