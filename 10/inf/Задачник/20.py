import random # Импортировать библиотеку random

a = [] # Создать пустой массив a
for i in range(10):
    a.append(random.randint(-10, 10)) # В массив a добавить случайное число (-10 <-> 10)
r = a[0] # Создать переменную Result, задать значение первого элемента
for b in a: # Перебор элементов
    if(b < r): # Если элемент подходить больше, чем текущий
        r = b # Задать значение результата текущим элементом
print(r) # Напечатать результат
