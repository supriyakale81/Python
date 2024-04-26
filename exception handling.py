import msilib.schema


def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Please change 'y' argument to non-zero value")
    except:
        print("Something went wrong")
    else:
        print(f"Your answer is {result}")
    finally:
        print("Code Is Done")
divide(1,0)
divide(3,4)
divide(1,'g')

class Students:
    data={}
    m=[]
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
    def show(self):
        print("Student Details : \n")
        print(f"Student ID : {self.ID} Name : {self.name}\n")
class Marks(Students):
    def __init__(self,name,ID):
        super().__init__(name, ID)
        self.phy=int(input("Enter Physiscs Marks"))
        self.math = int(input("Enter Mathematics Marks"))
        self.chem = int(input("Enter Chemistry Marks"))
    def marks_list(self):
        # super().__init__(self)
        self.m.append(self.phy)
        self.m.append(self.math)
        self.m.append(self.chem)
        self.data["ID"] = self.ID
        self.data['Name'] = self.name
        self.data["marks"] = self.m
        print(self.data)
    def show(self):
        print(f"Marks of {self.name}\n")
        print(f"Physics : {self.phy}\n Mathematics : {self.math}\n Chemistry : {self.chem}")
class Error:
    stud_data={}
    def valid_marks(marks_list):
        try:
            for i,mark in enumerate(marks_list):
                if (mark <= 0) or (type(mark) != int):
                    raise ValueError("Enter the correct marks for ",i+1 )
                elif (mark > 100):
                    raise Exception("Marks should be less than 100")
        except ValueError as v:
            print(v)
            marks_list[i] = int(input("Enter Correct Marks : "))
            print(marks_list)
        except Exception as e:
            print(e)
            marks_list[i] = int(input("Enter Correct Marks : "))
s1=Marks("Siya",1)
s1.marks_list()
Error.valid_marks(s1.m)
print(s1.data)





