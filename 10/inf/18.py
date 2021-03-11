def F(n):
    if(n == 1):
        return 1
    elif(n > 1):
        return 2*F(n-1)+G(n-1)-2

def G(n):
    if(n == 1):
        return 1
    elif(n > 1):
        return F(n-1)+2*G(n-1)

print(F(14) + G(14))
