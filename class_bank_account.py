class BankAccount:
    def __init__(self, username, account_nr, balance):
        self.username = username                              # username of owner (unique)
        self.account_nr = account_nr                      # account number is unique
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')
        self.balance += amount
        print(self)

    def withdraw(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Only numbers are allowed')
        if amount < 0:
            raise ValueError('Only positive values are allowed')
        if amount > self.balance:
            raise ValueError('Deposit some money please')
        self.balance -= amount
        print(self)

    def __str__(self):
       return f"{self.username}, account: {self.account_nr}, balance: {self.balance} € "

    def check_balance(self):
        print(self)

