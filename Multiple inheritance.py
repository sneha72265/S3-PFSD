class Parent1:
    def fn1(self):
        print("This is a parent class")


class Parent2:
    def fn2(self):
        print("This is also parent class")


class Derived(Parent1, Parent2):
    def fn3(self):
        print("This is child class")


ob = Derived()
ob.fn2()
ob.fn1()