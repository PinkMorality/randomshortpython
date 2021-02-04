from decimal import *

getcontext().prec = 15
decimal = 0.336944434029
a = 0
ad = 1
b = 1
bd = 1
nominatior = 0
denominator = 0
for i in range(1,1000):
    check = (a+b)/(ad+bd)
    #if decimal == check:
        #break
    if decimal > check:
        if denominator > 10000:
            break
        else:
            nominatior = a
            denominator = ad
        a = a + b
        ad = ad + bd
    elif decimal < check:
        if denominator > 10000:
            break
        else:
            nominatior = b
            denominator = bd
        b = a + b
        bd = ad + bd


print(f"Fraction is {nominatior}/{denominator}")