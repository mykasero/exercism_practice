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
