import random

found = False
target = random.randint(75,125)
print(target)
givenarray = []

for i in range(1,101):
    givenarray.append(random.randint(1,100))

for i in givenarray:
    if (target-i) in givenarray:
        if found == False:
            found = True
        print(f"{target-i}+{i}={target}")

if found == False:
    print("Error! No complement found.")
#print(givenarray)
