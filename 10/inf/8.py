def F(n):
    if(n > 18):
        return n
    elif(n <= 18):
        return 3*F(n+1) + n + 8

print(F(9))
