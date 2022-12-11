from class_bank import Bank
from class_bank_account import BankAccount
from class_customer import Customer

redi_bank = Bank("REDI_bank")

customer_iggy = Customer(name="Iggy Pop", address="Munich", phone_number="+49-025-45", username="iggy", password="123")
customer_bob = Customer(name="Bob Marley", address="Jamaica", phone_number="+39-01-88", username="bob", password="222")

redi_bank.customers.append(customer_iggy)

account_iggy_1 = BankAccount(username="iggy", account_nr=1, balance=1000)
account_iggy_2 = BankAccount(username="iggy", account_nr=2, balance=2000)
account_iggy_3 = BankAccount(username="iggy", account_nr=3, balance=3000)

redi_bank.customers.append(customer_bob)

account_bob_1 = BankAccount(username="bob", account_nr=1, balance=1000)
account_bob_2 = BankAccount(username="bob", account_nr=2, balance=2000)
account_bob_3 = BankAccount(username="bob", account_nr=3, balance=3000)

redi_bank.bankaccounts.append(account_iggy_1)
redi_bank.bankaccounts.append(account_iggy_2)
redi_bank.bankaccounts.append(account_iggy_3)

redi_bank.bankaccounts.append(account_bob_1)
redi_bank.bankaccounts.append(account_bob_2)
redi_bank.bankaccounts.append(account_bob_3)

redi_bank.start()