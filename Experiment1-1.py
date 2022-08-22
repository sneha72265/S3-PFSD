class Reservation:
    def details(self,name,phnumber,aadhar_num,age):
        print("Your Details")
        print("Name:",name)
        print("Phone number:",phnumber)
        print("Aadhar number:",aadhar_num)
        print("Age:",age)
class Ticket(Reservation):
    def trainDetails(self,tno,tname,seatno):
        print("Reservation successfull")
        print("Train Details")
        print("Train number : ", tno)
        print("Train name : ", tname)
        print("Seat number : ", seatno)
count=0
while(True):
    ch=int(input())
    if(ch==1):
        if(count<=3):
            t= Ticket()
            tnum=int(input("Enter the train number"))
            tname=input("Enter train name")
            seatno=int(input("Enter seat number"))
            pname=input("Enter passenger name")
            age=input("Enter passenger age")
            t.trainDetails(tnum,tname,seatno)
            t.details(pname,age)
            count=count+1
        else:
            print("Sorry fully booked!!")
            break
    else:
        break



    
