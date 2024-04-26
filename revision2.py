class vehicle:
    def __init__(self,type,color):
        self.type=type
        self.color=color
    def show(self,capacity):
        print(f"Vehicle type: {self.type}\ncolor : {self.color}\nseating capacity : {capacity}")
class car(vehicle):
    def __init__(self,type,color,brand,fuel):
        super().__init__(type, color)
        self.brand=brand
        self.fuel=fuel
    def info(self):
        print(f"Brand : {self.brand} is {self.fuel} Car.")
    def start_car(self):
        print("Start car...")
    def change_gear(self):
        print("Change gear...")
    def display(self):
        print(f"Car brand : {self.brand}\nFuel : {self.fuel}\nColor : {self.color} ")

my_car = car("Sedan", "Red", "Toyota", "Petrol")
my_car.show(4)
my_car.info()
my_car.start_car()
my_car.change_gear()
my_car.display()

data=[]
class students:
    def __init__(self,ID,name,contact,std):
        self.ID=ID
        self.name=name
        self.contact=contact
        self.std=std
    def display(self):
        print(f"ID : {self.ID}\nName: {self.name}\nContact Number :{self.contact}\nStandard : {self.std}")
def new_admission(data):
    ID=int(input("Enter ID :"))
    name=input("Enter name : ")
    contact= int(input("Enter Contact : "))
    std=input("Enter standard : ")
    for d in data:
        if d.ID==ID:
            print("student data already present ")
        else:
            s1=students(ID,name,contact,std)
            data.append(s1)
            s1.display()

s=students(1,"Siya",123345,'X')
s.display()
s1={'ID':2,'Name':"Ritu","Contact":123456,'std':'IX'}
new_admission(data)
# print(data)


