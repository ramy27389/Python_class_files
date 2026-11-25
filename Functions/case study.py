student = []

def add():
    name=input("Enter student name :")
    marks1=int(input("Enter marks  :"))
    marks2=int(input("Enter marks  :"))
    average=(marks1+marks2)/2
    student.append([name,average])
    print("Student added successfully")

def stud_info():
    print("Student details are:\n")
    for s in student:
        print("Name: ",s[0],"\nAverage: ",s[1])
        print()

def menu():
    while True:
        print("1. To add a student")
        print("2. To get students info")
        print("3. To exit\n")
        choice=int(input("Enter your choice"))

        if choice==1:
            add()
        elif choice==2:
            stud_info()
        elif choice==3:
            print("Good bye")
            break
        else:
            print("invalid input for choice")
            print()
menu()