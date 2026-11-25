cars=["audi", "bmw", "benz"]
mileage=[45,22,11]

i=0
while i<len(cars):
    j=0
    while j<len(mileage):
        print(cars[i], mileage[j])
        j+=1
    i+=1


#   Example -- 2

i=1
while i<=2:
    j=1
    while j<=2:
        print(i,j)
        j+=1
    i+=1