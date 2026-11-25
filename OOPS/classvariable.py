class Person:
    school_name="ABC school"
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("Raju",57)
print("Name: ",p1.name, 'Age :',p1.age, 'School name : ', p1.school_name)


p2=Person("ptpr",544)
print("Name: ",p2.name, 'Age :',p2.age, 'School name : ', p2.school_name)