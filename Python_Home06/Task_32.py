
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint
number=int(input('Колличество элементов в списке'))
#spisok=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number=int(input('Задайте минимальное число в списке '))
max_number=int(input('Задайте максимальное число в списке '))
spisok=[]
sort_spisok=[]
i=0
while i<number:
    d=randint(-10,10)
    spisok.append(d)
    i+=1
print(spisok)
for i in range(len(spisok)):
       if spisok[i]>= min_number and spisok[i]<=max_number:
        sort_spisok.append(i)
print(sort_spisok)



# for i in number:
#     i=randint(-10,10)
#     spisok.append()
