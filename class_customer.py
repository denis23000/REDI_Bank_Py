class Customer:
    def __init__(self, name, address, phone_number, username, password):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.username = username
        self.password = password


    def set_name(self, new_name):
        self.name = new_name
    def set_address(self, new_address):
        self.address = new_address
    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def __str__(self):
       return f"{self.name}, adress: {self.address}, phone number: {self.phone_number}"

