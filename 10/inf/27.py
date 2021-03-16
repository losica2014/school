def F(n):
    s = n+1
    if n > 1:
        s = s + 2 * n
        s = s + F(n-1)
        s = s + F(n-3)
    return s

i = 1
while True:
    r = F(i)
    if(r > 1000000):
        print(i, r)
        break
    i += 1
