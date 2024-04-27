"""An example showcasing multilevel inheritance in Python involves
classes like Student, Bsc, and Result."""

class students:
    def info(self):
        self.name=input("Enter name : ")
        self.__rollno=int(input("Enter roll no. : "))
    def show(self):
        print(f"Name : self.name \n Roll N. : {self.__rollno}")
class bsc(students):
    def marks(self):
        self.info()
        self.phy=int(input("Enter the Physics Marks: "))
        self.math = int(input("Enter the Math Marks: "))
        self.chem = int(input("Enter the Chem Marks: "))
        self.bio = int(input("Enter the Bio Marks: "))
        self.eng = int(input("Enter the English Marks: "))
        self.marathi = int(input("Enter the Marathi Marks: "))
    def printmarks(self):
        print("Marks of subjects are : \n")
        print(f"Physics : {self.phy}\n Math : {self.math}\n Chem : {self.chem}\n Bio : {self.bio}\n English : {self.eng}\n Marathi : {self.marathi}")
    def total_marks(self):
        return ("Total Marks: ", self.phy+self.math+self.chem+self.bio+self.eng+self.marathi)
class result(bsc):
    def get_result(self):
        self.marks()
        self.TotalMarks=self.total_marks()
    def show_result(self):
        self.printmarks()
        print("Total marks: ",self.TotalMarks)

r1=result()
print(r1.get_result())
print(r1.show_result())





