class BankAccount:

    def __init__(self, acct_num, balance):
        self.acct_num = acct_num
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __mul__(self, other):
        return self.balance * other
