def printAge(n):
    if(n > 10) and (n < 20):
        print(n, "лет"
    elif(n % 10 == 1):
        print(n, "год")
    elif(n % 10 >= 2) and (n % 10 < 5):
        print(n, "года")
    else:
        print(n, "лет")

printAge(int(input()))
