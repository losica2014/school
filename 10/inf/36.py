def F(n,m):
    if(m == 0):
        return n
    else:
        return F(m,n%m)
ns = []
for n in range(100, 1001):
    for m in range(100, 1001):
        r = F(n, m)
        if(r == 30):
            ns.insert(n, 0)
            ns.insert(n, 1)
nc = 0     
for n in ns: nc += n
print(ns, nc)
