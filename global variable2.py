x=int(input("Enter the value of x : "))
class calculator:
    y = int(input("Enter the value of y : "))  # class variable
    def add(self):
        print("Addition : ",x+self.y)
    def sub(self):
        print("Substraction : ", x - self.y)
    def mul(self):
        print("Multiplication : ", x * self.y)
    def div(self):
        try:
            if self.y==0:
                raise ZeroDivisionError("Cannot divide by Zero")
            print("Division : ", x / self.y)
        except ZeroDivisionError as e:
            print(e)

c=calculator()
c.add()
c.div()

d=40
def func():
    # modify global variable x using global keyword
    global d
    d=d+30
    print(d)
func()

def new():
    # create new global variable using global keyword
    global name
    name="Siya"
    print("Hello",name)
new()
print("Hello, I am ",name)

price=int(input("Enter the price"))
def shopping():
    discount=float(input("Enter the Discount : "))
    globals()['price']=price-(price*discount)
    print("Price : ",price)
print("price before Discount : ",price)
shopping()
print("price after Discount : ",price)
