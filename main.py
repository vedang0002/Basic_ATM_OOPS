import sys
import pandas as pd
class ATM():
    def __int__(self,balance=12000,pin='6121'):
        self.balance=balance
        self.pin=pin
    def pin(self):
        for i in range(3):
            p = input('Input your PIN\n')
            if (p == self.pin):
                break
            elif (p != self.pin and i == 2):
                sys.exit()
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
    def check_balance(self):
        print(f'Your current acount\'\s balance is {self.balance}')

df = pd.read_csv("bank_records.csv")
response = input('Press "1" to create a new account or "2" to perform transaction\n')
if (response=='2'):
    x = ATM()
    x.pin()
    print('''Select the number corresponding to your need
    1) Deposit money
    2) Withdraw money
    3) Check current balance
    4) Exit''')
    while True:
        user_command = int(input())
        if (user_command == 1):
            x.deposit()
        elif (user_command == 2):
            x.withdraw()
        elif (user_command == 3):
            x.check_balance()
        else:
            print('Invalid input')
            sys.exit()
elif (response=='1'):
    name = input("Please enter your name\n").upper()
    pin = input("Please enter a for digit number for your PIN\n")
    initial_deposit = float(input("Enter the amount to be deposited"))
    data = {"Name": [name],
            "PIN": [pin],
            "Initial Deposit": [initial_deposit]}
    df2 = pd.DataFrame(data)
    df = df.append(df2)
    sys.exit()