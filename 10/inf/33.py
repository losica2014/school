last = 0
def F(n):
    global last
    last = n
    if(n > 0):
        d=n%10+F(n//10)
        last = d
        return d
    else:
        return 0

i = 1
while True:
    r = F(i)
    if(last > 32):
        print(i, r)
        break
    i += 1
