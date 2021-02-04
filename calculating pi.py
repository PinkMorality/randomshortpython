import math
from decimal import *

getcontext().prec = 200

pi = Decimal(3.0)
real_pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

a = Decimal(2.0)
b = Decimal(3.0)
c = Decimal(4.0)
nve = 1

for i in range(10000000):
    four = 4
    pi = pi + ((four/(a*b*c))*nve)
    a += 2
    b += 2
    c += 2
    if nve == 1:
        nve = -1
    else:
        nve = 1

#print(pi)

#print(truncate(10.123, 2))
#print(pi)
printpi = ""
strpi = str(pi)
#print("We got", pi)
#print("Real is", real_pi)
for i in range(100):
    if strpi[i] == real_pi[i]:
        printpi += strpi[i]
    else:
        break

print(printpi)
accuracy_digits = len(printpi)-2
print(accuracy_digits)
    
    
    
