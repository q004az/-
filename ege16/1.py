def f(x):
    if x>1:
        return 2*f(x-1)+x+3
    else:
        return 1
print(f(19))
   
