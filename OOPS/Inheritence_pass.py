class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def getdata(self):
        print(self.name,self.age)

obj=Person('Raju',20)
obj.getdata()

class Student(Person):
    pass

p2=Student("puppu", 56)
p2.getdata()