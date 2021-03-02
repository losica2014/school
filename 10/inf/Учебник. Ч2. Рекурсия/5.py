def printDec(n, r=0):
    ns = str(n)
    r += 2**(len(ns)-1)
    ns = ns[1:]
    if(len(ns) == 0):
        print(r)
        return
    n = int(ns)
    printDec(n, r)

printDec(int(input()))
