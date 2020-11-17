import json
import random
from datetime import datetime
from tkinter import *


with open('accounts.json') as bankFile: 
    bankData = json.load(bankFile) 


class account:
    def __newHistoryEntry(self, entryMessage):
        timestamp = datetime.now()
        self.__history[str(self.__history.__len__())] = str(timestamp.strftime("%m/%d/%Y %H:%M:%S") + " - " + entryMessage)

    def __init__(self, customerName, initialBalance = 0):
        
        # Set the customer name of this account
        self.customerName = customerName

        # Generate a unique ID of this account
        while True:
            self.accountId = random.randint(1, 100000)
            if self.accountId not in bankData:
                break
        
        # Set the initial balance
        self.balance = initialBalance

        # Set an empty history
        self.__history = {}

        # Write creation of account to the history, of this account
        self.__newHistoryEntry("Account created - Name: " + str(self.customerName) + " - AccountID: " + str(self.accountId) + " - Initial Balance: " + str(self.balance))


#####################################################################################################################
#   
#
    def withdrawMoney(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            self.__newHistoryEntry("Withdraw " + str(amount) + ", new balance: " + str(self.balance))

        else:
            print ("Insufficient funds")

    def depositMoney(self, amount):
        self.balance += amount
        self.__newHistoryEntry("Deposit " + str(amount) + ", new balance: " + str(self.balance))

    def getHistory(self):
        for a in self.__history:
            print (self.__history[a])

#####################################################################################################################
#   
#
def withdrawMoneyFromAccout(tag, value, amount):
    with open('accounts.json', 'r') as bankFile:
        # Open the file, save contents in bankData
        bankData = json.load(bankFile)

    for k, v in bankData.items():
        if bankData[k][tag] == value:          

            if bankData[k]['balance'] >= amount:
                bankData[k]['balance'] -= amount
            
        # Dump the new contents to the file, overwriting everything.
    with open('accounts.json', 'w') as bankFile:
        json.dump(bankData, bankFile)

#####################################################################################################################
#   
#
def depositMoneyToAccount(tag, value, amount):
    
    with open('accounts.json', 'r') as bankFile:
        # Open the file, save contents in bankData
        bankData = json.load(bankFile)

    for k, v in bankData.items():
        if bankData[k][tag] == value:            
            bankData[k]['balance'] += amount

        # Dump the new contents to the file, overwriting everything.
    with open('accounts.json', 'w') as bankFile:
        json.dump(bankData, bankFile)

#depositMoneyToAccount(tag="accountId", value=69, amount=5)


