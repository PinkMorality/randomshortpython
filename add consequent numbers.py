print("Adding consequent numbers.")
lower_number = int(input("Enter first number. "))
last_number = int(input("Enter last number. "))
number = 0
for i in range(lower_number, last_number):
    number += i
print(number)
