try:
    a=int(input("enter the number "))
    print(a)
except  ValueError:
    raise ValueError("ValueError: invalid literal for int() with base 10: 'k")