from random import *
list1 = []
#bruh = randint(0,1)
count = 0
while True:
    count += 1
    for i in range(0,10):
        list1.append(randint(0,1))
    if 1 not in list1:
        break
    else:
        #print(list1)
        list1.clear()


print(count, list1)
