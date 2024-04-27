class grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
class father(grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        grandfather.__init__(self,grandfathername)
        print("father name: ",self.fathername,"grandfather name : ",self.grandfathername)
class son(father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
        father.__init__(self,fathername,grandfathername)
    def data(self):
        print("father name: ",self.fathername,"\n grandfather name : ",self.grandfathername,"\n son name : ",self.sonname)

d=son("prince","Rahul","Tukaram")
print(d.data())



