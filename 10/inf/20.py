import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
r = a[0]
for b in a:
    if(b < r):
        r = b
print(r)
