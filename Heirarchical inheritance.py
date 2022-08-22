class Parent:
    def fn1(self):
        print("This is a parent class")


class Child1(Parent):
    def fn2(self):
        print("This is also parent class")


class Child2(Parent):
    def fn3(self):
        print("This is child class")

ob1 = Child1()
ob2=Child2()
ob1.fn2()
ob1.fn1()
ob2.fn3()
ob2.fn1()
