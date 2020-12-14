def f(x):
    if x>1:
        return f(x-1)+2*f(x-2)-5
    elif x<=1:
        return 3
print(f(22))
