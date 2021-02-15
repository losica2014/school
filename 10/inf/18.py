import random # Импортировать библиотеку random

a = [] # Создать пустой массив a
for i in range(10):
    a.append(random.randint(-10, 10))
r = 0
for b in a:
    r = r + b
print(r)
