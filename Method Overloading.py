class Student:
    def info(self, id=10):
        self.id = id
        return id


ob = Student()
print(ob.info())
print(ob.info(20))
