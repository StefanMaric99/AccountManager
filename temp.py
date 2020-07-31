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
        
        
    def getFirstname(self):
        return self.firstname
    
    def getLastname(self):
        return self.lastname

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
    
    def getAccountNumber(self, accNumber):
        return self.accNumber
    
    def getBalance(self, balance):
        return self.balance
    
    
def menue():
    print("1. Add Account\n 2. Deposit \n 3. Withdraw \n 4. View Account \n 5. Exit")
    
    

def Main():
    acc = Account(100, "Joh", "Doe", 100)
    arr = []
    arr.append(acc) 
    menue()
    
    ipt = int(input("Please choose from the above options"))
    
    while ipt >= 1 and ipt <= 4:
        if ipt == 1:
            print("option 1 is")
        elif ipt == 2:
            print("option 2 is")
        elif ipt == 3:
            print("option 3 is")
        elif ipt == 4:
            print("option is 4")
            id = int(input("account number"))
        
        for acc in arr:
            print(acc)
        
        
        menue()
    
        ipt = int(input("Please choose from the above options"))
    
    
Main()    