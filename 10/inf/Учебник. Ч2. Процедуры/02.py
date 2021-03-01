def printHex(n):
    if(n >= 16**4):
        print("Error!")
        return
    
    k = 16**3
    while k > 0:
        t = n // k
        tp = ""
        if(t <= 9):
            tp = str(t)
        elif(t == 10):
            tp = "A"
        elif(t == 11):
            tp = "B"
        elif(t == 12):
            tp = "C"
        elif(t == 13):
            tp = "D"
        elif(t == 14):
            tp = "E"
        elif(t == 15):
            tp = "F"
        
        print(tp, end="")
        n = n%k
        k = k // 16

printHex(int(input()))
