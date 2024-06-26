class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = False
        self.closed = True

    def get_balance(self):
        if self.closed == True:
            raise ValueError("account not open")
        else:
            return self.balance

    def open(self):
        self.closed = False
        if self.opened == False:
            self.opened = True
        else:
            raise ValueError("account already open")


    def deposit(self, amount):
        if self.closed == True:
            raise ValueError("account not open")
        elif amount < 0:
            raise ValueError("amount must be greater than 0")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.closed == True:
            raise ValueError("account not open")
        elif self.balance < amount:
            raise ValueError("amount must be less than balance")
        elif amount < 0:
            raise ValueError("amount must be greater than 0")
        else:
            self.balance -= amount

    def close(self):
        if self.closed == True:
            raise ValueError("account not open")
        else:
            self.closed = True
            self.opened = False
            self.balance = 0

'''
Instructions
Your task is to implement bank accounts supporting opening/closing, withdrawals, and deposits of money.

As bank accounts can be accessed in many different ways (internet, mobile phones, automatic charges), 
your bank software must allow accounts to be safely accessed from multiple threads/processes 
(terminology depends on your programming language) in parallel. For example, there may be many deposits and withdrawals occurring in parallel; 
you need to ensure there is no race conditions between when you read the account balance and set the new balance.

It should be possible to close an account; operations against a closed account must fail.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/bank-account/canonical-data.json
