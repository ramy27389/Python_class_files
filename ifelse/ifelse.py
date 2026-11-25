marks = int(input("enter the marks"))
if marks>=90:
    print("Grade A+")
    if marks>96:
        print("outstanding")
    else:
        print("good work")
else:
    print("Grade is B+")
    if marks<80:
        print("average")
    