person={'name':'alice','age':24,"city":'new york'}
print(person)

person['job']='engineer'
del person['city']
print(person)

person.clear()
print(person)