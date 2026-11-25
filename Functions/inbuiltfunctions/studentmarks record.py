marks=[]
students=int(input("Enter the no of students : "))
for s in range(1,students+1):
    mark1=int(input("Enter the mark: "))
    marks.append(mark1)
print(marks)
print()

total_students=len(marks)
total_marks=sum(marks)
average=total_marks/total_students
higest=max(marks)
lowest=min(marks)
ascending=sorted(marks)
descending=sorted(marks, reverse=True)


print("Total no of students     : ",total_students)
print("Total marks              : ",total_marks)
print("Average                  : ",average)
print("Highest mark             : ",higest)
print("Lowest mark              : ",lowest)
print("Mark in ascending order  : ",ascending)
print("Mark in descending order : ",descending)
print("Datatype of the marks    : ",type(marks))

for m in marks:
    if m>=90:
        grade="E"
    elif m>=80:
        grade="A"
    elif m>=70:
        grade="B"
    elif m>=60:
        grade="C"
    else:
        grade="D"
    print("Mark : ",m, "|" , "Grade :" , grade)

Student_record={}
for i in range(1,students+1):
    name=input("Enter the name of students in order: ")
    Student_record[name]=marks[i-1]
print(Student_record)