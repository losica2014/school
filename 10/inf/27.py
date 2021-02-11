import random

s = int(input("Введите s: "))
while(s >= 20):
    s = int(input("s должен быть меньше 20!\nВведите s: "))

a = []
for i in range(10):
    a.append(random.randint(0, 10))

print(*a)

for i in range(10-1):
    if(a[i] + a[i+1] > s):
        print(i, i+1)
