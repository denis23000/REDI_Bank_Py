from class_bank_account import BankAccount

class Customer:
    def __init__(self, name, address, phone_number, username, password):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.accounts = []

    def show_bankaccounts(self):
        for i in self.accounts:
            if i.username == self.username:
                i.check_balance()

    def __str__(self):
       return f"{self.name}, adress: {self.address}, phone number: {self.phone_number}"

    def new_account(self):
        username = input("Enter your name ")
        acc_nr = 1
        for i in self.accounts:
            if i.account_nr > acc_nr:
                acc_nr = i.account_nr
                acc_nr += 1
        balance = int(input("Enter your start balance "))
        new_account = BankAccount(username=username, account_nr=acc_nr, balance=balance)
        self.accounts.append(new_account)
        print("Your new account successfully created.")
        new_account.work_as_customer()