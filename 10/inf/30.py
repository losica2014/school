def F(n):
    s = n*n
    if n > 1:
        s = s + 2*n+1
        s = s + F(n-2)
        s = s + F(n//3)
    return s

i = 1
while True:
    r = F(i)
    if(r > 3200000):
        print(i, r)
        break
    i += 1
