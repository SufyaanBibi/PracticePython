from decimal import *


class BankAccount:

    def __init__(self, acct_name, acct_balance):
        self._acct_name = acct_name
        self._balance = Decimal(acct_balance)

    pence = Decimal('.01')

    @staticmethod
    def quantize(deci):
        return deci.quantize(BankAccount.pence, rounding= ROUND_HALF_UP)

    def __add__(self, other_acct):
        new_balance = self._balance + other_acct._balance
        return BankAccount.quantize(new_balance)

    def __sub__(self, other_acct):
        new_balance = self._balance - other_acct._balance
        return BankAccount.quantize(new_balance)

    def __mul__(self, multiple):
        new_balance = self._balance * Decimal(multiple)
        return BankAccount.quantize(new_balance)
