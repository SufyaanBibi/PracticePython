import unittest
from CodingPractice.PythonAssignments.cleancode.BankAccount import BankAccount


class BankAccountTests(unittest.TestCase):

    def test_can_add_bankAccounts(self):
        a = BankAccount('basil', 100.11)
        b = BankAccount('sufi', 100.10)
        self.assertEqual( 200.21, a + b)

    def test_can_subtract_bankAccounts(self):
        a = BankAccount('basil', 100.50)
        b = BankAccount('sufi', 100.10)
        self.assertEqual( 0.40, a - b)

    def test_can_get_1_percent_of_the_balance_in_a_bankAccount(self):
        a = BankAccount('basil', 100.50)
        self.assertEqual( 1.005, a * 0.01)

