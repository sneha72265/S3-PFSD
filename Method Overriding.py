class Add1:
    def add(self, n1, n2):
        return (n1 + n2)
class Add2(Add1):
    def add(self, a, b):
        return (a + b)
obj = Add2()
print(obj.add(2, 3))
print(obj.add(1, 2))