import random

a = []
b = []
for i in range(10):
    a.append(random.randint(1, 100))
    b.append(random.randint(1, 100))

c = [a[i] + b[i] for i in range(10)]
print(*c)
