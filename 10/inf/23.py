import random # Импортировать библиотеку random

a = [] # Создать пустой массив a
for i in range(10): # Выполнить 10 раз
    a.append(random.randint(-10, 10)) # В массив a добавить случайное число (-10 <-> 10)
d = 0 # Создать переменную: сумма чётных
nd = 0 # Создать переменную: сумма нечётных
for b in a: # Перебор элементов
    if(b % 2 == 0): # Если чётный
        d += b # Прибавить к переменной чётных значение элемента
    else:
        nd += b # Прибавить к переменной нечётных значение элемента
print(d, nd) # Напечатать суммы чётных и нечётных
