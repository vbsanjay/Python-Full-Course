# - Encapsulation in programming is a concept where we bundle data (variables) and
#   the methods (functions) that operate on that data into a single unit, called a class.
# - It also restricts direct access to some of the object's components, meaning that the internal
#   representation of an object is hidden from the outside world, and only the methods provided by 
#   the class can be used to interact with the object's data.

class BankAccount:

    def __init__(self, account_number):
        self.__account_number = account_number
        self.__bank_balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__bank_balance += amount
        else:
            print("Amount should be positive")
    
    def withdraw(self, amount):
        if amount <= self.__bank_balance:
            self.__bank_balance -= amount
        else:
            print("Balance Insufficient")
    
    def get_balance(self):
        return self.__bank_balance


myaccount = BankAccount("12345")
print(myaccount.get_balance())
myaccount.deposit(200)
print(myaccount.get_balance())
myaccount.withdraw(100)
print(myaccount.get_balance())





