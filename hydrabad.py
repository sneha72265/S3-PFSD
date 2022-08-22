import Train

class hydrabad(Train.train):
    def __init__(self,name,number,age):
        super().__init__(name,number,age)
    def book(self):
        print("Your Ticket was Booked to HYDRABAD")
        print("Name: "+self.name+"\nPhone Number: "+self.number+"Age: "+self.age)

h=hydrabad(input("Enter Your Name: \n"),int(input("Enter Your Mobile Number: \n")),int(input("Enter Your Age: \n")))
h.book()