from bank_account import BankAccount
from savings_account import SavingsAccount
from checking_account import CheckingAccount

def run_tests():
    print("\n--- Standard Account Tests ---")
    acc1 = BankAccount("Ajax")
    print(acc1.account_info())
    acc1.deposit(200)
    acc1.deposit(-200)
    acc1.withdraw(50)
    acc1.withdraw(300)
    print(acc1.account_info()+"\n**************************************************************")

    print("\n--- Savings Account Tests ---")
    savings = SavingsAccount("Bob", 1000, 0.05)
    print(savings.account_info())
    savings.deposit(500)
    savings.deposit(-500)
    savings.apply_interest()
    savings.withdraw(2000)
    print(savings.account_info()+"\n**************************************************************")

    print("\n--- Checking Account Tests ---")
    checking = CheckingAccount("Charlie", 500, 2)
    print(checking.account_info())
    checking.deposit(100)
    checking.withdraw(50)
    checking.withdraw(600)
    print(checking.account_info()+"\n**************************************************************")

if __name__ == "__main__":
    run_tests()
