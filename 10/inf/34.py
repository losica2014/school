a = []
def F(n):
    global a
    a.append(n)
    if(n > 0):
        d=(n%10+F(n//10))
        a.append(d)
        return d
    else:
        return 0

i = 1
while True:
    r = F(i)
    if(a[2] > 51):
        print(i, r)
        break
    i += 1
    a = []
