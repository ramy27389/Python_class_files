import copy
a=[[1,2,3],[4,5,6]]

b=copy.copy(a)

b[0][0]=9

print('a is ',a)
print('b is ',b)

c=copy.deepcopy(a)

c[0][0]=11
c[1][2]=7
c.append(23)

print('c is ',c)