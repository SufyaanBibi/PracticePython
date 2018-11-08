from decimal import *


class BankAccount:

    def __init__(self, acct_num, balance):
        self.acct_num = acct_num
        self.balance = balance

    pence = Decimal('.01')

    def __add__(self, other):
        account_balance = Decimal(self.balance)
        other_balance = Decimal(other.balance)
        new_balance = account_balance + other_balance
        return new_balance.quantize(self.pence, rounding=ROUND_HALF_UP)

    def __sub__(self, other):
        account_balance = Decimal(self.balance)
        other_balance = Decimal(other.balance)
        new_balance = account_balance - other_balance
        return new_balance.quantize(self.pence, rounding=ROUND_HALF_UP)

    def __mul__(self, multiple):
        balance = Decimal(self.balance)
        multiplier = Decimal(multiple)
        new_balance = balance * multiplier
        return new_balance.quantize(self.pence, rounding=ROUND_HALF_UP)
