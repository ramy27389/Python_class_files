# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:
#         print("odd number")


list=[44,33,45,64,55,1,65,89,66]
list.append(11)
for i in list:
    if i%2==0:
        print(i,"even number")
    else:
        print(i, "odd number")

for number in list:
    if number==11:
        print("found the number:",number)
        break
else:
    print("number not found")