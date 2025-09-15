# Import the base class BankAccount
from bank_account import BankAccount

#derived class 1
class SavingsAccount(BankAccount):

    # Constructor initializes inherited attributes (account holder and balance) using the base class,
    # and sets the interest rate specific to the savings account.
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Method to apply interest to the current balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"\nInterest of ${interest:.2f} applied.\nNew balance: ${self.balance:.2f}\n")