answ = []

for x in range(1, 1000):
    # print(x)
    xo = x
    a = 0; b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 8)
        x = x // 8
        # print(a, b)
    if(a == 3) & (b == 24):
        # print(xo)
        answ.append(xo)

r = 0
print(answ)
for i in answ:
    if(i > r):
        r = i
print(r)
