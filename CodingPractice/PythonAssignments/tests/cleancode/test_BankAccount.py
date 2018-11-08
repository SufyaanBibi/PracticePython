import unittest
from CodingPractice.PythonAssignments.cleancode.BankAccount import BankAccount
from decimal import *


class BankAccountTests(unittest.TestCase):

    def test_00_can_add_bank_accounts(self):
        a = BankAccount('basil', 100.11)
        b = BankAccount('sufi', 100.10)
        self.assertEqual(Decimal('200.21'), a + b)

    def test_01_can_subtract_bank_accounts(self):
        a = BankAccount('basil', 100.50)
        b = BankAccount('sufi', 100.10)
        self.assertEqual(Decimal('0.40'), a - b)

    def test_02_can_get_1_percent_of_the_balance_in_a_bank_account(self):
        a = BankAccount('basil', 100.50)
        self.assertEqual(Decimal('1.01'), a * 0.01)

    def test_03_can_add_int_bank_accounts(self):
        a = BankAccount('basil', 100)
        b = BankAccount('sufi', 100)
        self.assertEqual(200, a + b)

    def test_04_can_add_0_5(self):
        a = BankAccount('basil', 0.25)
        b = BankAccount('sufi', 0.25)
        self.assertEqual(0.50, a + b)


if __name__ == '__main__':
    unittest.main()
