class Parent:
    def fn1(self):
        print("This is a parent class")


class Child1(Parent):
    def fn2(self):
        print("This is child class")


class GrandChild(Child1):
    def fn3(self):
        print("This is grandchild class")


ob = GrandChild()
ob.fn2()
ob.fn1()
ob.fn3()