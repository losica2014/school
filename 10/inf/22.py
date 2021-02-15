import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
p = 0
n = 0
for b in a:
    if(b >= 0):
        p += 1
    else:
        n += 1
print(p, n)
