import sys
import pandas as pd
class ATM():
    def pin(self,var):
        for i in range(3):
            p = int(input('Input your PIN\n'))
            if (p == df["PIN"][var]):
                break
            elif (p != df["PIN"][var] and i == 2):
                sys.exit()
    def deposit(self,var):
        amount = float(input("Enter the amount to be deposited\n"))
        df["Balance"][var] += amount
        print(f'The amount of {amount} has been deposited successfully.')
    def withdraw(self,var):
        amount = float(input('Enter the amount to be withdrawn\n'))
        if (df["Balance"][var]-amount)>=0:
            df["Balance"][var] -=amount
        else:
            print("You have insufficient funds\n")
    def check_balance(self,var):
        print(f'Your current acount\'\s balance is {df["Balance"][var]}')
df = pd.read_csv("Bank_Records.csv")
response = input('Press "1" to create a new account or "2" to perform transaction\n')
if (response=='2'):
    name = input("Please enter your name: ")
    name = name.upper()
    for i in range(len(df["Name"])+1):
      if (name == df["Name"][i]):
        var = i
        x = ATM()
        x.pin(var)
        print('''Select the number corresponding to your need
        1) Deposit money
        2) Withdraw money
        3) Check current balance
        4) Exit''')
        while True:
            user_command = int(input())
            if (user_command == 1):
                x.deposit(var)
            elif (user_command == 2):
                x.withdraw(var)
            elif (user_command == 3):
                x.check_balance(var)
            else:
                print('Invalid input')
                sys.exit()
    print("Name not found. Please try again from the start")
    sys.exit()
elif (response=='1'):
    name = input("Please enter your name\n").upper()
    pin = input("Please enter a for digit number for your PIN\n")
    initial_deposit = float(input("Enter the amount to be deposited"))
    data = {"Name": [name],
            "PIN": [pin],
            "Balance": [initial_deposit]}
    df2 = pd.DataFrame(data)
    df = df.append(df2)
    sys.exit()
else:
  sys.exit()