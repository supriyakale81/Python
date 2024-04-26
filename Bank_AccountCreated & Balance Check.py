import re
accounts=[]
class Account:
    def __init__(self,name,contact,account_number,balance):
        self.name=name
        self.contact=contact
        self.account_number=account_number
        self.balance=balance
        print(f"Welcome to the Bank {self.name}")
    def login_details(self,username,Pass):
        self.__username=username
        self.__password=Pass
    def login(self):
        print("Account Holder Name : ",self.name)
        print("Contact : ",self.contact)
        __username=input("Enter the username : ")
        __password=input("Enter the Password : ")
        if (__username==self.__username) and (__password==self.__password):
            print(f"Welcome {self.name}\nYour account Balance :  {self.balance}")
        else:
            print("Your username or password invalid. Please enter the correct username or password ")
    def deposit(self,amount):
        self.balance+=amount
        print(f"Total Balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            print(f"Balance : {self.balance}")
        else:
            print("Insufficient Balance")
    def display(self):
        print(f"Name : {self.name}\nAccount Number : {self.account_number}\nBalance : {self.balance}")
def open_account(accounts):
    name=input("Enter name : ")
    contact=input("Enter contact : ")
    account_no=input("Enter Account Number : ")
    initial_amount=int(input("Enter Initial deposit amount : "))
    new_acc=Account(name,contact,account_no,initial_amount)
    accounts.append(new_acc)
    print("Account created Successfully")
def deposit(accounts):
    account_no = input("Enter the Account number : ")
    amount = float(input("Enter the amount you want to Deposit: "))
    for acc in accounts:
        if acc.account_number == account_no:
            acc.deposit(amount)
            print("Amount Deposited Successfully...")
        else:
            print("Account not found...")
def withdraw(accounts):
    account_no=input("Enter the Account number : ")
    amount = float(input("Enter the amount you want to withdraw: "))
    for acc in accounts:
        if acc.account_number ==account_no:
            acc.withdraw(amount)
            print("Amount Withdraw Successfully...")
        else:
            print("Account not found...")

def check_balance(accounts):
    account_no=input("Enter account number : ")
    for acc in accounts:
        if acc.account_number==account_no:
            acc.display()
        else:
            print("Account not found ")

accounts = []
while True:
    print("\n1. Open Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        open_account(accounts)
    elif choice == '2':
        deposit(accounts)
    elif choice == '3':
        withdraw(accounts)
    elif choice == '4':
        check_balance(accounts)
    elif choice == '5':
        break


# A=Account("Siya",212134,1234321,6300)
# A.display()
# A.login_details('siya23','123456')
# A.login()
