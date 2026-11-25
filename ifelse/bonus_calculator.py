dept=input("Enter the department name:sales, HR or IT: ")
points=int(input("Enter the performance points:"))
salary=int(input("Enter basic salary:"))

if dept=="sales":
    if points>=90:
        bonus=salary*0.20
    elif points>=75:
        bonus=salary*0.1
    else:
        bonus=salary*0.05
elif dept=="IT":
    if points>=85:
        bonus=salary*0.15
    else:
        bonus=salary*.05
elif dept=="HR":
    if points>=80:
        bonus=salary*0.15
    else:
        bonus=salary*.05
else:
    bonus=0
    print("invalid dept input")

Final_salary=salary+bonus
print("Bonus amount: Rs",bonus,"\nSalary is : Rs",Final_salary)