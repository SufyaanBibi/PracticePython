import unittest
from CodingPractice.PythonAssignments.cleancode.StockExchangeUtils import has_common_tickers


class TestHasCommonTickers(unittest.TestCase):

    def test_00_has_common_tickers(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        self.assertTrue(has_common_tickers(NYSE, LON))

    def test_01_has_common_tickers(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'LXE', 'IBM', 'LON.SE'}
        self.assertTrue(has_common_tickers(NYSE, LON))

    def test_02_no_common_tickers(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'LXE', 'LON.SE'}
        self.assertFalse(has_common_tickers(NYSE, LON))

    def test_03_has_no_common_tickers(self):
        NYSE = set()
        LON = {'LXE', 'LON.SE'}
        self.assertFalse(has_common_tickers(NYSE, LON))


if __name__ == '__main__':
    unittest.main()
