import unittest
from CodingPractice.PythonAssignments.cleancode.StockExchangeUtils import all_tickers


class TestAllTickers(unittest.TestCase):

    def test_00_all_tickers(self):
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        self.assertEqual({'APPL', 'IBM', 'LXE', 'AAC', 'ORCL', 'AAD'}, all_tickers(LON, NYSE))

    def test_01_both_empty(self):
        LON = set()
        NYSE = set()
        self.assertEqual(set(), all_tickers(LON, NYSE))

    def test_02_one_empty(self):
        LON = set()
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        self.assertEqual({'AAD', 'APPL', 'AAC', 'IBM', 'ORCL'}, all_tickers(LON, NYSE))

    def test_03_the_other_empty(self):
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        NYSE = set()
        self.assertEqual({'IBM', 'APPL', 'AAC', 'LXE'}, all_tickers(LON, NYSE))


if __name__ == '__main__':
    unittest.main()
