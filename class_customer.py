class Customer:
    def __init__(self, name, address, phone_number, username, password):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.username = username
        self.password = password


    def set_name(self, new_name):                    # functions set are for admin modus.
        self.name = new_name
    def set_address(self, new_address):               # with theese function admin changes information of customers
        self.address = new_address
    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

# function for show customers information

    def __str__(self):
       return f"{self.name}, address: {self.address}, phone number: {self.phone_number}"

