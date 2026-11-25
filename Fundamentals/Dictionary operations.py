a={1:'one',2:'name','location':'kochi'}
print(a)
print(type(a))

a['place']='peringala'
del a[1]                #delete operation 
print(a)

val=a.pop(2)
print(a)

key,val=a.popitem()
print(a)