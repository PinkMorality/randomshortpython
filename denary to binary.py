d_number = int(input("Enter denary number. "))
d_print = d_number
b_digits = 7
b_number = ""
for i in range(0,b_digits+1):
    x = d_number//(2**b_digits)
    if x >= 1:
        x = 1
    if x == 1:
        d_number = d_number-(2**b_digits)
    #print(f"{x}      {2**b_digits}")
    b_number = b_number + str(x)
    b_digits -= 1

print(f"{d_print} in binary: {b_number}")