#set up the calculator
class calc:

    def addition(x,y):
        add = x + y
        print("%s plus %s is %s." % (for_addition_1, for_addition_2, add))

    def subtraction(x,y):
        sub = x - y
        print("%s minus %s is %s." % (for_subtraction_1, for_subtraction_2, sub))

    def multiplication(x,y):
        mult = x * y
        print("%s plus %s is %s." % (for_multiplication_1, for_multiplication_2, mult))

    def division(x,y):
        div = x / y
        print("%s plus %s is %s." % (for_division_dividend, for_division_divisor, div))

while close == "y":

    kind_of_calculation = input("What kind of calculation do you want?(Add, Subtract, Multiply, Divide) ") #get the kind of calculation desired

    if kind_of_calculation in ("Add","add"):
        for_addition_1, for_addition_2 = float(input("First number that you want to add. ")), float(input(
            "Second number that you want to add. "))
        calc.addition(for_addition_1,for_addition_2)


    elif kind_of_calculation in ("Subtract","subtract"):
      for_subtraction_1, for_subtraction_2 = float(input("The number that you want to subtract from. ")), float(input(
        "The number that you want to subtract. "))
    calc.subtraction(for_subtraction_1, for_subtraction_2)


    elif kind_of_calculation in ("Multiply","multiply"):
    for_multiplication_1, for_multiplication_2 = float(input("First number that you want to multiply. ")), float(input(
        "Second number that you want to multiply. "))
    calc.multiplication(for_multiplication_1, for_multiplication_2)


    elif kind_of_calculation in ("Divide","divide"):
        for_division_dividend, for_division_divisor = float(input("Enter the dividend. ")), float(input(
            "Enter the divisor. "))
        calc.division(for_division_dividend, for_division_divisor)


    else:
        print("Incompatible values")

    close = input("Press Y to redo.")



