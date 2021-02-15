import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))
ix = 0
for i in range(10):
    if(a[i] > a[ix]):
        ix = i
print(a[ix], ix)
