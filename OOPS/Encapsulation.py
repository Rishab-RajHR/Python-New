# Encapsulation is about bundling data and methods together inside a class, and restricting direct access to internal state. 

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance # Private attribute
    def deposit(self, amount):
        self.__balance += amount
    def getBalance(self):
        return self.__balance
    
acc = BankAccount("Alex", 1000)
acc.deposit(500)
print(acc.getBalance())
print(acc.__balance) # This will raise an error because __balance is private and cannot be accessed directly.
    