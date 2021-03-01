def printDividers(n):
    d = []
    i = 1
    while i <= n:
        if(n % i == 0):
            d.append(i)
        i += 1
    print(*d)
    
printDividers(int(input()))
