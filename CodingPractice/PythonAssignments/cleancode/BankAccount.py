from decimal import *


class BankAccount:

    def __init__(self, acct_name, acct_balance):
        self._acct_name = acct_name
        self._balance = BankAccount.quantize(Decimal(acct_balance))

    pence = Decimal('.01')

    @staticmethod
    def quantize(deci):
        return deci.quantize(BankAccount.pence, rounding=ROUND_HALF_UP)

    def __add__(self, ammount):
        new_balance = self._balance + Decimal(ammount)
        quantized = BankAccount.quantize(new_balance)
        return BankAccount(self._acct_name, quantized)

    def __sub__(self, ammount):
        new_balance = self._balance - Decimal(ammount)
        quantized = BankAccount.quantize(new_balance)
        return BankAccount(self._acct_name, quantized)

    def __mul__(self, multiple):
        new_balance = self._balance * Decimal(multiple)
        return BankAccount.quantize(new_balance)

    def __eq__(self, other):
        return self._balance == other._balance and self._acct_name == other._acct_name
