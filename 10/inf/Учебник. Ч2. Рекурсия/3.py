def printBin(n, k=2**9):
    if(n >= 2**10):
        print("Error!")
        return
    
    if k > 0:
        print(n // k, end="")
        printBin(n%k, k=k//2)

printBin(int(input()))
