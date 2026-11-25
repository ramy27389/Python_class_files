# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# studend1=Student("Arun",85)
# print(studend1.name,studend1.age)

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def getdata(self):
        print(self.fname,self.lname)
p1=Person("John", "Doe")
p2=Person('Python', 'programmer')

p1.getdata()
p2.getdata()