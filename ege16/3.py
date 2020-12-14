def f(x):
    if x>1:
        return f(x-1)+5*x**2
    else:
        return 2
print(f(39))
