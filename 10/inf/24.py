import random

A = []
for i in range(10):
    A.append(random.randint(-10, 10))
B = []
for i in range(10):
    if(A[i] % 2 == 0):
        B.append(i)
print(*B)