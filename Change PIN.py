
class Account:
    def __init__(self,name,contact,account_number,balance):
        self.name=name
        self.contact=contact
        self.account_number=account_number
        self.balance=balance
        self.__username=None
        self.__password=None
        print(f"Welcome to the Bank {self.name}")
    def login_details(self,username,Pass):
        self.__username=username
        self.__password=Pass
    def deposit(self, amount):
        self.balance += amount
        print(f"Total Balance: {self.balance}")
    def transfer(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Balance : {self.balance}")
        else:
            print("Insufficient Balance")
    def display(self):
        print(f"Name : {self.name}\nAccount Number : {self.account_number}\nBalance : {self.balance}")
def login(accounts):
    username=input("Enter the username : ")
    password=input("Enter the Password : ")
    for acc in accounts:
        if (username==acc.__username) and (password==acc.__password):
            print(f"Welcome {acc.name}")
            while True:
                print("\n1. Deposit Amount \n2. Withdraw \n3. Show Account Details \n4. Check Balance\n5. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    deposit(acc)
                elif choice == '2':
                    transfer(acc)
                elif choice == '3':
                    acc.display()
                elif choice=='4':
                    check_balance(acc)
                elif choice=='5':
                    break
            break
        elif (username!=acc.__username) or (password!=acc.__password):
            print("Your username or password invalid. Please enter the correct username or password ")
            forgot_pin(accounts)
        else:
            print("account is not existed")
            create_new_account(accounts)
def forgot_pin(accounts):
    contact=input("Enter contact number : ")
    print("OTP sent on registered contact number")
    otp=int(input("Enter OTP : "))
    new_pin=int(input("Enter new PIN : "))
    print("New PIN Generated Successfully...")
def create_new_account(accounts):
    name=input("Enter Name : ")
    contact=input("Enter Contact : ")
    username=input("Enter username")
    account_number=input("Enter Account Number : ")
    otp = int(input("Enter OTP : "))
    pin = int(input("Enter PIN : "))
    new_acc=Account(name,contact,account_number,0)
    new_acc.login_details(username,pin)
    accounts.append(new_acc)
    print("Account Created Successfully...")
def deposit(accounts):
    account_no = input("Enter the Account number : ")
    amount = float(input("Enter the amount you want to Deposit: "))
    for acc in accounts:
        if acc.account_number == account_no:
            acc.deposit(amount)
            print("Amount Deposited Successfully...")
        else:
            print("Account not found...")
def transfer(accounts):
    account_no = input("Enter the Account number : ")
    amount = float(input("Enter the amount you want to transfer: "))
    for acc in accounts:
        if acc.account_number == account_no:
            pin=int(input("Enter Pin : "))
            if pin==acc.__password:
                if acc.balance>=amount:
                    acc.transfer(amount)
                    print("Amount Deposited Successfully...")
            else:
                print("You Enter wrong PIN")
        else:
            print("Account not found...")
def check_balance(accounts):
    pin = int(input("Enter Pin : "))
    if pin == accounts.__password:
        accounts.display()
    else:
        print("Account not found ")

accounts = []
while True:
    print("\n1. Login Account \n2. create new account \n3. forgot pin \n4. transfer amount \n5. Check Balance\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        login(accounts)
    if choice == '2':
        create_new_account(accounts)
    elif choice == '3':
        forgot_pin(accounts)
    elif choice == '4':
        transfer(accounts)
    elif choice == '5':
        check_balance(accounts)
    elif choice == '6':
        break