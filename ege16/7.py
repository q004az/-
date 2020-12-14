def f(x):
    if x<=15:
        return 2*f(x+1)+5*x+2
    elif x>15:
        return x
print(f(2))
