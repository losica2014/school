print('r m k')
for r in range(1,11):
    for m in range(1,11):
        for k in range(1,11):
            if(m*m + r*r == k*k):
                print(r,m,k)
