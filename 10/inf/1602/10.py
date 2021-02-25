def printDividers(n):
    d = []
    i = 1
    while i**2 <= n:
        if(n % i == 0):
            d.append(i)
        i += 1
    print(*d)
    
printDividers(int(input()))
