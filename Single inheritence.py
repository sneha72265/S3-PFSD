class Parent:
    def fn1(self):
        print("This is a parent class")


class Child(Parent):
    def fn2(self):
        print("This is child class")


ob = Child()
ob.fn2()
ob.fn1()

