"""you provide a web form for users to fill in and submit.but incase there are a lot of conditions to be handled and
the conditions keeps changing periodically,you use exception handling to simplify the process"""

class form:
    data={}
    def __init__(self,name,age,experience,email):
        self.name=name
        self.age=age
        self.experience=experience
        self.email=email
        try:
            if type(self.name)!=str:
                raise ValueError("Enter the correct name")
            elif type(self.age)!=int:
                raise ValueError("Enetr the integer value of age")
            elif type(self.experience)!=int:
                raise ValueError("Enetr the experience in integer value")
            elif '@' not in self.email:
                raise ValueError("Invalid Email")
        except ValueError as e:
                print(e)
    def details(self):
        self.data["name"] = self.name
        self.data["age"] = self.age
        self.data["experience"] = self.experience
        self.data["email"] = self.email
        print(self.data)

c=form("Siya",24,'example.com',1)
print(c.details())
c1 = form("Siya", 'er', 1,'exampleexample.com')
print(c1.details())

c2 = form("Siya", 23, 'erf','exampleexample.com')
print(c2.details())
c3 = form("Siya", 23, 2,'exampleexample.com')
print(c3.details())