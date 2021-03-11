def F(n):
    if(n < 5):
        return 5-n
    elif(n % 3 == 0):
        return 4*(n-5)*F(n-5)
    else:
        return 3*n+2*F(n-1)+F(n-2)

print(F(20))
