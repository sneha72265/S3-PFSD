class train:
    def __init__(self,name,number,age):
        self.name=name
        self.number=number
        self.age=age

class vijayawada(train):
    def __init__(self,name,number,age):
        super().__init__(name,number,age)
    def book(self):
        print("Your Ticket was Booked to VIJAYAWADA")
        print("Name: "+self.name+"\nPhone Number: "+str(self.number)+"Age: "+str(self.age))
class hydrabad(train):
    def __init__(self,name,number,age):
        super().__init__(name,number,age)
    def book(self):
        print("Your Ticket was Booked to HYDRABAD")
        print("Name: "+self.name+"\nPhone Number: "+str(self.number)+"Age: "+str(self.age))

v=vijayawada(input("Enter Your Name: \n"),int(input("Enter Your Mobile Number: \n")),int(input("Enter Your Age: \n")))
v.book()
h=hydrabad(input("Enter Your Name: \n"),int(input("Enter Your Mobile Number: \n")),int(input("Enter Your Age: \n")))
h.book()