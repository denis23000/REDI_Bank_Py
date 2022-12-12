from class_customer import Customer
from class_bank_account import BankAccount

# in class bank happen all actions

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []                   # in the list customers saved all user, objects from class Customers
        self.pin_admin = "1111"               # password for admin
        self.bankaccounts = []

    def start(self):                           # the programm starts hier, from start.
        first_choise = "3"                     # a user can choose to work as a customer or as an admin
        while first_choise == "3":
            first_choise = input('Welcome to REDI Bank! 1. Customer, 2. Admin, 3. Exit')
            if first_choise == "3":
                print("Goodbye and have a nice day!")
            elif first_choise == "1":
                self.work_as_customer()
            elif first_choise == "2":
                self.work_as_admin()
            else:
                print("invalid input, try again")

    def work_as_customer(self):   # if user chosen to work as a customer, user comes hier and can create new useraccount
        customer_choise = "4"                                               # or login in a created useraccount
        while customer_choise == "4" or customer_choise == "3":
            customer_choise = input("1. Login, 2. Signup, 3. Previous menu, 4. exit")
            if customer_choise == "4":
                print("Goodbye and have a nece day!")
            elif customer_choise == "3":
                self.start()
            elif customer_choise == "2":
                self.new_customer()
            elif customer_choise == "1":
                self.check_pin()
            else:
                print("invalid input, try again")
                self.work_as_customer()

    def new_customer(self):                         # creating a new useraccount
        name = input("Enter your name ")
        address = input("Enter your address ")
        phone_number = input("Enter your phone number ")
        x = 0
        while x != 1:
            username_input = input("Create your username: ")                    # username must be unique
            for i in self.customers:
                if i.username == username_input:                         # checking if username already not exist
                    print("This name already exist. Try again ")
                else:
                    x += 1
            break
        username = username_input
        password = input("Create your password ")
        new_customer = Customer(name=name, address=address,     # creating new useraccount(new customer)
                                phone_number=phone_number,      # with constructor from class Customer
                                username=username,
                                password=password)
        self.customers.append(new_customer)                    # saving new useraccount in the customers list
        print("Customer created")
        self.work_as_customer()                  # switching to the working area "work as customer"

    def check_pin(self):
        username_input = input('Enter your username')
        password_input = input('Enter your password')
        for i in self.customers:
            if username_input in i.username:
                 if password_input in i.password:
                    work_customer = i
                    self.work_as_customer_in(customer=work_customer)

        print("Invalid username or password, try again")
        self.check_pin()




    def work_as_customer_in(self, customer: Customer):
        print("Welcome " + customer.name)
        customer_in_choise = "6"
        while customer_in_choise == "5" or customer_in_choise == "6":
            customer_in_choise = input(
                "1.Create new bankaccount, 2.Show bankaccounts, 3.Withdrow, 4.Deposit, 5.Previous menu, 6.Exit")
            if customer_in_choise == "1":
                self.new_bankaccount()
            elif customer_in_choise == "2":
                for i in self.bankaccounts:
                    print(i)
            elif customer_in_choise == "3":
                amount = input("Enter an amount ")
                if len(self.bankaccounts) > 1:
                    wich_account = input("Enter account nummer")
                    for i in self.bankaccounts:
                        if i.account_nr == wich_account:
                            this_account = i
                            this_account.withdrow(amount)
                else:
                    self.bankaccounts[0].withdrow(amount)
            elif customer_in_choise == "4":
                amount = input("Enter an amount ")
                if len(self.bankaccounts) > 1:
                    wich_account = input("Enter account nummer")
                    for i in self.bankaccounts:
                        if i.account_nr == wich_account:
                            this_account = i
                            this_account.deposit(amount)
                else:
                    self.bankaccounts[0].deposit(amount)
            elif customer_in_choise == "5":
                self.work_as_customer()
            elif customer_in_choise == "6":
                print("Goodbye and have a nece day!")


    def work_as_admin(self):
        customer_choise = "3"
        while customer_choise == "3" or customer_choise == "2":
            customer_choise = input("1. Login, 2. Previous menu, 3. Exit")
            if customer_choise == "3":
                print("Goodbye and have a nece day!")
            elif customer_choise == "2":
                self.start()
            elif customer_choise == "1":
                self.check_pin_admin()
            else:
                print("invalid input, try again")

    def check_pin_admin(self):
        trying = 3
        while trying != 0:
            pin_admin_input = input("Enter admin's pin ")
            if pin_admin_input == self.pin_admin:
                self.work_as_admin_in()
            else:
                trying = trying - 1
                print("invalid admin's pin. You have {} tries left. ".format(trying))
                if trying == 0:
                    print("Sorry, You can't try again :(")

    def work_as_admin_in(self):
        admin_choise = "5"
        while admin_choise == "4" or admin_choise == "5":
            admin_choise = input(
                "Welcome admin: 1.Show customers, 2.Delete customers, 3.Update a customer info, 4.Previous menu, 5.Exit")
            if admin_choise == "5":
                print("Goodbye and have a nece day!")
            elif admin_choise == "4":
                self.work_as_admin()
            elif admin_choise == "3":
                update_data = "5"
                while update_data == "5" or update_data == "4":
                    update_data = input(
                        "1.Update the address, 2.Update the phone number, "
                        "3.Update the password, 4.Previous menu, 5.Exit ")
                if update_data == "5":
                    print("Goodbye and have a nece day!")
                elif update_data == "4":
                    self.work_as_admin_in()
                elif update_data == "3":
                    new_password = input("Enter new password ")
                    for_customer = input("For wich customer is this new password? Enter the username of the customer ")
                    for i in self.customers:
                        if i.username == for_customer:
                            i.password = new_password
                            print("Done. New password saved. ")
                            self.work_as_admin_in()
                elif update_data == "2":
                    new_phone_number = input("Enter new phone number ")
                    for_customer = input("For wich customer is this new phone number? "
                                         "Enter the username of the customer")
                    for i in self.customers:
                        if i.username == for_customer:
                            i.phone_number = new_phone_number
                            print("Done. New phone number saved. ")
                            self.work_as_admin_in()
                elif update_data == "1":
                    new_address = input("Enter new address ")
                    for_customer = input("For wich customer is this new address? Enter the name of the customer ")
                    for i in self.customers:
                        if i.username == for_customer:
                            i.address = new_address
                            print("Done. New address saved. ")
                            self.work_as_admin_in()
            elif admin_choise == "2":
                for i in self.customers:
                    print(i)

    def new_bankaccount(self):
        username = input("Enter your name ")
        acc_nr = 1
        for i in self.bankaccounts:
            if i.account_nr > acc_nr:
                acc_nr = i.account_nr
                acc_nr += 1
        balance = int(input("Enter your start balance "))
        new_account = BankAccount(username=username, account_nr=acc_nr, balance=balance)
        self.bankaccounts.append(new_account)
        print("Your new account successfully created.")
        self.work_as_customer()




