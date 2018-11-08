import unittest
from CodingPractice.PythonAssignments.cleancode.BankAccount import BankAccount
from decimal import *


class BankAccountTests(unittest.TestCase):

    def test_00_can_add_to_bank_account(self):
        a = BankAccount('basil', 100.10)
        self.assertEqual(BankAccount("basil", 200.20), a + 100.10)

    def test_01_can_subtract_from_bank_account(self):
        a = BankAccount('basil', 200.10)
        self.assertEqual(BankAccount("basil", 99.60), a - 100.5)

    def test_02_can_get_1_percent_of_the_balance_in_a_bank_account(self):
        a = BankAccount('basil', 100.50)
        self.assertEqual(Decimal('1.01'), a * 0.01)


if __name__ == '__main__':
    unittest.main()
