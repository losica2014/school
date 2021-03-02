def printSum(n, n2=0):
    if(n2 == 0):
        n -= 1
        n2 += 1
    if(n <= 0) or (n2 < 0):
        return
    print(n, n2)
    if(n-1 == n2) or (n2+1 == n):
        return
    printSum(n-1, n2=n2+1)

printSum(int(input()))
