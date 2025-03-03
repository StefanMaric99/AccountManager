# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Assignment2
#Stefan Maric - 101208175


class Account:
    def __init__(self, accNumber, firstname, lastname, balance):
        self.accNumber = accNumber
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def __str__(self):
      return self.firstname + " - " + self.lastname + " - " + str(self.balance)

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
            

    def getAccountNumber(self):
        return self.accNumber

    def getBalance(self, balance):
        return self.balance


def menue():
    print("\n 1. Add Account\n 2. Deposit \n 3. Withdraw \n 4. View Account \n 5. Exit")


def Main():
    arr = []
    menue()

    ipt = int(input("Please choose from the above options: "))

    while ipt >= 1 and ipt <= 4:
        if ipt == 1:
            accNum = int(input("what is your account number? "))
            firstname = input("what is your firstname? ")
            lastname = input("what is your lastname? ")
            balance = float(input("what is your balance? "))
            
            account = Account(accNum, firstname, lastname, balance)
            arr.append(account)
            
            
        elif ipt == 2:
            exist = False
            accId = int(input("account number please "))
            
            for acc in arr:
              if(acc.getAccountNumber() == accId):
                exist = True
                amount = float(input("how much do you want to deposit? "))
                acc.deposit(amount)
                
            if exist == False:
                print("account not found")
            
        elif ipt == 3:
            exist = False
            accId = int(input("account number please "))
            
            for acc in arr:
              if(acc.getAccountNumber() == accId):
                exist = True
                amount = float(input("how much do you want to withdraw? "))
                result = acc.withdraw(amount)
                if result == True:
                    print("${} has been withdrawn".format(amount))
                else:
                    print("you do not have enough balance")
            
            if exist == False:
                print("account not found")
            
        elif ipt == 4:
            exist = False
            accId = int(input("account number please "))

            for acc in arr:
              if(acc.getAccountNumber() == accId):
                exist = True
                print(acc)
            
            if exist == False:
                print("account not found")
            
            
                
                

        menue()
        ipt = int(input("Please choose from the above options: "))
        
    if ipt == 5:
        print("\nExited")
    else:
        print("Wrong input")


Main()
