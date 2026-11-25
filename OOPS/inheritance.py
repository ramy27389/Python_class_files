class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getdata(self):
        self.data=self.name+" "+str(self.age)
        print(self.data)
p1=Person("Raju",57)
p1.getdata()

class Student(Person):
    def add_data(self,cls,division):
        self.cls=cls
        self.division=division
    def get_alldata(self):
        print("Name: ", self.name)
        print("Age :",self.age)
        print("Class :",self.cls)
        print("Division :",self.division)

student1=Student("Manu",20)
student1.add_data("10th","B")

student1.get_alldata()