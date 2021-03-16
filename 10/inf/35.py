def F(n,m):
    if(n < m):
        n,m = m,n
    if n != m:
        return F(n-m, m)
    else:
        return n
    
# Переведено с C++
#
#def F(n, m):
#    if(n > m):
#        return F(n-m, m)
#    elif(n < m):
#        return F(m-n, n)
#    else:
#        return n

smin = 1000+1000
nmin = 1000
mmin = 1000

for n in range(1, 1000):
    for m in range(1, 1000):
        r = F(n, m)
        if(r > 15) and(n != m):
            if(n+m < smin):
                smin = n+m
                nmin = n
                mmin = m
if(nmin >= mmin):
    print(mmin, nmin, F(nmin,mmin))
else:
    print(nmin, mmin, F(nmin,mmin))

