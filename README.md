# ACIT4420 – Assignment 1  
**Problem-Solving with Scripting**  

## Overview
This project implements a simple **banking system** in Python using **object-oriented programming** and **inheritance**.  
The system models three types of accounts:

- **BankAccount** (base class)
- **SavingsAccount** (inherits from BankAccount)
- **CheckingAccount** (inherits from BankAccount)
- **Tests** -All tests for this project are implemented in the `main.py` file
           You can run `main.py` to execute and verify the functionality of the banking system classes.
##  Requirements
- **Python 3.8+** (tested with Python 3.10)  
- No external libraries required — only Python’s standard library is used.
  
## How to Run
1. Clone the repository:
   git clone https://github.com/Sribidya/ACIT4420.git
   
   cd ACIT4420/Assignmnet 1
3. Run 
    python main.py

*Example output:*

--- Standard Account Tests ---

Account Information
Account Holder: Ajax
Balance In Account: $0.00

Deposited $200.00
New balance: $200.00

Deposit amount must be positive.
Deposit is not made.

Withdrew $50.00
New balance: $150.00

Insufficient funds to withdraw $300.00.

Account Information
Account Holder: Ajax
Balance In Account: $150.00

**************************************************************

--- Savings Account Tests ---

Account Information
Account Holder: Bob
Balance In Account: $1000.00

Deposited $500.00
New balance: $1500.00

Deposit amount must be positive.
Deposit is not made.


Interest of $75.00 applied.
New balance: $1575.00

Insufficient funds to withdraw $2000.00.

Account Information
Account Holder: Bob
Balance In Account: $1575.00

**************************************************************

--- Checking Account Tests ---

Account Information
Account Holder: Charlie
Balance In Account: $500.00

Deposited $100.00
New balance: $600.00

Withdrew $50.00 + fee $2.00.
New balance: $548.00

Insufficient funds for withdrawal and transaction fee.

Account Information
Account Holder: Charlie
Balance In Account: $548.00

