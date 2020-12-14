def f(x):
    if x<=12:
        return 2*f(x+2)+x-4
    elif x>12:
        return 2*x-5
print(f(9))

