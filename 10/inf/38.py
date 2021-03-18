def F(n,m):
    if(m == 0):
        d=0
    else:
        d = n+F(n,m-1)
    return d

ns = []

for na in range(1, 100):
    for ma in range(1, 100):
        r = F(na, ma)
        if(r == 30):
            # print(i, r)
            ns.insert(na, 1)

nc = 0
for n in ns:
    nc += n
print(nc)
