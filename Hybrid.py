class P:
    def fn4(self):
        print("This is parent class")


class Derived1(P):
    def fn1(self):
        print("This is 1st derived class")


class Derived2(P):
    def fn2(self):
        print("This is 2nd Derived class")


class DC(Derived1, Derived2):
    def fn3(self):
        print("This is derived from 1st and 2nd derived classes")


ob1 = DC()
ob1.fn1()
ob1.fn2()
ob1.fn3()

