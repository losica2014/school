c = 0
def F(n):
    global c
    c += n+1
    if(n >= 1):
        c += n+5
        F(n-1)
        F(n-2)
r = 0
n = 1
while r < 1000000:
    F(n)
    r = c
    c = 0
    if(r >= 1000000):
        print(n)
        
    else:
        n += 1
