# for i in range(10):
#     print(i)
#     print("done")

# for i in range(10,0,-2):
#     print(i)
# print("done")

# _______________________________________________________
#STRINGS

name = "John Honai"
for c in name[::-1]:
    print(c,end=" ")

sentence = "\nlore nfs fe efdfd kjjje fd eddd"
count=0
for word in sentence.split():
    count += 1
print(sentence)
print(f"there are {count} words in the sentence")

cars=["audi", "bmw", "benz"]
mileage=[45,22,11]

for i in cars:
    print(i)

for c in range(len(cars)):
    print(cars[c], c)

for mil in range(len(mileage)):
    print(mileage[mil], mil)
print()

for i in cars:
    print(i)
for mil in mileage:
    print(mil)



