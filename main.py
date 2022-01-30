class ATM():
    def __int__(self,balance=12000,pin=6121):
        self.balance=balance
        self.pin=pin
    def deposit(self):
        amount = float(input("Enter the amount to be deposited\n"))
        self.balance += amount
        print(f'The amount of {amount} has been deposited successfully.')
    def withdraw(self):
        amount = float(input('Enter the amount to be withdrawn\n'))
        if (self.balance-amount)>=0:
            self.balance -=amount
        else:
            print("You have insufficient funds\n")
print("Welcome to SBI!")
