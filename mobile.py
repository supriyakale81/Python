class mobile:
    def __init__(self,brand,name):
        self.name=name
        self.brand=brand
    def calling(self,number):
        print("Calling...",{number})
    def send_message(self,receipt,message):
        print("send message...",receipt,message)
    def camera(self):
        print("open camera..")
        print("take picture...")
m=mobile("Samsung",'Glaxy')
m.calling(23456778)
m.send_message('Siya','Hello')
m.camera()

