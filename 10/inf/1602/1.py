def printOctal(n):
    if(n >= 8**10):
        print("Error!")
        return
    
    k = 8**9
    while k > 0:
        print(n // k, end="")
        n = n%k
        k = k // 8

printOctal(int(input()))
