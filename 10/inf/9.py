def F(n):
    if(n > 16):
        return n-3
    elif(n <= 16):
        return 2*F(n+1) + 2*n + 3

print(F(9))
