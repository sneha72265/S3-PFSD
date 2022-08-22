import Train
class vijayawada(Train.train):
    def __init__(self,name,number,age):
        super().__init__(name,number,age)
    def book(self):
        print("Your Ticket was Booked to VIJAYAWADA")
        print("Name: "+self.name+"\nPhone Number: "+self.number+"Age: "+self.age)

v=vijayawada(input("Enter Your Name: \n"),int(input("Enter Your Mobile Number: \n")),int(input("Enter Your Age: \n")))
v.book()