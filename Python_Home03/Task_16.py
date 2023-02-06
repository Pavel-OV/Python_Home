# Задача 16:  Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint
print('Требуется вычислить, сколько раз встречается некоторое  число X в массиве A[1..N].')
massiv=[]
number=int(input('Введите длину массива='))
x=int(input('Какое число X ищем?'))
for i in range(number):
    number=randint(0,10)
    massiv.append(number)
print(massiv)
count=0
for i in range(len(massiv)):
    
    if(x==massiv[i]):
        count=count+1
print(count)