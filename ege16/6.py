def f(x):
    if x>1:
        return f(x-1)+f(x-2)+4*x
    elif x<=1:
        return 2
print(f(24))
