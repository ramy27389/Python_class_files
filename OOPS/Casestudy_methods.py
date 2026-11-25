class Person:
    school_name="ABC school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def instantmethod(self):
        print(self.name,self.age)
    @classmethod
    def class_method(cls,new_name):
        cls.school_name=new_name
    @staticmethod
    def static_method():
        print("welcome tot he method study")

s1=Person("Ramy", 45)
s1.instantmethod()

Person.class_method("Changed scho")
print(Person.school_name)
Person.static_method()
