import random # Импортировать библиотеку random

a = [] # Создать пустой массив a
for i in range(10): # Выполнить 10 раз
    a.append(random.randint(-10, 10)) # В массив a добавить случайное число (-10 <-> 10)
p = 0 # Создать счётчик положительных чисел
n = 0 # Создать счётчик отрицательных чисел
for b in a: # Перебор элементов
    if(b >= 0): # Если положительный
        p += 1 # Увеличить значение p на 1
    else:
        n += 1 # Увеличить значение n на 1
print(p, n) # Напечатать значения p и n
