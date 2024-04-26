x=20  #global varibale
def fun():
    y=35  # local vraible
    global x  # access global variable
    x=x+20
    print(x)
fun()
print(x)

name=input("Enter name : ")  # global varible
def print_name():
    print("Name of student : ",name)
print_name()
print("Name of student : ",name)

name1=input("Enter name : ")  # global variable
class Employee:
    position="Software Developer"           #class variable
    def __init__(self):
        print(f"I am {name1}. I am working as {self.position}")
e=Employee()

# Using Global Variables In Function
# x is global variable
# y is local variable
x=int(input("Enter the value of x : "))
class calculator:
    def add(self):
        y=int(input("Enter the value of y : "))
        print("Addition : ",x+y)
    def sub(self):
        y = int(input("Enter the value of y : "))
        print("Substraction : ", x - y)
    def mul(self):
        y = int(input("Enter the value of y : "))
        print("Multiplication : ", x * y)
    def div(self):
        y = int(input("Enter the value of y : "))
        try:
            print("Division : ", x / y)
            if y==0:
                raise ZeroDivisionError("can not divide by Zero")
        except ZeroDivisionError as e:
            print(e)

c=calculator()
c.add()
c.div()