# ; задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи,
# ;  в том числе для отрицательных индексов.

# ; *Пример:*

# ; - для k = 8 
# ; список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print('Список чисел Фибоначчи, в том числе и для отрицательных чисел')
sp=[]
fibonacci=int(input('индекс='))
sum=0
a=0
b=1
for i in range(fibonacci+1): # 
    sum=a
    a=b
    b=a+sum
    sp.append(sum)
sp2=[]
sum=0
a=0
b=1
for i in range(fibonacci): 
    sum=a
    a=b
    b=(a-sum)*(-1)
    sp2.insert((0),a)
sp3=[]
sp3=sp2+sp
print("Число Фибоначчи с отрицательныит числами \n", sp3)    


