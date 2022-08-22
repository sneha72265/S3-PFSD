import math
class Rectangle:
    def findRPerimeter(self,l,b):
        res=(2*(l+b))
        return res
    def findRArea(self,l1,b1):
        res1 = l1*b1
        return res1
r=Rectangle()
print(r.findRPerimeter(4,5))
print(r.findRArea(3,9))

class Circle:
    def findCArea(self,ci):
        ca=2*(math.pi)*ci*ci
        return ca
    def findCPerimeter(self,ci1):
        ca1=2*(math.pi)*ci1
        return ca1
circle =Circle()
print(circle.findCArea(23))
print(circle.findCPerimeter(34))
class Triangle():
    def findTPerimeter(self):
        t1=3
        t2=4
        t3=9
        r=int((t1+t2+t3))
        print(r)
    def findTArea(self):
        t4=7
        t5=9
        t6=10
        s = (t4 + t5 + t6) / 3
        s1 =((math.sqrt(s*(s - t4)*(s - t5)*(s - t6))))
        print(s1)
obj=Triangle()
obj.findTPerimeter()
obj.findTArea()





