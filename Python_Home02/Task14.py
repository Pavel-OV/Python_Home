# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
print('Bывести все целые степени двойки до числа N')
number=int(input('Введите число N='))
count=0
k=0
for i in range(number):
        count=2**k
        k=k+1
        if(count<number):
            print(count)