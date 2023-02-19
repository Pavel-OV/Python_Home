# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10
from random import randint
rows=int(input('Колличество строк ='))
column=int(input('Колличество  столбцов ='))
mas = [] 
for i in range(rows): 
    for j in range(column):
        mas.append(randint(0,10) )
for i in range(rows):
    for j in range(column):
        print(mas[rows * j + i], end=" ")
    print()
print()
mas.sort()
for i in range(rows):
    for j in range(column):
        print(mas[column * i + j], end=" ")
    print()

