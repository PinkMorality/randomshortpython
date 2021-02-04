print("Finding out Simple Interest")
p = float(input("Enter your principle amount "))
t = float(input("Enter your payment time in years "))
r = float(input("Enter your rate of interest p.a. "))
interest = (p*r*t)/100
to_pay = p+interest

print(f"Your interest will be {interest}, and your total amount will be {to_pay}.")