def F(n):
    s = 2*n+1
    if n > 1:
        s = s + 3 * n - 8
        s = s + F(n-1)
        s = s + F(n-4)
    return s

i = 1
while True:
    r = F(i)
    if(r > 5000000):
        print(i, r)
        break
    i += 1
