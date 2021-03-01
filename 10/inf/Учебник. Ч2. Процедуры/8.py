def printDigitsLast(n):
    ns = str(n)
    for i in range(len(ns)-1, -1, -1):
        print(ns[i])
printDigitsLast(int(input()))
