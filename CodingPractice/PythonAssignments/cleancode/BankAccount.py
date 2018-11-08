from decimal import *


class BankAccount:

    def __init__(self, acct_num, acct_balance):
        self.acct_num = acct_num
        self.balance = acct_balance

    pence = Decimal('.01')

    def __add__(self, other_acct):
        acct_balance, other_acct_balance = Decimal(self.balance), Decimal(other_acct.balance)
        new_acct_balance = acct_balance + other_acct_balance
        return new_acct_balance.quantize(self.pence, rounding=ROUND_HALF_UP)

    def __sub__(self, other_acct):
        acct_balance, other_acct_balance = Decimal(self.balance), Decimal(other_acct.balance)
        new_balance = acct_balance - other_acct_balance
        return new_balance.quantize(self.pence, rounding=ROUND_HALF_UP)

    def __mul__(self, multiple):
        acct_balance, multiplier = Decimal(self.balance), Decimal(multiple)
        new_balance = acct_balance * multiplier
        return new_balance.quantize(self.pence, rounding=ROUND_HALF_UP)
