def F(n):
    if(n == 1):
        return 2*n-5
    elif(n % 2 == 0):
        return 2*F(n-1)
    else:
        return 5 * n + F(n-2)

print(F(64))
