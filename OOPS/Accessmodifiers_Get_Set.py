class Student:
    def __init__(self,name,age,roll):
        self.name=name
        self._age=age
        self.__roll=roll

    def show_details(self):
        print('Student name: ', self.name)
        print('Student age : ', self._age)

    def get_roll(self):
        return self.__roll

    def set_roll(self,new_roll):
        self.__roll=new_roll

class Marksheet(Student):
    def show_marksheet(self):
        print('\nMARKSHEET DETAILS')
        print('Student name     : ', self.name)
        print('Student age      : ', self._age)
        print('Student rollno   : ', self.get_roll())

name=input('Enter student name')
age=input('enter student age')
rollno=input('enter rol number')

student1=Marksheet(name,age,rollno)

student1.show_details()
print()
student1.show_marksheet()

new_roll=input("enter new roll number ")

student1.set_roll(new_roll)
print("\nupdated the roll number successfully")
print('new roll number is',student1.get_roll())