c = 0
def F(n):
    global c
    c += 1
    if(n >= 1):
        c += 1
        F(n-1)
        F(n-2)
        c += 1

F(35)
print(c)
