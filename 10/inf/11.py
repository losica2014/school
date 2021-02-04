r2 = 0
r1 = 1
r = 1
n = 1
l = 2**16
# print('n r 1 2')
while(r <= l):
    # print(n, r, r1, r2)
    n += 1
    r = r1 + r2
    r2 = r1
    r1 = r
print(n)
