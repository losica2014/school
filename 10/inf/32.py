def F(n):
    if n < 10:
        return n
    else:
        m = F(n//10)
        d = m%10
        if m<d:
            return d
        else:
            return m

i = 999
while i > 99:
    r = F(i)
    if(r > 7):
        print(i, r)
        break
    i -= 1
