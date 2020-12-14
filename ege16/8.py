def f(x):
    if x<=18:
        return 3*f(x+1)+x+8
    elif x>18:
        return x
print(f(9))
