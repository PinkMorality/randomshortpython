print("Finding out Compound Interest")
p = float(input("Enter your principle amount "))
t = float(input("Enter your payment time in years "))
r = float(input("Enter your rate of interest p.a. "))
c_interest = (p*((1+(r/100))**t))-p
to_pay = p+c_interest

print(f"Your interest will be {c_interest}, and your total amount will be {to_pay}.")

a="hello"
print(a)
type(a)