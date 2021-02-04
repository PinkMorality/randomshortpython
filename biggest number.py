first_n = int(input("Enter the first number. "))
sec_n = int(input("Enter the second number. "))
third_n = int(input("Enter the third number. "))

if first_n > third_n:
    if first_n > sec_n:
        print(f"First number is the biggest.")
    elif sec_n > first_n:
        print("Second number is the biggest.")
elif third_n > first_n:
    if third_n > sec_n:
        print("Third number is biggest.")
    elif sec_n > third_n:
        print("Second number is biggest.")