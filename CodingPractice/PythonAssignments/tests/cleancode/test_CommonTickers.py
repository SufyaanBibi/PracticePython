import unittest
from CodingPractice.PythonAssignments.cleancode.CommonTickers import *


class CommonTickersTests(unittest.TestCase):

    def test_00_common_tickers(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'APPL' 'IBM', 'LXE', 'AAC'}
        self.assertEqual({'APPL', 'IBM', 'AAC'}, common_tickers(NYSE, LON))


if __name__ == '__main__':
    unittest.main()
