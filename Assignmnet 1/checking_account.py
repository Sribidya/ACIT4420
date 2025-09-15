from bank_account import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee=1.0):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        # Convert input to float
        amount = float(amount)
        total_withdrawal = amount + self.transaction_fee
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if self.balance >= total_withdrawal:
            self.balance -= total_withdrawal
            print(f"Withdrew ${amount:.2f} + fee ${self.transaction_fee:.2f}.\n"
                  f"New balance: ${self.balance:.2f}\n")
        else:
            print("Insufficient funds for withdrawal and transaction fee.\n")
