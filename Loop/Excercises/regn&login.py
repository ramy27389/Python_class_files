x=True
while x:
    data=[]
    data.append(input("Enter Name: "))
    data.append(input("Enter username: "))
    data.append(input("Enter email id: "))
    data.append(input("Enter password: "))
    data.append(input("confirm password: "))
    if data[0]!='' and data[1]!='' and data[2]!='' and data[3]!='' and data[4]!='': 
        if data[-1]==data[-2]:
            if '@' in data[2] and '.' in data[2]:
                print("Registration successfull")
                x=False
            else:
                print("invalid email id")
        else:
            print("password does not match")
    else:
        print("Field cant be left blank")

                #LOG IN
username=input("Enter username : ")
password=input("Enter password : ")

y=1
while y:
    if username==data[1]:
        if password==data[4]:
            print("Welcome ",username)
            y=0
        else:
            print("Invalid password")
    elif username==data[2]:
        if password==data[-2]:
            print("Welcome ",data[0])
            y=0
        else:
            print("Invalid password")
    else:
        print("Invalid username")    