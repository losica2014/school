def F(n):
    if(n == 1):
        return 3
    elif(n > 1):
        return 2 * F(n-1)- n + 1

print(F(21))
