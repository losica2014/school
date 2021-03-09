def F(n):
    if(n == 1):
        return 1
    elif(n > 1):
        return 2 * F(n-1)+ n + 3

print(F(19))
