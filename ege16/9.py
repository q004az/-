def f(x):
    if x<=16:
        return 2*f(x+1)+2*x+3
    elif x>16:
        return x-3
print(f(9))
