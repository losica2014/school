def checkForSimplicity(n):
    i = 2
    while i**2 <= n:
        if(n % i == 0):
            print("Составное")
            return
        i += 1
    print("Простое")
    return
checkForSimplicity(int(input()))
