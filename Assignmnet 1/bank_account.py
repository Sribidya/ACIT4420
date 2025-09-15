class BankAccount:
    # Constructor to initialize account holder and set default balance to 0
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = float(balance)

    # Method to deposit money into the account
    def deposit(self, amount):
        # Convert input to float
        amount = float(amount)  
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}\nNew balance: ${self.balance:.2f}\n")
        else:
            print("Deposit amount must be positive.\nDeposit is not made.\n")

    # Method to withdraw money if sufficient balance is available
    def withdraw(self, amount):
        # Convert input to float
        amount = float(amount) 
        if amount <= 0:
            print("Withdrawal amount must be positive.\n")
            return
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}\nNew balance: ${self.balance:.2f}\n")
        else:
            print(f"Insufficient funds to withdraw ${amount:.2f}.\n")

    # Method to return account information
    def account_info(self):
        return (
            f"Account Information\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance In Account: ${self.balance:.2f}\n"
        )
