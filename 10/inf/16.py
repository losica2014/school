def F(n):
    if(n < 5):
        return 1+2*n
    elif(n % 3 == 0):
        return 2*(n+1)*F(n-2)
    else:
        return 2*n+1+F(n-1)+2*F(n-2)

print(F(15))
