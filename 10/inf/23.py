import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
d = 0
nd = 0
for b in a:
    if(b % 2 == 0):
        d += b
    else:
        nd += b
print(d, nd)
