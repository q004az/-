def f(x):
    if x>1:
        return f(x-1)+f(x-2)+2*x+4
    elif x<=1:
        return 2
print(f(25))
