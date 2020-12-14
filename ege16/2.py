def f(x):
    if x>1:
        return 2*f(x-1)-x+1
    else:
        return 3
print(f(21))
