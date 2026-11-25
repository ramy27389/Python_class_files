import copy
a=[1,2,3]
b=copy.copy(a)
b.append(5)
print("b is " ,b)
print("a is  ",a)

c=a[:]
c.append(6)
print("c is" ,c)