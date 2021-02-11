import random

k1 = int(input("k1: "))
k2 = int(input("k2: "))

a = []
for i in range(10):
    a.append(random.randint(1, 100))
s = 0
c = 0
for b in a:
    if((b % k1 == 0) and (b % k2 == 0)):
        s = s + b
        c = c + 1
print(s, c)
