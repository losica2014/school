c = 0
def F(n):
    global c
    c += 1
    if(n >= 1):
        c += 1
        F(n-1)
        F(n//3)
        c += 1

F(280)
print(c)
