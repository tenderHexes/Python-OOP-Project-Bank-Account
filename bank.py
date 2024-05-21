
import random
import re
class Bank:
    transactionList = None
    password = None
    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.balance = balance
        x = random.randint(1111111,9999999)
        self.id = str(x)
    def __str__(self):
        return f"name: {self.name}, address: {self.address}, balance: {self.balance}, id: {self.id}"

#functionalities

    def withdrawDepositTransactions(self):
        transactionList = []

        while True:
            print("press d for deposit, w for withdraw, q to return to the main menu, t to see transaction history")
            choice2 = input()
            if choice2 == "d":
                print("choose amount to deposit")
                amount = float(input())

                setattr(account, "balance", float(self.balance))
                self.balance += amount
                print("balance updated!")
                formatted_balance = "{:.2f}".format(self.balance)
                print("your balance is" +" " + str(formatted_balance))
                # adding a "d" to identify amount as a deposited amount
                transactionList.append(str(amount) + "d")
            transactionList1 = transactionList

            if choice2 == "w":
                print("choose amount to withdraw")
                amount = float(input())
                if amount > self.balance:
                    print("insuficient funds in your balance ")
                if amount <= self.balance:
                    self.balance -= amount
                    print("balance updated!")
                    formatted_balance = "{:.2f}".format(self.balance)
                    print("your balance is" + " " + str(formatted_balance))
                    #adding a "w" to identify amount as a withdrew amount
                    transactionList1.append(str(amount) + "w")
            transactionList2 = transactionList1

            if choice2 == "t":

                for x in transactionList2:
                    if "d" in str(x):
                        amount = float(x.replace("d", ""))
                        formatted_amount = "{:.2f}".format(amount)
                        print("you've deposit " + str(formatted_amount))

                    if "w" in str(x):
                        amount = float(x.replace("w", ""))
                        formatted_amount = "{:.2f}".format(amount)
                        print("You've withdrawn " + formatted_amount)

            if choice2 == "b":
                    print(self.balance)

            if choice2 == "q":
                break
            if all(char not in choice2 for char in "dwbtq"):
                print("Please choose the correct input")
                continue
        transactionList2 = transactionList1
        setattr(self, "transactionList", transactionList2)





    def balanceInquiry(self):
        print("your balance is" + " " + str(self.balance))

    def transactionHistory(self,transactionList2):
     if transactionList2 is not None: #incase user has made no transactions
        for x in transactionList2: # to format and print
            if "d" in str(x):
                amount = float(x.replace("d", ""))
                formatted_amount = "{:.2f}".format(amount)
                print("you've deposit " + str(formatted_amount))

            if "w" in str(x):
                amount = float(x.replace("w", ""))
                formatted_amount = "{:.2f}".format(amount)
                print("You've withdrawn " + formatted_amount)
            if "d" or "w" not in str(x):
                print("No transactions has been made")
     else:
         print("No transactions made")

    def accountManagement(self):
        print("List of accounts")
        num = 0
        for x in accountList:
            num += 1
            print("account" + str(num) + ": " + str(x))
        print("Press T if you would like to transfer funds to another account. Press any key to (q*?)quit")
        transferringFundsOrNot = input()
        if transferringFundsOrNot == "T":
            self.transferFund()
        else:
            pass

    def transferFund(self):
        print("To choose an account to retrieve funds from, type its id.")
        idAccountRetrievingFrom = str(input())
        for account in accountList:
            if getattr(account, "id") == idAccountRetrievingFrom:
                print("Selected account:", account)
                print("Select the amount to retrieve from")
                amountToRetrieve = float(input())
                print(account.balance)
                updatedBalanceAfterRetrieving = account.balance - amountToRetrieve
                print("your balance for this account is:  " + str(updatedBalanceAfterRetrieving))
                print("Now to choose the account to transfer funds to, type its id")
                idAccountTransferringTo = str(input())
                for account in accountList:
                    if getattr(account, "id") == idAccountTransferringTo:
                        print("Selected account:", account)
                        transferredUpdatedBalance = float(account.balance) + float(amountToRetrieve)
                        print("your balance for this account is:  " + str(transferredUpdatedBalance))




    def switch(self, choice):
        match choice:
            case 1:
                self.withdrawDepositTransactions()

            case 2:
                self.balanceInquiry()

            case 3:
                self.transactionHistory(self.transactionList)


            case 4:
                self.accountManagement()

            case _:
                self.default_case()

def passwordCreation():




    while True:
        print("Please create a password")
        print()
        print("Password must be minimum 8 characters long")
        print("Password must contain at least one uppercase letter")
        print("Password must contain at least one lowercase letter")
        print("Password must contain at least one number")


        password = input()
        if len(password) < 8:
            print("Password must be minimum 8 characters long")
            continue
        elif not re.search("[A-Z]", password):
            print("Password must contain at least one uppercase letter")
            continue
        elif not re.search("[a-z]",password):
            print("Password must contain at least one lowercase letter")
            continue
        elif not re.search("[0-9]", password):
            print("Password must contain at least one number")
            continue
        print("Password accepted")

        break
    return getPassword(password)


def getPassword(thePassword):

    return thePassword


def authentification(thePassword):
    getPassword()
    print("Please enter your password")

    tryPassword = input()



accountList = []
idAccountRetrievingFrom = 0
while True:
    print("press Y to create an account, L to login, Q to quit")
    creatingAccountorNot = input()
    if creatingAccountorNot == "Y":
        ########Creating password#######
        while True:
            print("Please create a password")
            print("Password must be minimum 8 characters long")
            print("Password must contain at least one uppercase letter")
            print("Password must contain at least one lowercase letter")
            print("Password must contain at least one number")

            password = input()
            if len(password) < 8:
                print("Password must be minimum 8 characters long")
                continue
            elif not re.search("[A-Z]", password):
                print("Password must contain at least one uppercase letter")
                continue
            elif not re.search("[a-z]", password):
                print("Password must contain at least one lowercase letter")
                continue
            elif not re.search("[0-9]", password):
                print("Password must contain at least one number")
                continue
            print("Password accepted")
            break
        ########End of Creation of the password#########

        #####Creating account######
        print("your name?")
        name = input()
        print("your address?")
        address = input()
        balance = 0.00
        formatted_balance = "{:.2f}".format(balance)
        account = Bank(name,address,formatted_balance)
        accountList.append(account)
        print("congratulation, you've created your account!")
        print("your balance is" + " " + str(formatted_balance))
        theAccount = account
        while True:
         choice = int(input("Enter your choice:\n press 1 to deposit or withdraw \n press 2 to see your balance \n press 3 to see transaction history \n press 4 to see your accounts \n press 5 to quit"))
         if choice == 5:
           break
         account.switch(choice)



    if creatingAccountorNot == "L":
       print("Please enter password")
       userPassword = input()
       try:
           if password == userPassword:
               print("Correct password!")
               while True:
                   choice = int(input("Enter your choice:\n press 1 to deposit or withdraw \n press 2 to see your balance \n press 3 to see transaction history \n press 4 to see your accounts \n press 5 to quit"))

                   if choice == 5:
                       break
                   account.switch(choice)

       except NameError:
         print("Incorrect password")

    if creatingAccountorNot == "Q":
     print("Have a good day!")
     break
    else:
       pass


