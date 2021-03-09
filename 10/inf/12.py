def F(n):
    if(n < 1):
        return n
    elif(n % 2 == 0):
        return n + 3*F(n-3)
    else:
        return 5*n + 2*F(n-5)

print(F(30))
