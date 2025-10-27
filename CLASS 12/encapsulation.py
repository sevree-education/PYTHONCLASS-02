import random
class bank_account:
    _id = random.randint(12123213,1232143565656)
    __password = "yasdyui123542lkiadsf"
    __balance = 0
    def __init__(self, name, address, nin):
        self.name = name
        self.address = address
        self.__NIN = nin

    def get_password(self):
        print(self.__password)

    def get_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance = self.__balance + amount


USER1 = {"name" : "OUSSAMA", "bankaccount" : bank_account("OUSSAMA", "AD2", "1001230981239872191239")}
USER1["bankaccount"].get_balance()
USER1["bankaccount"].balance = 1500000
USER1["bankaccount"].deposit(1500)
USER1["bankaccount"].get_balance()

