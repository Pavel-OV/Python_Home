
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
# Домашнее задание
from random import randint
print('Найти в массиве A[1..N] самый близкий по  величине элемент к заданному числу X')
numberN=int(input('Количество элементов в массиве='))
spicok=[]
for i in range(numberN):
    spicok.append(randint(0,10))
print(*spicok)
x=int(input('Введите число ='))
digital=0
count=len(spicok)
# for i in range(len(spicok)):
   
#     if (x==spicok[i]-1 or x==spicok[i]+1): 
#         print(f'ближайщее число к {x} находится число по индексу {i} значение {spicok[i]} ')
#     else:
#         print(f'Нет чисел ближайщих к{x}')
while digital<len(spicok):
    if (x==spicok[digital]-1 or x==spicok[digital]+1): 
        print(f'ближайщее число к {x} находится число по индексу {digital} значение {spicok[digital]} ')
        count+=1
    digital=digital+1
if(count==len(spicok)):
    print(f'Нет чисел ближайщих к{x}')
   



  

