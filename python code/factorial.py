def fact(x):
    if x == 1:
        return x
    elif x ==0:
        return 1
    else:
        return (x * fact(x-1))
print (fact(7))
                
