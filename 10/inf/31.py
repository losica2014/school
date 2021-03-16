def F(n):
    if n > 0:
        return n%10*F(n//10)
    else:
        return 1

i = 1
while True:
    r = F(i)
    if(r > 320):
        print(i, r)
        break
    i += 1
