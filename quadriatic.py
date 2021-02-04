while True:
    import cmath
    a = float(input("Enter a. "))
    b = float(input("Enter b. "))
    c = float(input("Enter c. "))
    bsquare_4ac = cmath.sqrt(b*b-(4*a*c))
    bsquare_4ac_backup = bsquare_4ac
    bsquare_4ac = bsquare_4ac.real
    bsquare_4ac_checker = (b*b)-(4*a*c)
    if bsquare_4ac_checker < 0:
        quadratic_equation1 = (-b + bsquare_4ac_backup) / (2 * a)
        quadratic_equation2 = (-b - bsquare_4ac_backup) / (2 * a)
        print(f"X has two values, {quadratic_equation1} and {quadratic_equation2}")
    elif bsquare_4ac_checker == 0:
        quadratic_equation1 = (-b + bsquare_4ac) / (2 * a)
        quadratic_equation2 = (-b - bsquare_4ac) / (2 * a)
        print(f"X has only one value, which is {quadratic_equation1}")
    elif bsquare_4ac_checker > 0:
        quadratic_equation1 = (-b + bsquare_4ac) / (2 * a)
        quadratic_equation2 = (-b - bsquare_4ac) / (2 * a)
        print(f"X has two values, {quadratic_equation1} and {quadratic_equation2}")
    if input("Do you want to repeat[y/n]? ") == "n":
        break
